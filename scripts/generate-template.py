#!/usr/bin/env python3
"""
Template Generator Script

Creates new templates based on existing base templates with proper metadata
and structure validation.
"""

import json
import os
import sys
from pathlib import Path
from datetime import date
from typing import Dict, List, Any
import argparse

class TemplateGenerator:
    def __init__(self, base_template_dir: str = "resources/templates/base"):
        self.base_template_dir = Path(base_template_dir)
        self.template_types = ["spec", "plan", "tasks"]
        self.domains = ["api", "backend", "frontend", "mobile", "devops", "data", "ml"]
        self.complexities = ["basic", "intermediate", "advanced"]
        self.audiences = ["new-developer", "experienced-developer", "product-manager", "team-lead", "specialist"]
    
    def create_template(self, template_config: Dict[str, Any]) -> bool:
        """Create a new template based on configuration."""
        try:
            # Validate configuration
            if not self._validate_config(template_config):
                return False
            
            # Create template directory
            template_dir = Path(f"resources/templates/{template_config['domain']}")
            template_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate template file
            template_file = template_dir / f"{template_config['name']}.md"
            if not self._generate_template_file(template_config, template_file):
                return False
            
            # Generate metadata file
            metadata_file = template_dir / f"{template_config['name']}.meta.json"
            if not self._generate_metadata_file(template_config, metadata_file):
                return False
            
            # Update domain README if it doesn't exist
            readme_file = template_dir / "README.md"
            if not readme_file.exists():
                self._generate_domain_readme(template_config['domain'], readme_file)
            
            print(f"✅ Template created successfully:")
            print(f"   Template: {template_file}")
            print(f"   Metadata: {metadata_file}")
            
            return True
        
        except Exception as e:
            print(f"❌ Error creating template: {e}")
            return False
    
    def _validate_config(self, config: Dict[str, Any]) -> bool:
        """Validate template configuration."""
        required_fields = ['name', 'type', 'domain', 'complexity', 'audience', 'description']
        
        for field in required_fields:
            if field not in config:
                print(f"❌ Missing required field: {field}")
                return False
        
        # Validate enum values
        if config['type'] not in self.template_types:
            print(f"❌ Invalid template type: {config['type']}")
            print(f"   Valid types: {', '.join(self.template_types)}")
            return False
        
        if config['domain'] not in self.domains + ['base']:
            print(f"❌ Invalid domain: {config['domain']}")
            print(f"   Valid domains: {', '.join(self.domains)}")
            return False
        
        if config['complexity'] not in self.complexities:
            print(f"❌ Invalid complexity: {config['complexity']}")
            print(f"   Valid complexities: {', '.join(self.complexities)}")
            return False
        
        # Validate audience (can be list)
        audiences = config['audience'] if isinstance(config['audience'], list) else [config['audience']]
        for audience in audiences:
            if audience not in self.audiences + ['all']:
                print(f"❌ Invalid audience: {audience}")
                print(f"   Valid audiences: {', '.join(self.audiences + ['all'])}")
                return False
        
        return True
    
    def _generate_template_file(self, config: Dict[str, Any], output_file: Path) -> bool:
        """Generate the template markdown file."""
        try:
            # Load base template
            base_template_file = self.base_template_dir / f"{config['type']}.md"
            
            if not base_template_file.exists():
                print(f"❌ Base template not found: {base_template_file}")
                return False
            
            with open(base_template_file, 'r') as f:
                base_content = f.read()
            
            # Customize content for domain
            customized_content = self._customize_template_content(base_content, config)
            
            # Write template file
            with open(output_file, 'w') as f:
                f.write(customized_content)
            
            return True
        
        except Exception as e:
            print(f"❌ Error generating template file: {e}")
            return False
    
    def _customize_template_content(self, base_content: str, config: Dict[str, Any]) -> str:
        """Customize base template content for specific domain."""
        content = base_content
        
        # Add domain-specific header
        domain_header = f"# {config['description']}\n\n"
        domain_header += f"*Domain-specific template for {config['domain']} development*\n\n"
        domain_header += f"**Complexity Level:** {config['complexity'].title()}\n"
        domain_header += f"**Target Audience:** {', '.join(config['audience']) if isinstance(config['audience'], list) else config['audience']}\n\n"
        
        # Insert after first heading
        lines = content.split('\n')
        if lines and lines[0].startswith('#'):
            lines[0] = domain_header + lines[0]
        else:
            content = domain_header + content
        
        # Add domain-specific sections based on type and domain
        if config['type'] == 'spec':
            content = self._add_spec_domain_sections(content, config['domain'])
        elif config['type'] == 'plan':
            content = self._add_plan_domain_sections(content, config['domain'])
        elif config['type'] == 'tasks':
            content = self._add_tasks_domain_sections(content, config['domain'])
        
        return '\n'.join(lines) if 'lines' in locals() else content
    
    def _add_spec_domain_sections(self, content: str, domain: str) -> str:
        """Add domain-specific sections to spec templates."""
        domain_sections = {
            'api': [
                "\n## API Specifications\n",
                "### Endpoints\n",
                "- **[HTTP Method] [Endpoint Path]**\n",
                "  - Purpose: [endpoint purpose]\n",
                "  - Parameters: [parameter details]\n",
                "  - Response: [response format]\n",
                "\n### Data Models\n",
                "```json\n{\n  \"[model_name]\": {\n    \"[field]\": \"[type]\"\n  }\n}\n```\n"
            ],
            'frontend': [
                "\n## User Interface Specifications\n",
                "### Components\n",
                "- **[Component Name]**\n",
                "  - Purpose: [component purpose]\n",
                "  - Props: [prop specifications]\n",
                "  - State: [state management]\n",
                "\n### User Interactions\n",
                "- **[Interaction Type]**: [interaction description]\n"
            ],
            'backend': [
                "\n## Service Specifications\n",
                "### Services\n",
                "- **[Service Name]**\n",
                "  - Purpose: [service purpose]\n",
                "  - Dependencies: [service dependencies]\n",
                "  - Interface: [service interface]\n",
                "\n### Data Storage\n",
                "- **[Storage Type]**: [storage specifications]\n"
            ]
        }
        
        if domain in domain_sections:
            content += ''.join(domain_sections[domain])
        
        return content
    
    def _add_plan_domain_sections(self, content: str, domain: str) -> str:
        """Add domain-specific sections to plan templates."""
        # Similar implementation for plan templates
        return content
    
    def _add_tasks_domain_sections(self, content: str, domain: str) -> str:
        """Add domain-specific sections to task templates."""
        # Similar implementation for task templates
        return content
    
    def _generate_metadata_file(self, config: Dict[str, Any], output_file: Path) -> bool:
        """Generate the metadata JSON file."""
        try:
            # Load base metadata if extending
            base_metadata = {}
            if config.get('extends'):
                base_metadata_file = Path(config['extends']).with_suffix('.meta.json')
                if base_metadata_file.exists():
                    with open(base_metadata_file, 'r') as f:
                        base_metadata = json.load(f)
            
            # Create metadata structure
            metadata = {
                "template": {
                    "name": config['description'],
                    "version": config.get('version', '1.0.0'),
                    "type": config['type'],
                    "domain": config['domain'],
                    "complexity": config['complexity'],
                    "audience": config['audience'] if isinstance(config['audience'], list) else [config['audience']],
                    "description": config['description'],
                    "ai_compatibility": config.get('ai_compatibility', ["github-copilot", "claude", "chatgpt", "cursor", "kiro", "generic"]),
                    "requirements": config.get('requirements', []),
                    "tags": config.get('tags', [config['domain'], config['type'], config['complexity']])
                },
                "structure": base_metadata.get('structure', {
                    "sections": self._get_default_sections(config['type'], config['domain']),
                    "placeholders": self._get_default_placeholders(config['type'], config['domain'])
                }),
                "validation": base_metadata.get('validation', {
                    "rules": self._get_default_validation_rules(config['type'])
                }),
                "usage": {
                    "instructions": f"This template is optimized for {config['domain']} {config['type']} creation. {config.get('usage_instructions', '')}",
                    "examples": config.get('examples', []),
                    "prerequisites": config.get('prerequisites', []),
                    "related_templates": config.get('related_templates', [])
                },
                "maintenance": {
                    "created": str(date.today()),
                    "updated": str(date.today()),
                    "maintainer": config.get('maintainer', 'SDD Community'),
                    "status": config.get('status', 'draft')
                }
            }
            
            # Add extends if specified
            if config.get('extends'):
                metadata['template']['extends'] = config['extends']
            
            # Write metadata file
            with open(output_file, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            return True
        
        except Exception as e:
            print(f"❌ Error generating metadata file: {e}")
            return False
    
    def _get_default_sections(self, template_type: str, domain: str) -> List[Dict]:
        """Get default sections for template type and domain."""
        base_sections = {
            'spec': [
                {"name": "Overview", "required": True, "description": "High-level description"},
                {"name": "User Stories", "required": True, "description": "User-centered functionality descriptions"},
                {"name": "Acceptance Criteria", "required": True, "description": "Testable criteria using EARS format"}
            ],
            'plan': [
                {"name": "Architecture", "required": True, "description": "System architecture overview"},
                {"name": "Components", "required": True, "description": "System components and interfaces"},
                {"name": "Technical Constraints", "required": False, "description": "Technical limitations"}
            ],
            'tasks': [
                {"name": "Implementation Plan", "required": True, "description": "Ordered list of implementation tasks"}
            ]
        }
        
        sections = base_sections.get(template_type, [])
        
        # Add domain-specific sections
        domain_sections = {
            'api': [{"name": "API Specifications", "required": True, "description": "API endpoint specifications"}],
            'frontend': [{"name": "UI Specifications", "required": True, "description": "User interface specifications"}],
            'backend': [{"name": "Service Specifications", "required": True, "description": "Backend service specifications"}]
        }
        
        if domain in domain_sections:
            sections.extend(domain_sections[domain])
        
        return sections
    
    def _get_default_placeholders(self, template_type: str, domain: str) -> List[Dict]:
        """Get default placeholders for template type and domain."""
        base_placeholders = [
            {"name": "feature_name", "description": "Name of the feature", "required": True},
            {"name": "description", "description": "Feature description", "required": True}
        ]
        
        domain_placeholders = {
            'api': [
                {"name": "endpoint_path", "description": "API endpoint path", "required": True},
                {"name": "http_method", "description": "HTTP method", "required": True}
            ],
            'frontend': [
                {"name": "component_name", "description": "UI component name", "required": True},
                {"name": "user_interaction", "description": "User interaction type", "required": True}
            ]
        }
        
        placeholders = base_placeholders.copy()
        if domain in domain_placeholders:
            placeholders.extend(domain_placeholders[domain])
        
        return placeholders
    
    def _get_default_validation_rules(self, template_type: str) -> List[Dict]:
        """Get default validation rules for template type."""
        rules = {
            'spec': [
                {"type": "required_section", "target": "User Stories", "message": "Specification must include User Stories"},
                {"type": "required_section", "target": "Acceptance Criteria", "message": "Specification must include Acceptance Criteria"},
                {"type": "content_check", "target": "EARS format", "pattern": "WHEN.*THEN.*SHALL", "message": "Use EARS format for acceptance criteria"}
            ],
            'plan': [
                {"type": "required_section", "target": "Architecture", "message": "Plan must include Architecture section"},
                {"type": "required_section", "target": "Components", "message": "Plan must include Components section"}
            ],
            'tasks': [
                {"type": "content_check", "target": "checkboxes", "pattern": "- \\[ \\]", "message": "Tasks should use checkbox format"}
            ]
        }
        
        return rules.get(template_type, [])
    
    def _generate_domain_readme(self, domain: str, output_file: Path):
        """Generate README for domain directory."""
        readme_content = f"""# {domain.title()} Templates

This directory contains templates specifically designed for {domain} development within the Spec-Driven Development framework.

## Available Templates

<!-- This section will be automatically updated -->

## Usage

Each template includes:
- **Template file** (`.md`): The actual template with placeholders
- **Metadata file** (`.meta.json`): Template configuration and validation rules
- **Examples**: Sample usage scenarios and outputs

## Contributing

When adding new {domain} templates:
1. Follow the naming convention: `[template-name].md`
2. Include corresponding metadata: `[template-name].meta.json`
3. Test with at least one AI agent
4. Update this README with template information

## Domain-Specific Guidelines

### {domain.title()} Best Practices
- [Add domain-specific best practices here]
- [Include common patterns and anti-patterns]
- [Reference relevant tools and frameworks]

### Integration Points
- [List how these templates integrate with other domains]
- [Include workflow recommendations]
- [Reference related templates in other domains]
"""
        
        with open(output_file, 'w') as f:
            f.write(readme_content)

def interactive_template_creation():
    """Interactive template creation wizard."""
    print("🎯 SDD Template Generator")
    print("=" * 30)
    
    generator = TemplateGenerator()
    config = {}
    
    # Get basic information
    config['name'] = input("Template name (kebab-case): ").strip()
    config['description'] = input("Template description: ").strip()
    
    # Template type
    print(f"\nAvailable types: {', '.join(generator.template_types)}")
    config['type'] = input("Template type: ").strip()
    
    # Domain
    print(f"\nAvailable domains: {', '.join(generator.domains)}")
    config['domain'] = input("Domain: ").strip()
    
    # Complexity
    print(f"\nComplexity levels: {', '.join(generator.complexities)}")
    config['complexity'] = input("Complexity: ").strip()
    
    # Audience
    print(f"\nTarget audiences: {', '.join(generator.audiences + ['all'])}")
    audience_input = input("Target audience (comma-separated): ").strip()
    config['audience'] = [a.strip() for a in audience_input.split(',')]
    
    # Optional fields
    extends = input("Extends template (optional, path): ").strip()
    if extends:
        config['extends'] = extends
    
    requirements = input("Requirements addressed (comma-separated, optional): ").strip()
    if requirements:
        config['requirements'] = [r.strip() for r in requirements.split(',')]
    
    tags = input("Tags (comma-separated, optional): ").strip()
    if tags:
        config['tags'] = [t.strip() for t in tags.split(',')]
    
    # Create template
    print(f"\n🔨 Creating template...")
    if generator.create_template(config):
        print("✅ Template created successfully!")
    else:
        print("❌ Failed to create template")

def main():
    parser = argparse.ArgumentParser(description='Generate new SDD templates')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Interactive template creation')
    parser.add_argument('--config', '-c', type=str,
                       help='JSON config file for template creation')
    parser.add_argument('--list-domains', action='store_true',
                       help='List available domains')
    parser.add_argument('--list-types', action='store_true',
                       help='List available template types')
    
    args = parser.parse_args()
    
    generator = TemplateGenerator()
    
    if args.list_domains:
        print("Available domains:")
        for domain in generator.domains:
            print(f"  - {domain}")
        return
    
    if args.list_types:
        print("Available template types:")
        for template_type in generator.template_types:
            print(f"  - {template_type}")
        return
    
    if args.interactive:
        interactive_template_creation()
    elif args.config:
        try:
            with open(args.config, 'r') as f:
                config = json.load(f)
            
            if generator.create_template(config):
                print("✅ Template created successfully!")
            else:
                print("❌ Failed to create template")
                sys.exit(1)
        except Exception as e:
            print(f"❌ Error reading config file: {e}")
            sys.exit(1)
    else:
        print("Use --interactive for interactive creation or --config for config file")
        print("Use --help for more options")

if __name__ == '__main__':
    main()