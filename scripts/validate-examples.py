#!/usr/bin/env python3
"""
Validation script for SDD example specifications and workflows.
Ensures all examples follow proper structure and contain required elements.
"""

import os
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class ExampleValidator:
    """Validates SDD examples for completeness and correctness."""
    
    def __init__(self, examples_dir: str = "examples"):
        self.examples_dir = Path(examples_dir)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def validate_all_examples(self) -> bool:
        """Validate all examples in the examples directory."""
        print("🔍 Validating SDD examples...")
        
        if not self.examples_dir.exists():
            self.errors.append(f"Examples directory '{self.examples_dir}' not found")
            return False
            
        # Validate directory structure
        self._validate_directory_structure()
        
        # Find and validate all example projects
        example_projects = self._find_example_projects()
        
        for project_path in example_projects:
            self._validate_example_project(project_path)
            
        # Print results
        self._print_results()
        
        return len(self.errors) == 0
    
    def _validate_directory_structure(self):
        """Validate the overall examples directory structure."""
        required_dirs = ["greenfield", "legacy-integration", "feature-addition", "workflows"]
        
        for dir_name in required_dirs:
            dir_path = self.examples_dir / dir_name
            if not dir_path.exists():
                self.errors.append(f"Missing required directory: {dir_path}")
                
        # Check for README.md in examples root
        readme_path = self.examples_dir / "README.md"
        if not readme_path.exists():
            self.errors.append("Missing README.md in examples directory")
        else:
            self._validate_readme_content(readme_path)
    
    def _find_example_projects(self) -> List[Path]:
        """Find all example project directories."""
        projects = []
        
        for category_dir in self.examples_dir.iterdir():
            if category_dir.is_dir() and category_dir.name != "__pycache__":
                for project_dir in category_dir.iterdir():
                    if project_dir.is_dir():
                        projects.append(project_dir)
                        
        return projects
    
    def _validate_example_project(self, project_path: Path):
        """Validate a single example project."""
        project_name = f"{project_path.parent.name}/{project_path.name}"
        
        # Check for required files
        required_files = ["README.md", "spec.md"]
        optional_files = ["plan.md", "tasks.md"]
        
        for file_name in required_files:
            file_path = project_path / file_name
            if not file_path.exists():
                self.errors.append(f"{project_name}: Missing required file {file_name}")
            else:
                self._validate_file_content(file_path, project_name)
                
        for file_name in optional_files:
            file_path = project_path / file_name
            if file_path.exists():
                self._validate_file_content(file_path, project_name)
    
    def _validate_file_content(self, file_path: Path, project_name: str):
        """Validate the content of a specific file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"{project_name}: Error reading {file_path.name}: {e}")
            return
            
        file_type = file_path.name
        
        if file_type == "README.md":
            self._validate_project_readme(content, project_name)
        elif file_type == "spec.md":
            self._validate_spec_file(content, project_name)
        elif file_type == "plan.md":
            self._validate_plan_file(content, project_name)
        elif file_type == "tasks.md":
            self._validate_tasks_file(content, project_name)
    
    def _validate_readme_content(self, readme_path: Path):
        """Validate examples directory README content."""
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Error reading examples README.md: {e}")
            return
            
        required_sections = [
            "# Example Specifications and Workflows",
            "## Directory Structure",
            "## How to Use These Examples"
        ]
        
        for section in required_sections:
            if section not in content:
                self.errors.append(f"Examples README.md missing section: {section}")
    
    def _validate_project_readme(self, content: str, project_name: str):
        """Validate project README content."""
        required_sections = [
            "## Project Context",
            "## Business Requirements", 
            "## Technical Constraints",
            "## SDD Workflow Files"
        ]
        
        for section in required_sections:
            if section not in content:
                self.warnings.append(f"{project_name}: README.md missing recommended section: {section}")
                
        # Check for validation results section
        if "## Validation Results" not in content:
            self.warnings.append(f"{project_name}: README.md missing validation results section")
    
    def _validate_spec_file(self, content: str, project_name: str):
        """Validate specification file content."""
        required_sections = [
            "# ",  # Title
            "## Overview",
            "## Functional Requirements",
            "## Technical Requirements"
        ]
        
        for section in required_sections:
            if section not in content:
                self.errors.append(f"{project_name}: spec.md missing required section: {section}")
        
        # Check for requirement format (FR-X.X, TR-X.X)
        fr_pattern = r'FR-\d+\.\d+'
        tr_pattern = r'TR-\d+\.\d+'
        
        fr_matches = re.findall(fr_pattern, content)
        tr_matches = re.findall(tr_pattern, content)
        
        if not fr_matches:
            self.errors.append(f"{project_name}: spec.md missing functional requirements (FR-X.X format)")
        if not tr_matches:
            self.errors.append(f"{project_name}: spec.md missing technical requirements (TR-X.X format)")
            
        # Check for SHALL statements
        shall_pattern = r'\bSHALL\b'
        shall_matches = re.findall(shall_pattern, content)
        
        if len(shall_matches) < 5:
            self.warnings.append(f"{project_name}: spec.md has few SHALL statements ({len(shall_matches)}), consider more specific requirements")
    
    def _validate_plan_file(self, content: str, project_name: str):
        """Validate technical plan file content."""
        recommended_sections = [
            "## Architecture Overview",
            "## Technology Stack",
            "## Database Design",
            "## Security Architecture"
        ]
        
        for section in recommended_sections:
            if section not in content:
                self.warnings.append(f"{project_name}: plan.md missing recommended section: {section}")
                
        # Check for code blocks (architecture diagrams, schemas)
        code_block_pattern = r'```'
        code_blocks = re.findall(code_block_pattern, content)
        
        if len(code_blocks) < 4:  # At least 2 code blocks (opening and closing)
            self.warnings.append(f"{project_name}: plan.md should include code examples or diagrams")
    
    def _validate_tasks_file(self, content: str, project_name: str):
        """Validate implementation tasks file content."""
        # Check for task format with checkboxes
        task_pattern = r'- \[ \] \d+\.'
        task_matches = re.findall(task_pattern, content)
        
        if not task_matches:
            self.errors.append(f"{project_name}: tasks.md missing properly formatted tasks (- [ ] X. format)")
            
        # Check for requirement references
        req_ref_pattern = r'_Requirements?: [A-Z]+-\d+\.\d+'
        req_refs = re.findall(req_ref_pattern, content)
        
        if not req_refs:
            self.errors.append(f"{project_name}: tasks.md missing requirement references (_Requirements: XX-X.X_)")
            
        # Check for sub-tasks
        subtask_pattern = r'- \[ \] \d+\.\d+'
        subtask_matches = re.findall(subtask_pattern, content)
        
        if len(subtask_matches) < 2:
            self.warnings.append(f"{project_name}: tasks.md should include sub-tasks for complex features")
    
    def _print_results(self):
        """Print validation results."""
        if self.errors:
            print(f"\n❌ Found {len(self.errors)} errors:")
            for error in self.errors:
                print(f"  • {error}")
                
        if self.warnings:
            print(f"\n⚠️  Found {len(self.warnings)} warnings:")
            for warning in self.warnings:
                print(f"  • {warning}")
                
        if not self.errors and not self.warnings:
            print("\n✅ All examples validated successfully!")
        elif not self.errors:
            print(f"\n✅ Validation passed with {len(self.warnings)} warnings")

def main():
    """Main validation function."""
    validator = ExampleValidator()
    success = validator.validate_all_examples()
    
    if not success:
        sys.exit(1)
    
    print("\n🎉 Example validation completed successfully!")

if __name__ == "__main__":
    main()