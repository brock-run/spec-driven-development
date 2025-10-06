#!/usr/bin/env python3
"""
Validation script for community launch readiness.
Checks that all required community infrastructure is in place.
"""

import os
import json
from pathlib import Path

def check_file_exists(path, description):
    """Check if a file exists and report status."""
    if Path(path).exists():
        print(f"✅ {description}: {path}")
        return True
    else:
        print(f"❌ {description}: {path} (MISSING)")
        return False

def check_directory_exists(path, description):
    """Check if a directory exists and report status."""
    if Path(path).is_dir():
        print(f"✅ {description}: {path}")
        return True
    else:
        print(f"❌ {description}: {path} (MISSING)")
        return False

def validate_json_file(path, description):
    """Validate that a JSON file exists and is valid."""
    if not Path(path).exists():
        print(f"❌ {description}: {path} (MISSING)")
        return False
    
    try:
        with open(path, 'r') as f:
            json.load(f)
        print(f"✅ {description}: {path}")
        return True
    except json.JSONDecodeError as e:
        print(f"❌ {description}: {path} (INVALID JSON: {e})")
        return False

def main():
    """Run comprehensive community setup validation."""
    print("🔍 Validating Community Launch Setup")
    print("=" * 50)
    
    checks_passed = 0
    total_checks = 0
    
    # GitHub Infrastructure
    print("\n📁 GitHub Infrastructure:")
    github_checks = [
        (".github/DISCUSSION_TEMPLATE/general.yml", "General discussion template"),
        (".github/DISCUSSION_TEMPLATE/show-and-tell.yml", "Show and tell template"),
        (".github/ISSUE_TEMPLATE/feedback.md", "Feedback issue template"),
        (".github/workflows/community-metrics.yml", "Community metrics workflow"),
        ("CODE_OF_CONDUCT.md", "Code of conduct"),
        ("CONTRIBUTING.md", "Contributing guidelines"),
    ]
    
    for path, desc in github_checks:
        if check_file_exists(path, desc):
            checks_passed += 1
        total_checks += 1
    
    # Analytics and Privacy
    print("\n📊 Analytics and Privacy:")
    analytics_checks = [
        ("analytics", "Analytics directory"),
        ("analytics/config.json", "Analytics configuration"),
        ("analytics/privacy-policy.md", "Privacy policy"),
        ("analytics/dashboard.md", "Community dashboard"),
    ]
    
    for path, desc in analytics_checks:
        if path.endswith('.json'):
            if validate_json_file(path, desc):
                checks_passed += 1
        elif Path(path).is_dir():
            if check_directory_exists(path, desc):
                checks_passed += 1
        else:
            if check_file_exists(path, desc):
                checks_passed += 1
        total_checks += 1
    
    # Community Documentation
    print("\n📚 Community Documentation:")
    docs_checks = [
        ("docs/community", "Community docs directory"),
        ("docs/community/feedback-process.md", "Feedback process documentation"),
        ("docs/community/launch-checklist.md", "Launch checklist"),
        ("docs/community/survey-templates.md", "Survey templates"),
    ]
    
    for path, desc in docs_checks:
        if Path(path).is_dir():
            if check_directory_exists(path, desc):
                checks_passed += 1
        else:
            if check_file_exists(path, desc):
                checks_passed += 1
        total_checks += 1
    
    # Scripts and Automation
    print("\n🔧 Scripts and Automation:")
    script_checks = [
        ("scripts/analytics-setup.py", "Analytics setup script"),
        ("scripts/validate-community-setup.py", "Community validation script"),
    ]
    
    for path, desc in script_checks:
        if check_file_exists(path, desc):
            checks_passed += 1
        total_checks += 1
    
    # Content Validation
    print("\n📝 Content Integration:")
    content_checks = []
    
    # Check if README has community sections
    if Path("README.md").exists():
        with open("README.md", "r") as f:
            readme_content = f.read()
            if "Contributing & Community" in readme_content:
                print("✅ README has community section")
                checks_passed += 1
            else:
                print("❌ README missing community section")
            if "Privacy & Analytics" in readme_content:
                print("✅ README has privacy section")
                checks_passed += 1
            else:
                print("❌ README missing privacy section")
    else:
        print("❌ README.md not found")
    
    total_checks += 2
    
    # Final Report
    print("\n" + "=" * 50)
    print(f"📊 VALIDATION SUMMARY")
    print(f"Checks passed: {checks_passed}/{total_checks}")
    
    if checks_passed == total_checks:
        print("🎉 ALL CHECKS PASSED - Ready for community launch!")
        return 0
    else:
        missing = total_checks - checks_passed
        print(f"⚠️  {missing} checks failed - Please address missing items before launch")
        return 1

if __name__ == "__main__":
    exit(main())