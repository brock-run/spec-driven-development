#!/bin/bash

# Template Validation Script
# Validates template structure, format, and completeness

set -e

echo "🎯 Template Validation Script"
echo "=============================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
TOTAL_TEMPLATES=0
VALID_TEMPLATES=0
WARNINGS=0
ERRORS=0

# Function to log messages
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
    ((WARNINGS++))
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
    ((ERRORS++))
}

# Function to validate base template structure
validate_base_templates() {
    log_info "Validating base templates..."
    
    base_templates=("spec.md" "plan.md" "tasks.md")
    base_dir="resources/templates/base"
    
    for template in "${base_templates[@]}"; do
        template_path="$base_dir/$template"
        
        if [ ! -f "$template_path" ]; then
            log_error "Missing base template: $template_path"
            return 1
        fi
        
        log_success "Found base template: $template"
        
        # Validate base template content
        validate_template_content "$template_path" "base"
    done
}

# Function to validate template content
validate_template_content() {
    local file="$1"
    local type="$2"
    
    log_info "Validating content: $(basename "$file")"
    
    # Check for front matter (if applicable)
    if head -n 1 "$file" | grep -q "^---"; then
        log_success "Has front matter: $file"
    fi
    
    # Check for placeholders
    if grep -q "\[.*\]" "$file"; then
        placeholder_count=$(grep -o "\[.*\]" "$file" | wc -l)
        log_success "Has $placeholder_count placeholders: $file"
    else
        log_warning "No placeholders found: $file"
    fi
    
    # Check for requirement references
    if grep -q "_Requirements:" "$file"; then
        req_count=$(grep -c "_Requirements:" "$file")
        log_success "Has $req_count requirement references: $file"
    else
        log_warning "No requirement references: $file"
    fi
    
    # Check for proper markdown structure
    if grep -q "^# " "$file"; then
        log_success "Has main heading: $file"
    else
        log_warning "Missing main heading: $file"
    fi
    
    # Validate specific template types
    case "$type" in
        "spec")
            validate_spec_template "$file"
            ;;
        "plan")
            validate_plan_template "$file"
            ;;
        "tasks")
            validate_tasks_template "$file"
            ;;
    esac
}

# Function to validate spec templates
validate_spec_template() {
    local file="$1"
    
    # Check for required sections
    required_sections=("User Story" "Acceptance Criteria")
    
    for section in "${required_sections[@]}"; do
        if grep -q "$section" "$file"; then
            log_success "Has '$section' section: $file"
        else
            log_warning "Missing '$section' section: $file"
        fi
    done
    
    # Check for EARS format
    if grep -q "WHEN.*THEN.*SHALL" "$file"; then
        log_success "Uses EARS format: $file"
    else
        log_warning "May not use EARS format: $file"
    fi
}

# Function to validate plan templates
validate_plan_template() {
    local file="$1"
    
    # Check for required sections
    required_sections=("Architecture" "Components" "Technical Constraints")
    
    for section in "${required_sections[@]}"; do
        if grep -qi "$section" "$file"; then
            log_success "Has '$section' section: $file"
        else
            log_warning "Missing '$section' section: $file"
        fi
    done
}

# Function to validate task templates
validate_tasks_template() {
    local file="$1"
    
    # Check for checkbox format
    if grep -q "- \[ \]" "$file"; then
        checkbox_count=$(grep -c "- \[ \]" "$file")
        log_success "Has $checkbox_count checkboxes: $file"
    else
        log_warning "No checkboxes found: $file"
    fi
    
    # Check for numbered tasks
    if grep -q "^- \[ \] [0-9]" "$file"; then
        log_success "Has numbered tasks: $file"
    else
        log_warning "Tasks may not be numbered: $file"
    fi
}

# Function to validate domain-specific templates
validate_domain_templates() {
    log_info "Validating domain-specific templates..."
    
    domains=("api" "backend" "frontend" "mobile")
    
    for domain in "${domains[@]}"; do
        domain_dir="resources/templates/$domain"
        
        if [ -d "$domain_dir" ]; then
            log_info "Checking $domain templates..."
            
            find "$domain_dir" -name "*.md" | while read template; do
                ((TOTAL_TEMPLATES++))
                
                # Determine template type from filename
                if [[ "$(basename "$template")" == *"spec"* ]]; then
                    validate_template_content "$template" "spec"
                elif [[ "$(basename "$template")" == *"plan"* ]]; then
                    validate_template_content "$template" "plan"
                elif [[ "$(basename "$template")" == *"task"* ]]; then
                    validate_template_content "$template" "tasks"
                else
                    validate_template_content "$template" "generic"
                fi
                
                ((VALID_TEMPLATES++))
            done
        else
            log_warning "Domain directory not found: $domain_dir"
        fi
    done
}

# Function to validate template metadata
validate_template_metadata() {
    log_info "Validating template metadata..."
    
    find resources/templates -name "*.md" | while read template; do
        # Check file naming convention
        basename=$(basename "$template" .md)
        if [[ "$basename" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
            log_success "Follows naming convention: $template"
        else
            log_warning "May not follow kebab-case: $template"
        fi
        
        # Check for documentation
        template_dir=$(dirname "$template")
        if [ -f "$template_dir/README.md" ]; then
            log_success "Has documentation: $template_dir"
        else
            log_warning "Missing README.md: $template_dir"
        fi
    done
}

# Function to validate template examples
validate_template_examples() {
    log_info "Validating template examples..."
    
    find resources/templates -name "*.md" | while read template; do
        # Check for example content
        if grep -q "Example:" "$template" || grep -q "Sample:" "$template"; then
            log_success "Has examples: $template"
        else
            log_warning "May be missing examples: $template"
        fi
        
        # Check for usage instructions
        if grep -q "Usage:" "$template" || grep -q "How to use:" "$template"; then
            log_success "Has usage instructions: $template"
        else
            log_warning "May be missing usage instructions: $template"
        fi
    done
}

# Function to check template compatibility
validate_template_compatibility() {
    log_info "Validating template compatibility..."
    
    # Check for AI agent compatibility notes
    find resources/templates -name "*.md" | while read template; do
        if grep -qi "copilot\|claude\|chatgpt\|ai agent" "$template"; then
            log_success "Has AI compatibility notes: $template"
        else
            log_warning "Missing AI compatibility info: $template"
        fi
    done
}

# Main validation function
main() {
    log_info "Starting template validation..."
    echo
    
    # Validate base templates
    validate_base_templates
    echo
    
    # Validate domain-specific templates
    validate_domain_templates
    echo
    
    # Validate metadata
    validate_template_metadata
    echo
    
    # Validate examples
    validate_template_examples
    echo
    
    # Validate compatibility
    validate_template_compatibility
    echo
    
    # Summary
    echo "=============================="
    log_info "Validation Summary"
    echo "Total templates processed: $TOTAL_TEMPLATES"
    echo "Valid templates: $VALID_TEMPLATES"
    echo "Warnings: $WARNINGS"
    echo "Errors: $ERRORS"
    
    if [ $ERRORS -eq 0 ]; then
        log_success "Template validation completed successfully!"
        if [ $WARNINGS -gt 0 ]; then
            log_warning "Consider addressing the warnings above"
        fi
        exit 0
    else
        log_error "Template validation failed with $ERRORS errors"
        exit 1
    fi
}

# Run main function
main "$@"