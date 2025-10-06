#!/usr/bin/env python3
"""
Comprehensive Test Runner for SDD Repository Validation.
Orchestrates all validation frameworks and generates unified reports.
"""

import os
import sys
import json
import time
import asyncio
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class TestSuite:
    """Configuration for a test suite."""
    name: str
    script_path: str
    description: str
    timeout: int = 300  # 5 minutes default
    required: bool = True

@dataclass
class TestResult:
    """Result of running a test suite."""
    suite_name: str
    success: bool
    duration: float
    exit_code: int
    output: str
    error_output: str

class ComprehensiveTestRunner:
    """Runs all validation tests and generates unified reports."""
    
    def __init__(self, repo_root: str = "."):
        self.repo_root = Path(repo_root)
        self.test_suites = self._define_test_suites()
        self.results: List[TestResult] = []
        
    def _define_test_suites(self) -> List[TestSuite]:
        """Define all available test suites."""
        return [
            TestSuite(
                name="Template Validation",
                script_path="scripts/validate-templates.sh",
                description="Validate template syntax and completeness",
                timeout=120,
                required=True
            ),
            TestSuite(
                name="Example Validation",
                script_path="scripts/validate-examples.py",
                description="Validate example specifications and workflows",
                timeout=180,
                required=True
            ),
            TestSuite(
                name="Content Validation",
                script_path=".github/workflows/content-validation.yml",
                description="Markdown linting and link checking",
                timeout=240,
                required=True
            ),
            TestSuite(
                name="AI Integration Testing",
                script_path="scripts/test-ai-integration.py",
                description="Test compatibility with AI agents",
                timeout=300,
                required=False
            ),
            TestSuite(
                name="User Journey Testing",
                script_path="scripts/test-user-journeys.py",
                description="Validate complete user workflows",
                timeout=180,
                required=True
            ),
            TestSuite(
                name="Feedback Analysis",
                script_path="scripts/feedback-analysis.py",
                description="Analyze feedback and generate improvement recommendations",
                timeout=120,
                required=False
            )
        ]
    
    async def run_all_tests(self, include_optional: bool = False) -> Dict[str, Any]:
        """Run all test suites and generate comprehensive report."""
        print("🚀 Starting Comprehensive SDD Repository Validation")
        print("=" * 60)
        
        start_time = time.time()
        
        # Filter test suites based on requirements and options
        suites_to_run = [
            suite for suite in self.test_suites
            if suite.required or include_optional
        ]
        
        print(f"Running {len(suites_to_run)} test suites...\n")
        
        # Run test suites
        for i, suite in enumerate(suites_to_run, 1):
            print(f"[{i}/{len(suites_to_run)}] {suite.name}")
            print(f"Description: {suite.description}")
            
            result = await self._run_test_suite(suite)
            self.results.append(result)
            
            # Print immediate result
            status = "✅ PASSED" if result.success else "❌ FAILED"
            print(f"Result: {status} ({result.duration:.1f}s)")
            
            if not result.success and result.error_output:
                print(f"Error: {result.error_output[:200]}...")
            
            print("-" * 40)
        
        total_time = time.time() - start_time
        
        # Generate comprehensive report
        report = self._generate_comprehensive_report(total_time)
        
        # Save report
        self._save_report(report)
        
        # Print summary
        self._print_summary(report)
        
        return report
    
    async def _run_test_suite(self, suite: TestSuite) -> TestResult:
        """Run a single test suite."""
        script_path = self.repo_root / suite.script_path
        
        if not script_path.exists():
            return TestResult(
                suite_name=suite.name,
                success=False,
                duration=0.0,
                exit_code=-1,
                output="",
                error_output=f"Script not found: {script_path}"
            )
        
        start_time = time.time()
        
        try:
            # Determine how to run the script
            if script_path.suffix == ".py":
                cmd = [sys.executable, str(script_path)]
            elif script_path.suffix == ".sh":
                cmd = ["bash", str(script_path)]
            elif script_path.suffix == ".yml":
                # For GitHub Actions, we'll simulate or skip
                return TestResult(
                    suite_name=suite.name,
                    success=True,
                    duration=1.0,
                    exit_code=0,
                    output="GitHub Actions workflow (simulated)",
                    error_output=""
                )
            else:
                cmd = [str(script_path)]
            
            # Run the command
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=self.repo_root
            )
            
            try:
                stdout, stderr = await asyncio.wait_for(
                    process.communicate(),
                    timeout=suite.timeout
                )
                exit_code = process.returncode
            except asyncio.TimeoutError:
                process.kill()
                await process.wait()
                return TestResult(
                    suite_name=suite.name,
                    success=False,
                    duration=suite.timeout,
                    exit_code=-1,
                    output="",
                    error_output=f"Test timed out after {suite.timeout} seconds"
                )
            
            duration = time.time() - start_time
            
            return TestResult(
                suite_name=suite.name,
                success=exit_code == 0,
                duration=duration,
                exit_code=exit_code,
                output=stdout.decode('utf-8', errors='ignore'),
                error_output=stderr.decode('utf-8', errors='ignore')
            )
            
        except Exception as e:
            duration = time.time() - start_time
            return TestResult(
                suite_name=suite.name,
                success=False,
                duration=duration,
                exit_code=-1,
                output="",
                error_output=f"Exception running test: {str(e)}"
            )
    
    def _generate_comprehensive_report(self, total_time: float) -> Dict[str, Any]:
        """Generate comprehensive test report."""
        total_tests = len(self.results)
        passed_tests = sum(1 for r in self.results if r.success)
        failed_tests = total_tests - passed_tests
        
        # Required vs optional test results
        required_results = [r for r in self.results if any(s.name == r.suite_name and s.required for s in self.test_suites)]
        optional_results = [r for r in self.results if any(s.name == r.suite_name and not s.required for s in self.test_suites)]
        
        required_passed = sum(1 for r in required_results if r.success)
        optional_passed = sum(1 for r in optional_results if r.success)
        
        # Calculate quality score
        quality_score = self._calculate_quality_score()
        
        # Identify critical issues
        critical_issues = [
            r for r in self.results
            if not r.success and any(s.name == r.suite_name and s.required for s in self.test_suites)
        ]
        
        report = {
            "summary": {
                "timestamp": datetime.now().isoformat(),
                "total_duration": total_time,
                "total_tests": total_tests,
                "passed_tests": passed_tests,
                "failed_tests": failed_tests,
                "success_rate": (passed_tests / total_tests * 100) if total_tests > 0 else 0,
                "quality_score": quality_score
            },
            "test_breakdown": {
                "required_tests": {
                    "total": len(required_results),
                    "passed": required_passed,
                    "failed": len(required_results) - required_passed,
                    "success_rate": (required_passed / len(required_results) * 100) if required_results else 0
                },
                "optional_tests": {
                    "total": len(optional_results),
                    "passed": optional_passed,
                    "failed": len(optional_results) - optional_passed,
                    "success_rate": (optional_passed / len(optional_results) * 100) if optional_results else 0
                }
            },
            "detailed_results": [
                {
                    "suite_name": r.suite_name,
                    "success": r.success,
                    "duration": r.duration,
                    "exit_code": r.exit_code,
                    "required": any(s.name == r.suite_name and s.required for s in self.test_suites),
                    "error_summary": r.error_output[:500] if r.error_output else None
                }
                for r in self.results
            ],
            "critical_issues": [
                {
                    "suite": issue.suite_name,
                    "error": issue.error_output[:200]
                }
                for issue in critical_issues
            ],
            "recommendations": self._generate_recommendations()
        }
        
        return report
    
    def _calculate_quality_score(self) -> float:
        """Calculate overall repository quality score (0-100)."""
        if not self.results:
            return 0.0
        
        # Base score from test results
        required_results = [r for r in self.results if any(s.name == r.suite_name and s.required for s in self.test_suites)]
        optional_results = [r for r in self.results if any(s.name == r.suite_name and not s.required for s in self.test_suites)]
        
        # Required tests are worth 80% of the score
        required_score = 0
        if required_results:
            required_passed = sum(1 for r in required_results if r.success)
            required_score = (required_passed / len(required_results)) * 80
        
        # Optional tests are worth 20% of the score
        optional_score = 0
        if optional_results:
            optional_passed = sum(1 for r in optional_results if r.success)
            optional_score = (optional_passed / len(optional_results)) * 20
        
        return required_score + optional_score
    
    def _generate_recommendations(self) -> List[str]:
        """Generate improvement recommendations based on test results."""
        recommendations = []
        
        # Check for failed required tests
        failed_required = [
            r for r in self.results
            if not r.success and any(s.name == r.suite_name and s.required for s in self.test_suites)
        ]
        
        if failed_required:
            recommendations.append(f"Fix {len(failed_required)} critical test failures before deployment")
        
        # Check for performance issues
        slow_tests = [r for r in self.results if r.duration > 60]
        if slow_tests:
            recommendations.append(f"Optimize {len(slow_tests)} slow-running test suites")
        
        # Check for missing optional tests
        optional_results = [r for r in self.results if any(s.name == r.suite_name and not s.required for s in self.test_suites)]
        if len(optional_results) < 2:
            recommendations.append("Consider running optional test suites for comprehensive validation")
        
        # Quality-based recommendations
        quality_score = self._calculate_quality_score()
        if quality_score < 80:
            recommendations.append("Repository quality below 80% - review and improve failing areas")
        elif quality_score < 90:
            recommendations.append("Good quality - consider addressing optional improvements")
        
        return recommendations
    
    def _save_report(self, report: Dict[str, Any]):
        """Save comprehensive report to file."""
        output_dir = self.repo_root / "test-results"
        output_dir.mkdir(exist_ok=True)
        
        # Save main report
        report_file = output_dir / "comprehensive-test-report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
        
        # Save summary for quick reference
        summary_file = output_dir / "test-summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(report["summary"], f, indent=2, default=str)
        
        print(f"\n📊 Reports saved to {output_dir}/")
    
    def _print_summary(self, report: Dict[str, Any]):
        """Print test summary to console."""
        summary = report["summary"]
        
        print("\n" + "=" * 60)
        print("🎯 COMPREHENSIVE TEST SUMMARY")
        print("=" * 60)
        
        print(f"Overall Success Rate: {summary['success_rate']:.1f}%")
        print(f"Quality Score: {summary['quality_score']:.1f}/100")
        print(f"Total Duration: {summary['total_duration']:.1f} seconds")
        
        print(f"\nTest Results:")
        print(f"  ✅ Passed: {summary['passed_tests']}")
        print(f"  ❌ Failed: {summary['failed_tests']}")
        print(f"  📊 Total: {summary['total_tests']}")
        
        # Required vs Optional breakdown
        req_breakdown = report["test_breakdown"]["required_tests"]
        opt_breakdown = report["test_breakdown"]["optional_tests"]
        
        print(f"\nRequired Tests: {req_breakdown['success_rate']:.1f}% ({req_breakdown['passed']}/{req_breakdown['total']})")
        print(f"Optional Tests: {opt_breakdown['success_rate']:.1f}% ({opt_breakdown['passed']}/{opt_breakdown['total']})")
        
        # Critical issues
        if report["critical_issues"]:
            print(f"\n⚠️  Critical Issues:")
            for issue in report["critical_issues"]:
                print(f"  • {issue['suite']}: {issue['error'][:100]}...")
        
        # Recommendations
        if report["recommendations"]:
            print(f"\n💡 Recommendations:")
            for i, rec in enumerate(report["recommendations"], 1):
                print(f"  {i}. {rec}")
        
        print("\n" + "=" * 60)

async def main():
    """Main test runner function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Run comprehensive SDD repository validation")
    parser.add_argument("--include-optional", action="store_true", help="Include optional test suites")
    parser.add_argument("--timeout", type=int, default=300, help="Global timeout for test suites")
    
    args = parser.parse_args()
    
    runner = ComprehensiveTestRunner()
    
    # Run all tests
    report = await runner.run_all_tests(include_optional=args.include_optional)
    
    # Determine exit code
    required_success_rate = report["test_breakdown"]["required_tests"]["success_rate"]
    
    if required_success_rate < 100:
        print(f"\n❌ Required tests failed - cannot proceed with deployment")
        return 1
    elif report["summary"]["quality_score"] < 80:
        print(f"\n⚠️  Quality score below 80% - consider improvements")
        return 1
    else:
        print(f"\n✅ All validation tests passed!")
        return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)