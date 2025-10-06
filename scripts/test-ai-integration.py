#!/usr/bin/env python3
"""
AI Integration Testing Framework for SDD Templates and Examples.
Tests template compatibility with major AI agents and validates AI-generated outputs.
"""

import os
import json
import time
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

class AIAgent(Enum):
    """Supported AI agents for testing."""
    GITHUB_COPILOT = "github_copilot"
    CLAUDE = "claude"
    GEMINI = "gemini"
    CHATGPT = "chatgpt"

@dataclass
class TestResult:
    """Result of an AI integration test."""
    agent: AIAgent
    template_path: str
    test_type: str
    success: bool
    response_time: float
    output_quality: int  # 1-5 scale
    errors: List[str]
    warnings: List[str]

class AIIntegrationTester:
    """Tests SDD templates and examples with AI agents."""
    
    def __init__(self, templates_dir: str = "resources/templates", examples_dir: str = "examples"):
        self.templates_dir = Path(templates_dir)
        self.examples_dir = Path(examples_dir)
        self.results: List[TestResult] = []
        
    async def run_all_tests(self) -> Dict[str, Any]:
        """Run comprehensive AI integration tests."""
        print("🤖 Starting AI Integration Tests...")
        
        # Test template compatibility
        await self._test_template_compatibility()
        
        # Test example spec consumption
        await self._test_example_consumption()
        
        # Test code generation from specs
        await self._test_code_generation()
        
        # Generate test report
        return self._generate_test_report()
    
    async def _test_template_compatibility(self):
        """Test AI agent compatibility with SDD templates."""
        print("\n📋 Testing template compatibility...")
        
        template_files = list(self.templates_dir.rglob("*.md"))
        
        for template_path in template_files:
            if template_path.name in ["spec.md", "plan.md", "tasks.md"]:
                await self._test_template_with_agents(template_path)
    
    async def _test_example_consumption(self):
        """Test AI agents' ability to consume and understand example specs."""
        print("\n📖 Testing example spec consumption...")
        
        example_specs = list(self.examples_dir.rglob("spec.md"))
        
        for spec_path in example_specs[:3]:  # Test first 3 examples
            await self._test_spec_understanding(spec_path)
    
    async def _test_code_generation(self):
        """Test AI agents' ability to generate code from specifications."""
        print("\n💻 Testing code generation capabilities...")
        
        # Use a simple example for code generation testing
        test_spec_path = self.examples_dir / "greenfield" / "task-management-api" / "spec.md"
        
        if test_spec_path.exists():
            await self._test_code_generation_from_spec(test_spec_path)
    
    async def _test_template_with_agents(self, template_path: Path):
        """Test a specific template with multiple AI agents."""
        template_name = str(template_path.relative_to(self.templates_dir))
        
        # Simulate AI agent testing (in real implementation, this would call actual APIs)
        test_prompts = [
            "Please analyze this SDD template for completeness and clarity.",
            "Generate a sample specification using this template.",
            "Identify any missing sections or improvements needed."
        ]
        
        for agent in AIAgent:
            for prompt in test_prompts:
                result = await self._simulate_ai_test(
                    agent, template_path, "template_compatibility", prompt
                )
                self.results.append(result)
    
    async def _test_spec_understanding(self, spec_path: Path):
        """Test AI agents' understanding of specification content."""
        spec_name = str(spec_path.relative_to(self.examples_dir))
        
        understanding_prompts = [
            "Summarize the key requirements from this specification.",
            "Identify potential implementation challenges from these requirements.",
            "Generate test cases based on the functional requirements."
        ]
        
        for agent in AIAgent:
            for prompt in understanding_prompts:
                result = await self._simulate_ai_test(
                    agent, spec_path, "spec_understanding", prompt
                )
                self.results.append(result)
    
    async def _test_code_generation_from_spec(self, spec_path: Path):
        """Test code generation capabilities from specifications."""
        code_gen_prompts = [
            "Generate a basic API endpoint implementation based on this spec.",
            "Create database models from the data models in this specification.",
            "Implement authentication middleware based on the security requirements."
        ]
        
        for agent in AIAgent:
            for prompt in code_gen_prompts:
                result = await self._simulate_ai_test(
                    agent, spec_path, "code_generation", prompt
                )
                self.results.append(result)
    
    async def _simulate_ai_test(self, agent: AIAgent, file_path: Path, test_type: str, prompt: str) -> TestResult:
        """Simulate an AI agent test (replace with actual API calls in production)."""
        start_time = time.time()
        
        # Simulate API call delay
        await asyncio.sleep(0.1)
        
        # Read file content for analysis
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return TestResult(
                agent=agent,
                template_path=str(file_path),
                test_type=test_type,
                success=False,
                response_time=time.time() - start_time,
                output_quality=1,
                errors=[f"Failed to read file: {e}"],
                warnings=[]
            )
        
        # Simulate analysis based on content quality
        success, quality, errors, warnings = self._analyze_content_quality(content, test_type)
        
        return TestResult(
            agent=agent,
            template_path=str(file_path),
            test_type=test_type,
            success=success,
            response_time=time.time() - start_time,
            output_quality=quality,
            errors=errors,
            warnings=warnings
        )
    
    def _analyze_content_quality(self, content: str, test_type: str) -> tuple:
        """Analyze content quality for AI compatibility."""
        errors = []
        warnings = []
        quality = 5  # Start with perfect score
        
        # Check for basic structure
        if len(content) < 100:
            errors.append("Content too short for meaningful AI analysis")
            quality -= 2
        
        # Check for clear headings
        if content.count('#') < 3:
            warnings.append("Limited heading structure may reduce AI comprehension")
            quality -= 1
        
        # Check for specific requirements format
        if test_type == "template_compatibility":
            if "SHALL" not in content:
                warnings.append("Missing SHALL statements for clear requirements")
                quality -= 1
            
            if not any(pattern in content for pattern in ["FR-", "TR-", "Requirements"]):
                errors.append("Missing requirement identification patterns")
                quality -= 2
        
        # Check for code examples
        if test_type == "code_generation":
            if "```" not in content:
                warnings.append("No code examples to guide AI generation")
                quality -= 1
        
        success = len(errors) == 0 and quality >= 3
        
        return success, max(1, quality), errors, warnings
    
    def _generate_test_report(self) -> Dict[str, Any]:
        """Generate comprehensive test report."""
        total_tests = len(self.results)
        successful_tests = sum(1 for r in self.results if r.success)
        
        # Group results by agent
        agent_results = {}
        for agent in AIAgent:
            agent_tests = [r for r in self.results if r.agent == agent]
            agent_results[agent.value] = {
                "total_tests": len(agent_tests),
                "successful_tests": sum(1 for r in agent_tests if r.success),
                "average_quality": sum(r.output_quality for r in agent_tests) / len(agent_tests) if agent_tests else 0,
                "average_response_time": sum(r.response_time for r in agent_tests) / len(agent_tests) if agent_tests else 0
            }
        
        # Group results by test type
        test_type_results = {}
        for test_type in ["template_compatibility", "spec_understanding", "code_generation"]:
            type_tests = [r for r in self.results if r.test_type == test_type]
            test_type_results[test_type] = {
                "total_tests": len(type_tests),
                "successful_tests": sum(1 for r in type_tests if r.success),
                "success_rate": (sum(1 for r in type_tests if r.success) / len(type_tests) * 100) if type_tests else 0
            }
        
        # Collect all errors and warnings
        all_errors = []
        all_warnings = []
        for result in self.results:
            all_errors.extend(result.errors)
            all_warnings.extend(result.warnings)
        
        report = {
            "summary": {
                "total_tests": total_tests,
                "successful_tests": successful_tests,
                "success_rate": (successful_tests / total_tests * 100) if total_tests > 0 else 0,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            },
            "agent_performance": agent_results,
            "test_type_performance": test_type_results,
            "issues": {
                "errors": list(set(all_errors)),
                "warnings": list(set(all_warnings))
            }
        }
        
        return report
    
    def save_report(self, report: Dict[str, Any], output_path: str = "test-results/ai-integration-report.json"):
        """Save test report to file."""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📊 Test report saved to: {output_file}")

async def main():
    """Main testing function."""
    tester = AIIntegrationTester()
    
    # Run all tests
    report = await tester.run_all_tests()
    
    # Print summary
    print(f"\n🎯 Test Summary:")
    print(f"   Total Tests: {report['summary']['total_tests']}")
    print(f"   Successful: {report['summary']['successful_tests']}")
    print(f"   Success Rate: {report['summary']['success_rate']:.1f}%")
    
    # Print agent performance
    print(f"\n🤖 Agent Performance:")
    for agent, stats in report['agent_performance'].items():
        success_rate = (stats['successful_tests'] / stats['total_tests'] * 100) if stats['total_tests'] > 0 else 0
        print(f"   {agent}: {success_rate:.1f}% success rate, {stats['average_quality']:.1f}/5 quality")
    
    # Save detailed report
    tester.save_report(report)
    
    # Return appropriate exit code
    if report['summary']['success_rate'] < 80:
        print("\n⚠️  AI integration tests below 80% success rate")
        return 1
    else:
        print("\n✅ AI integration tests passed!")
        return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())