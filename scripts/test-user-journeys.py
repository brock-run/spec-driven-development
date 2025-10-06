#!/usr/bin/env python3
"""
User Journey Testing Framework for SDD Repository.
Tests complete user workflows from different entry points and validates user experience.
"""

import os
import json
import time
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

class UserType(Enum):
    """Different types of users accessing the SDD repository."""
    NEW_DEVELOPER = "new_developer"
    EXPERIENCED_DEVELOPER = "experienced_developer"
    PRODUCT_MANAGER = "product_manager"
    TEAM_LEAD = "team_lead"
    SPECIALIST = "specialist"

@dataclass
class JourneyStep:
    """A single step in a user journey."""
    step_name: str
    expected_file: str
    required_content: List[str]
    optional_content: List[str]
    success_criteria: str

@dataclass
class JourneyResult:
    """Result of a user journey test."""
    user_type: UserType
    journey_name: str
    total_steps: int
    completed_steps: int
    success_rate: float
    time_to_complete: float
    issues: List[str]
    recommendations: List[str]

class UserJourneyTester:
    """Tests complete user journeys through the SDD repository."""
    
    def __init__(self, repo_root: str = "."):
        self.repo_root = Path(repo_root)
        self.results: List[JourneyResult] = []
        
    def test_all_user_journeys(self) -> Dict[str, Any]:
        """Test all defined user journeys."""
        print("👥 Testing User Journeys...")
        
        # Define and test journeys for each user type
        self._test_new_developer_journey()
        self._test_experienced_developer_journey()
        self._test_product_manager_journey()
        self._test_team_lead_journey()
        self._test_specialist_journey()
        
        return self._generate_journey_report()
    
    def _test_new_developer_journey(self):
        """Test the journey of a new developer learning SDD."""
        journey_steps = [
            JourneyStep(
                step_name="Landing and Overview",
                expected_file="README.md",
                required_content=[
                    "Spec-Driven Development",
                    "getting started",
                    "new developers"
                ],
                optional_content=["quick start", "tutorial"],
                success_criteria="Clear introduction and navigation for beginners"
            ),
            JourneyStep(
                step_name="Getting Started Guide",
                expected_file="how-to/getting-started.md",
                required_content=[
                    "first spec",
                    "step-by-step",
                    "example"
                ],
                optional_content=["video", "interactive"],
                success_criteria="Actionable first steps for creating a spec"
            ),
            JourneyStep(
                step_name="New Developer Guidance",
                expected_file="audiences/new-developers.md",
                required_content=[
                    "SDD fundamentals",
                    "common pitfalls",
                    "first workflow"
                ],
                optional_content=["mentorship", "community"],
                success_criteria="Comprehensive guidance for SDD adoption"
            ),
            JourneyStep(
                step_name="Basic Template Usage",
                expected_file="resources/templates/base/spec.md",
                required_content=[
                    "functional requirements",
                    "technical requirements",
                    "acceptance criteria"
                ],
                optional_content=["examples", "comments"],
                success_criteria="Clear template structure with guidance"
            ),
            JourneyStep(
                step_name="First Tutorial",
                expected_file="training/hands-on/tutorial-1-first-workflow.md",
                required_content=[
                    "complete workflow",
                    "step by step",
                    "validation"
                ],
                optional_content=["exercises", "solutions"],
                success_criteria="Guided practice with real example"
            )
        ]
        
        result = self._execute_journey(UserType.NEW_DEVELOPER, "Complete Onboarding", journey_steps)
        self.results.append(result)
    
    def _test_experienced_developer_journey(self):
        """Test the journey of an experienced developer adopting SDD."""
        journey_steps = [
            JourneyStep(
                step_name="Advanced Guidance Access",
                expected_file="audiences/experienced-developers.md",
                required_content=[
                    "advanced planning",
                    "legacy integration",
                    "multi-agent"
                ],
                optional_content=["best practices", "optimization"],
                success_criteria="Advanced techniques and strategies"
            ),
            JourneyStep(
                step_name="Decision Tree Navigation",
                expected_file="resources/decision-trees/integration-strategy.md",
                required_content=[
                    "decision points",
                    "integration options",
                    "trade-offs"
                ],
                optional_content=["flowchart", "examples"],
                success_criteria="Clear decision-making framework"
            ),
            JourneyStep(
                step_name="Legacy Integration Example",
                expected_file="examples/legacy-integration/payment-modernization/spec.md",
                required_content=[
                    "legacy constraints",
                    "integration strategy",
                    "migration plan"
                ],
                optional_content=["risk mitigation", "rollback"],
                success_criteria="Real-world integration example"
            ),
            JourneyStep(
                step_name="Advanced Workflows",
                expected_file="how-to/advanced-flows.md",
                required_content=[
                    "complex scenarios",
                    "multi-system",
                    "orchestration"
                ],
                optional_content=["automation", "tooling"],
                success_criteria="Advanced implementation patterns"
            )
        ]
        
        result = self._execute_journey(UserType.EXPERIENCED_DEVELOPER, "Advanced Implementation", journey_steps)
        self.results.append(result)
    
    def _test_product_manager_journey(self):
        """Test the journey of a product manager using SDD for requirements."""
        journey_steps = [
            JourneyStep(
                step_name="PM-Specific Guidance",
                expected_file="audiences/product-managers.md",
                required_content=[
                    "PRD to spec",
                    "cross-functional",
                    "ChatPRD"
                ],
                optional_content=["collaboration", "templates"],
                success_criteria="PM-focused SDD guidance"
            ),
            JourneyStep(
                step_name="ChatPRD Integration",
                expected_file="how-to/chatprd-workflow-integration.md",
                required_content=[
                    "setup guide",
                    "workflow integration",
                    "collaboration"
                ],
                optional_content=["examples", "troubleshooting"],
                success_criteria="Clear ChatPRD integration instructions"
            ),
            JourneyStep(
                step_name="Cross-functional Checklist",
                expected_file="resources/checklists/cross-functional-review.md",
                required_content=[
                    "alignment validation",
                    "stakeholder review",
                    "sign-off process"
                ],
                optional_content=["templates", "automation"],
                success_criteria="Structured review process"
            )
        ]
        
        result = self._execute_journey(UserType.PRODUCT_MANAGER, "Requirements Management", journey_steps)
        self.results.append(result)
    
    def _test_team_lead_journey(self):
        """Test the journey of a team lead implementing SDD governance."""
        journey_steps = [
            JourneyStep(
                step_name="Team Lead Guidance",
                expected_file="audiences/team-leads.md",
                required_content=[
                    "governance framework",
                    "change management",
                    "team training"
                ],
                optional_content=["metrics", "success measurement"],
                success_criteria="Leadership and governance guidance"
            ),
            JourneyStep(
                step_name="Organizational Readiness",
                expected_file="resources/checklists/organizational-readiness.md",
                required_content=[
                    "readiness assessment",
                    "prerequisites",
                    "implementation plan"
                ],
                optional_content=["timeline", "resources"],
                success_criteria="Structured adoption framework"
            ),
            JourneyStep(
                step_name="Training Program",
                expected_file="training/index.md",
                required_content=[
                    "curriculum paths",
                    "role-based training",
                    "assessment"
                ],
                optional_content=["certification", "mentorship"],
                success_criteria="Comprehensive training framework"
            )
        ]
        
        result = self._execute_journey(UserType.TEAM_LEAD, "Team Implementation", journey_steps)
        self.results.append(result)
    
    def _test_specialist_journey(self):
        """Test the journey of a role-specific specialist (frontend, backend, etc.)."""
        journey_steps = [
            JourneyStep(
                step_name="Specialist Guidance",
                expected_file="audiences/specialists.md",
                required_content=[
                    "role-specific patterns",
                    "domain templates",
                    "integration guidance"
                ],
                optional_content=["best practices", "examples"],
                success_criteria="Role-specific SDD guidance"
            ),
            JourneyStep(
                step_name="Domain Template",
                expected_file="resources/templates/frontend/spec.md",
                required_content=[
                    "frontend requirements",
                    "UI specifications",
                    "user experience"
                ],
                optional_content=["accessibility", "performance"],
                success_criteria="Domain-specific template structure"
            ),
            JourneyStep(
                step_name="Integration Workflows",
                expected_file="how-to/tool-integration-workflows.md",
                required_content=[
                    "tool setup",
                    "workflow integration",
                    "best practices"
                ],
                optional_content=["automation", "troubleshooting"],
                success_criteria="Practical integration guidance"
            )
        ]
        
        result = self._execute_journey(UserType.SPECIALIST, "Domain Implementation", journey_steps)
        self.results.append(result)
    
    def _execute_journey(self, user_type: UserType, journey_name: str, steps: List[JourneyStep]) -> JourneyResult:
        """Execute a complete user journey and return results."""
        start_time = time.time()
        completed_steps = 0
        issues = []
        recommendations = []
        
        for step in steps:
            step_success = self._validate_journey_step(step)
            if step_success:
                completed_steps += 1
            else:
                issues.append(f"Failed step: {step.step_name}")
                recommendations.append(f"Improve {step.expected_file} for {step.success_criteria}")
        
        completion_time = time.time() - start_time
        success_rate = (completed_steps / len(steps)) * 100 if steps else 0
        
        return JourneyResult(
            user_type=user_type,
            journey_name=journey_name,
            total_steps=len(steps),
            completed_steps=completed_steps,
            success_rate=success_rate,
            time_to_complete=completion_time,
            issues=issues,
            recommendations=recommendations
        )
    
    def _validate_journey_step(self, step: JourneyStep) -> bool:
        """Validate a single journey step."""
        file_path = self.repo_root / step.expected_file
        
        if not file_path.exists():
            return False
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
        except Exception:
            return False
        
        # Check required content
        for required in step.required_content:
            if required.lower() not in content:
                return False
        
        # Check file length (minimum quality threshold)
        if len(content) < 200:
            return False
        
        return True
    
    def _generate_journey_report(self) -> Dict[str, Any]:
        """Generate comprehensive journey test report."""
        total_journeys = len(self.results)
        successful_journeys = sum(1 for r in self.results if r.success_rate >= 80)
        
        # Calculate overall metrics
        avg_success_rate = sum(r.success_rate for r in self.results) / total_journeys if total_journeys > 0 else 0
        avg_completion_time = sum(r.time_to_complete for r in self.results) / total_journeys if total_journeys > 0 else 0
        
        # Group results by user type
        user_type_results = {}
        for user_type in UserType:
            user_results = [r for r in self.results if r.user_type == user_type]
            if user_results:
                user_type_results[user_type.value] = {
                    "journeys_tested": len(user_results),
                    "average_success_rate": sum(r.success_rate for r in user_results) / len(user_results),
                    "total_issues": sum(len(r.issues) for r in user_results),
                    "journeys": [
                        {
                            "name": r.journey_name,
                            "success_rate": r.success_rate,
                            "completed_steps": f"{r.completed_steps}/{r.total_steps}",
                            "issues": r.issues
                        }
                        for r in user_results
                    ]
                }
        
        # Collect all recommendations
        all_recommendations = []
        for result in self.results:
            all_recommendations.extend(result.recommendations)
        
        # Remove duplicates and prioritize
        unique_recommendations = list(set(all_recommendations))
        
        report = {
            "summary": {
                "total_journeys": total_journeys,
                "successful_journeys": successful_journeys,
                "overall_success_rate": avg_success_rate,
                "average_completion_time": avg_completion_time,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            },
            "user_type_performance": user_type_results,
            "recommendations": unique_recommendations[:10],  # Top 10 recommendations
            "detailed_results": [
                {
                    "user_type": r.user_type.value,
                    "journey": r.journey_name,
                    "success_rate": r.success_rate,
                    "issues": r.issues
                }
                for r in self.results
            ]
        }
        
        return report
    
    def save_report(self, report: Dict[str, Any], output_path: str = "test-results/user-journey-report.json"):
        """Save journey test report to file."""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📊 Journey test report saved to: {output_file}")

def main():
    """Main testing function."""
    tester = UserJourneyTester()
    
    # Run all journey tests
    report = tester.test_all_user_journeys()
    
    # Print summary
    print(f"\n🎯 Journey Test Summary:")
    print(f"   Total Journeys: {report['summary']['total_journeys']}")
    print(f"   Successful Journeys: {report['summary']['successful_journeys']}")
    print(f"   Overall Success Rate: {report['summary']['overall_success_rate']:.1f}%")
    
    # Print user type performance
    print(f"\n👥 User Type Performance:")
    for user_type, stats in report['user_type_performance'].items():
        print(f"   {user_type.replace('_', ' ').title()}: {stats['average_success_rate']:.1f}% success rate")
    
    # Print top recommendations
    if report['recommendations']:
        print(f"\n💡 Top Recommendations:")
        for i, rec in enumerate(report['recommendations'][:5], 1):
            print(f"   {i}. {rec}")
    
    # Save detailed report
    tester.save_report(report)
    
    # Return appropriate exit code
    if report['summary']['overall_success_rate'] < 75:
        print("\n⚠️  User journey tests below 75% success rate")
        return 1
    else:
        print("\n✅ User journey tests passed!")
        return 0

if __name__ == "__main__":
    exit(main())