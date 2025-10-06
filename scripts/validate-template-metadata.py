#!/usr/bin/env python3
"""
Template Metadata Validation Script

Validates template metadata against the schema and checks template content
against the metadata specifications.
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple
import argparse

class TemplateValidator:
    def __init__(self, schema_path: str):
        """Initialize validator with schema."""
        with open(schema_path, 'r') as f:
            self.schema = json.load(f)
        self.errors = []
        self.warnings = []
    
    def validate_metadata_file(self, metadata_path: str) -> bool:
        """Validate a metadata file against the schema."""
        try:
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
            
            # Basic schema validation (simplified)
            return self._validate_metadata_structure(metadata, metadata_path)
        
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON in {metadata_path}: {e}")
            return False
        except FileNotFoundError:
            self.errors.append(f"Metadata file not found: {metadata_path}")
            return False
    
    def _validate_metadata_structure(self, metadata: Dict, file_path: str) -> bool:
        """Validate metadata structure against schema."""
        valid = True
        
        # Check required top-level keys
        required_keys = ['template', 'structure', 'maintenance']
        for key in required_keys:
            if key not in metadata:
                self.errors.append(f"Missing required key '{key}' in {file_path}")
                valid = False
        
        # Validate template section
        if 'template' in metadata:
            template = metadata['template']
            template_required = ['name', 'version', 'type', 'domain', 'complexity', 'audience', 'description']
            for key in template_required:
                if key not in template:
                    self.errors.append(f"Missing required template key '{key}' in {file_path}")
                    valid = False
            
            # Validate version format
            if 'version' in template:
                if not re.match(r'^\d+\.\d+\.\d+$', template['version']):
                    self.errors.append(f"Invalid version format in {file_path}: {template['version']}")
                    valid = False
        
        return valid
    
    def validate_template_content(self, template_path: str, metadata_path: str) -> bool:
        """Validate template content against its metadata."""
        if not os.path.exists(metadata_path):
            self.warnings.append(f"No metadata file found for template: {template_path}")
            return True
        
        try:
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
            
            with open(template_path, 'r') as f:
                content = f.read()
            
            return self._validate_content_against_metadata(content, metadata, template_path)
        
        except Exception as e:
            self.errors.append(f"Error validating {template_path}: {e}")
            return False
    
    def _validate_content_against_metadata(self, content: str, metadata: Dict, template_path: str) -> bool:
        """Validate template content against metadata specifications."""
        valid = True
        
        # Check required sections
        if 'structure' in metadata and 'sections' in metadata['structure']:
            for section in metadata['structure']['sections']:
                if section.get('required', False):
                    section_pattern = f"#{1,6}\\s+{re.escape(section['name'])}"
                    if not re.search(section_pattern, content, re.IGNORECASE):
                        self.errors.append(f"Required section '{section['name']}' not found in {template_path}")
                        valid = False
        
        # Check placeholders
        if 'structure' in metadata and 'placeholders' in metadata['structure']:
            for placeholder in metadata['structure']['placeholders']:
                placeholder_pattern = f"\\[{re.escape(placeholder['name'])}\\]"
                if placeholder.get('required', False):
                    if not re.search(placeholder_pattern, content):
                        self.warnings.append(f"Required placeholder '[{placeholder['name']}]' not found in {template_path}")
        
        # Run validation rules
        if 'validation' in metadata and 'rules' in metadata['validation']:
            for rule in metadata['validation']['rules']:
                valid = self._apply_validation_rule(rule, content, template_path) and valid
        
        return valid
    
    def _apply_validation_rule(self, rule: Dict, content: str, template_path: str) -> bool:
        """Apply a specific validation rule."""
        rule_type = rule['type']
        target = rule['target']
        message = rule['message']
        
        if rule_type == 'required_section':
            section_pattern = f"#{1,6}\\s+{re.escape(target)}"
            if not re.search(section_pattern, content, re.IGNORECASE):
                self.errors.append(f"{template_path}: {message}")
                return False
        
        elif rule_type == 'content_check' and 'pattern' in rule:
            if not re.search(rule['pattern'], content):
                self.warnings.append(f"{template_path}: {message}")
        
        elif rule_type == 'format_check' and 'pattern' in rule:
            if not re.search(rule['pattern'], content):
                self.warnings.append(f"{template_path}: {message}")
        
        elif rule_type == 'required_placeholder':
            placeholder_pattern = f"\\[{re.escape(target)}\\]"
            if not re.search(placeholder_pattern, content):
                self.errors.append(f"{template_path}: {message}")
                return False
        
        return True
    
    def validate_template_directory(self, template_dir: str) -> Tuple[int, int]:
        """Validate all templates in a directory."""
        template_dir = Path(template_dir)
        validated_count = 0
        error_count = 0
        
        for template_file in template_dir.rglob("*.md"):
            # Skip README files
            if template_file.name.lower() == 'readme.md':
                continue
            
            # Find corresponding metadata file
            metadata_file = template_file.with_suffix('.meta.json')
            
            print(f"Validating: {template_file}")
            
            # Validate metadata if it exists
            if metadata_file.exists():
                if not self.validate_metadata_file(str(metadata_file)):
                    error_count += 1
                
                # Validate content against metadata
                if not self.validate_template_content(str(template_file), str(metadata_file)):
                    error_count += 1
            else:
                self.warnings.append(f"No metadata file for template: {template_file}")
            
            validated_count += 1
        
        return validated_count, error_count
    
    def generate_template_index(self, template_dir: str, output_file: str):
        """Generate an index of all templates with their metadata."""
        template_dir = Path(template_dir)
        templates = []
        
        for template_file in template_dir.rglob("*.md"):
            if template_file.name.lower() == 'readme.md':
                continue
            
            metadata_file = template_file.with_suffix('.meta.json')
            
            template_info = {
                'path': str(template_file.relative_to(template_dir)),
                'name': template_file.stem,
                'metadata': None
            }
            
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r') as f:
                        template_info['metadata'] = json.load(f)
                except Exception as e:
                    print(f"Error reading metadata for {template_file}: {e}")
            
            templates.append(template_info)
        
        # Sort by domain, then by complexity, then by name
        templates.sort(key=lambda x: (
            x['metadata']['template']['domain'] if x['metadata'] else 'zzz',
            x['metadata']['template']['complexity'] if x['metadata'] else 'zzz',
            x['name']
        ))
        
        with open(output_file, 'w') as f:
            json.dump(templates, f, indent=2)
        
        print(f"Template index generated: {output_file}")
    
    def print_summary(self):
        """Print validation summary."""
        print("\n" + "="*50)
        print("VALIDATION SUMMARY")
        print("="*50)
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  • {error}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  • {warning}")
        
        if not self.errors and not self.warnings:
            print("\n✅ All validations passed!")
        elif not self.errors:
            print(f"\n✅ Validation completed with {len(self.warnings)} warnings")
        else:
            print(f"\n❌ Validation failed with {len(self.errors)} errors and {len(self.warnings)} warnings")

def main():
    parser = argparse.ArgumentParser(description='Validate SDD templates and metadata')
    parser.add_argument('--template-dir', default='resources/templates', 
                       help='Directory containing templates')
    parser.add_argument('--schema', default='resources/templates/template-schema.json',
                       help='Path to template schema file')
    parser.add_argument('--generate-index', action='store_true',
                       help='Generate template index file')
    parser.add_argument('--index-output', default='resources/templates/template-index.json',
                       help='Output file for template index')
    
    args = parser.parse_args()
    
    # Check if schema exists
    if not os.path.exists(args.schema):
        print(f"❌ Schema file not found: {args.schema}")
        sys.exit(1)
    
    # Check if template directory exists
    if not os.path.exists(args.template_dir):
        print(f"❌ Template directory not found: {args.template_dir}")
        sys.exit(1)
    
    validator = TemplateValidator(args.schema)
    
    print(f"🎯 Validating templates in: {args.template_dir}")
    print(f"📋 Using schema: {args.schema}")
    print("-" * 50)
    
    validated_count, error_count = validator.validate_template_directory(args.template_dir)
    
    if args.generate_index:
        validator.generate_template_index(args.template_dir, args.index_output)
    
    validator.print_summary()
    
    print(f"\nProcessed {validated_count} templates")
    
    # Exit with error code if there were errors
    sys.exit(1 if error_count > 0 else 0)

if __name__ == '__main__':
    main()