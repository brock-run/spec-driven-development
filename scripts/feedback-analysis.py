#!/usr/bin/env python3
"""
Feedback Collection and Analysis System for SDD Repository.
Analyzes GitHub issues, discussions, and usage patterns to improve content quality.
"""

import os
import json
import re
import time
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from collections import defaultdict, Counter
from datetime import datetime, timedelta

@dataclass
class FeedbackItem:
    """A single piece of feedback from users."""
    source: str  # 'issue', 'discussion', 'pr_comment', 'survey'
    type: str    # 'bug', 'enhancement', 'question', 'documentation'
    title: str
    content: str
    labels: List[str]
    sentiment: str  # 'positive', 'negative', 'neutral'
    priority: int   # 1-5 scale
    created_at: datetime
    related_files: List[str]

@dataclass
class ContentMetrics:
    """Metrics for content usage and effectiveness."""
    file_path: str
    view_count: int
    engagement_score: float
    feedback_count: int
    positive_feedback: int
    negative_feedback: int
    improvement_suggestions: List[str]

class FeedbackAnalyzer:
    """Analyzes feedback and generates improvement recommendations."""
    
    def __init__(self, repo_root: str = "."):
        self.repo_root = Path(repo_root)
        self.feedback_items: List[FeedbackItem] = []
        self.content_metrics: Dict[str, ContentMetrics] = {}
        
    def analyze_feedback(self) -> Dict[str, Any]:
        """Perform comprehensive feedback analysis."""
        print("📊 Analyzing feedback and usage patterns...")
        
        # Collect feedback from various sources
        self._collect_simulated_feedback()
        
        # Analyze content effectiveness
        self._analyze_content_metrics()
        
        # Generate improvement recommendations
        recommendations = self._generate_recommendations()
        
        # Create analysis report
        return self._create_analysis_report(recommendations)
    
    def _collect_simulated_feedback(self):
        """Simulate feedback collection (replace with actual GitHub API calls)."""
        # Simulate various types of feedback
        simulated_feedback = [
            {
                "source": "issue",
                "type": "documentation",
                "title": "Getting started guide needs more examples",
                "content": "The getting started guide is helpful but could use more concrete examples for different project types.",
                "labels": ["documentation", "enhancement"],
                "sentiment": "neutral",
                "priority": 3,
                "related_files": ["how-to/getting-started.md"]
            },
            {
                "source": "discussion",
                "type": "question",
                "title": "How to integrate with existing CI/CD?",
                "content": "Looking for guidance on integrating SDD workflows with existing Jenkins pipelines.",
                "labels": ["question", "integration"],
                "sentiment": "neutral",
                "priority": 4,
                "related_files": ["how-to/advanced-flows.md"]
            },
            {
                "source": "issue",
                "type": "bug",
                "title": "Template validation script fails on Windows",
                "content": "The validate-templates.sh script doesn't work on Windows environments.",
                "labels": ["bug", "windows", "scripts"],
                "sentiment": "negative",
                "priority": 3,
                "related_files": ["scripts/validate-templates.sh"]
            },
            {
                "source": "pr_comment",
                "type": "enhancement",
                "title": "Add mobile app template",
                "content": "Would be great to have a specific template for mobile app development with React Native.",
                "labels": ["enhancement", "template", "mobile"],
                "sentiment": "positive",
                "priority": 4,
                "related_files": ["resources/templates/"]
            },
            {
                "source": "survey",
                "type": "documentation",
                "title": "Decision trees are very helpful",
                "content": "The decision trees really help with choosing the right approach for our legacy system integration.",
                "labels": ["positive", "decision-trees"],
                "sentiment": "positive",
                "priority": 2,
                "related_files": ["resources/decision-trees/integration-strategy.md"]
            }
        ]
        
        for item_data in simulated_feedback:
            feedback_item = FeedbackItem(
                source=item_data["source"],
                type=item_data["type"],
                title=item_data["title"],
                content=item_data["content"],
                labels=item_data["labels"],
                sentiment=item_data["sentiment"],
                priority=item_data["priority"],
                created_at=datetime.now() - timedelta(days=item_data.get("days_ago", 1)),
                related_files=item_data["related_files"]
            )
            self.feedback_items.append(feedback_item)
    
    def _analyze_content_metrics(self):
        """Analyze content effectiveness based on feedback and usage."""
        # Initialize metrics for all content files
        content_files = []
        
        # Find all markdown files
        for pattern in ["**/*.md"]:
            content_files.extend(self.repo_root.glob(pattern))
        
        for file_path in content_files:
            relative_path = str(file_path.relative_to(self.repo_root))
            
            # Calculate metrics based on feedback
            related_feedback = [f for f in self.feedback_items if relative_path in f.related_files]
            
            positive_count = sum(1 for f in related_feedback if f.sentiment == "positive")
            negative_count = sum(1 for f in related_feedback if f.sentiment == "negative")
            
            # Simulate view count and engagement (replace with actual analytics)
            view_count = self._simulate_view_count(relative_path)
            engagement_score = self._calculate_engagement_score(relative_path, related_feedback)
            
            # Extract improvement suggestions from feedback
            suggestions = []
            for feedback in related_feedback:
                if feedback.type in ["enhancement", "documentation"]:
                    suggestions.append(feedback.title)
            
            self.content_metrics[relative_path] = ContentMetrics(
                file_path=relative_path,
                view_count=view_count,
                engagement_score=engagement_score,
                feedback_count=len(related_feedback),
                positive_feedback=positive_count,
                negative_feedback=negative_count,
                improvement_suggestions=suggestions
            )
    
    def _simulate_view_count(self, file_path: str) -> int:
        """Simulate view count based on file type and location."""
        # Simulate higher views for key files
        if "README.md" in file_path:
            return 1000 + hash(file_path) % 500
        elif "getting-started" in file_path:
            return 500 + hash(file_path) % 300
        elif file_path.startswith("examples/"):
            return 200 + hash(file_path) % 200
        elif file_path.startswith("how-to/"):
            return 150 + hash(file_path) % 150
        else:
            return 50 + hash(file_path) % 100
    
    def _calculate_engagement_score(self, file_path: str, feedback: List[FeedbackItem]) -> float:
        """Calculate engagement score based on feedback and file characteristics."""
        base_score = 3.0  # Start with neutral score
        
        # Adjust based on feedback sentiment
        for item in feedback:
            if item.sentiment == "positive":
                base_score += 0.5
            elif item.sentiment == "negative":
                base_score -= 0.3
        
        # Adjust based on file completeness (simulate)
        try:
            with open(self.repo_root / file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Longer, more structured content gets higher scores
            if len(content) > 2000:
                base_score += 0.5
            if content.count('#') >= 5:  # Good heading structure
                base_score += 0.3
            if '```' in content:  # Contains code examples
                base_score += 0.2
                
        except Exception:
            base_score -= 0.5
        
        return max(1.0, min(5.0, base_score))
    
    def _generate_recommendations(self) -> List[Dict[str, Any]]:
        """Generate improvement recommendations based on analysis."""
        recommendations = []
        
        # Analyze feedback patterns
        feedback_by_type = defaultdict(list)
        for feedback in self.feedback_items:
            feedback_by_type[feedback.type].append(feedback)
        
        # High-priority issues
        high_priority_issues = [f for f in self.feedback_items if f.priority >= 4]
        if high_priority_issues:
            recommendations.append({
                "category": "Critical Issues",
                "priority": 5,
                "description": f"Address {len(high_priority_issues)} high-priority issues",
                "actions": [f.title for f in high_priority_issues[:5]],
                "affected_files": list(set(file for f in high_priority_issues for file in f.related_files))
            })
        
        # Documentation improvements
        doc_feedback = feedback_by_type.get("documentation", [])
        if doc_feedback:
            recommendations.append({
                "category": "Documentation Enhancement",
                "priority": 4,
                "description": f"Improve documentation based on {len(doc_feedback)} feedback items",
                "actions": [f.title for f in doc_feedback[:3]],
                "affected_files": list(set(file for f in doc_feedback for file in f.related_files))
            })
        
        # Content with low engagement
        low_engagement_content = [
            (path, metrics) for path, metrics in self.content_metrics.items()
            if metrics.engagement_score < 2.5 and metrics.view_count > 50
        ]
        
        if low_engagement_content:
            recommendations.append({
                "category": "Content Quality",
                "priority": 3,
                "description": f"Improve {len(low_engagement_content)} low-engagement content files",
                "actions": ["Add more examples", "Improve structure", "Add practical guidance"],
                "affected_files": [path for path, _ in low_engagement_content[:5]]
            })
        
        # Missing content (based on questions)
        questions = feedback_by_type.get("question", [])
        common_topics = Counter()
        for question in questions:
            # Extract topics from question content (simplified)
            words = re.findall(r'\b\w+\b', question.content.lower())
            for word in words:
                if len(word) > 4 and word not in ["with", "from", "that", "this", "have"]:
                    common_topics[word] += 1
        
        if common_topics:
            top_topics = [topic for topic, count in common_topics.most_common(3)]
            recommendations.append({
                "category": "Content Gaps",
                "priority": 4,
                "description": f"Create content for frequently asked topics: {', '.join(top_topics)}",
                "actions": [f"Create guide for {topic}" for topic in top_topics],
                "affected_files": ["how-to/", "examples/"]
            })
        
        # Sort recommendations by priority
        recommendations.sort(key=lambda x: x["priority"], reverse=True)
        
        return recommendations
    
    def _create_analysis_report(self, recommendations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create comprehensive analysis report."""
        # Calculate summary statistics
        total_feedback = len(self.feedback_items)
        positive_feedback = sum(1 for f in self.feedback_items if f.sentiment == "positive")
        negative_feedback = sum(1 for f in self.feedback_items if f.sentiment == "negative")
        
        # Feedback by source
        feedback_by_source = Counter(f.source for f in self.feedback_items)
        
        # Feedback by type
        feedback_by_type = Counter(f.type for f in self.feedback_items)
        
        # Top content by engagement
        top_content = sorted(
            self.content_metrics.items(),
            key=lambda x: x[1].engagement_score,
            reverse=True
        )[:10]
        
        # Content needing attention
        needs_attention = sorted(
            [(path, metrics) for path, metrics in self.content_metrics.items()
             if metrics.negative_feedback > 0 or metrics.engagement_score < 2.5],
            key=lambda x: (x[1].negative_feedback, -x[1].engagement_score),
            reverse=True
        )[:10]
        
        report = {
            "summary": {
                "total_feedback_items": total_feedback,
                "positive_feedback": positive_feedback,
                "negative_feedback": negative_feedback,
                "sentiment_ratio": positive_feedback / max(1, negative_feedback),
                "analysis_date": datetime.now().isoformat()
            },
            "feedback_breakdown": {
                "by_source": dict(feedback_by_source),
                "by_type": dict(feedback_by_type)
            },
            "content_performance": {
                "top_performing": [
                    {
                        "file": path,
                        "engagement_score": metrics.engagement_score,
                        "view_count": metrics.view_count,
                        "positive_feedback": metrics.positive_feedback
                    }
                    for path, metrics in top_content
                ],
                "needs_attention": [
                    {
                        "file": path,
                        "engagement_score": metrics.engagement_score,
                        "negative_feedback": metrics.negative_feedback,
                        "suggestions": metrics.improvement_suggestions
                    }
                    for path, metrics in needs_attention
                ]
            },
            "recommendations": recommendations,
            "action_items": [
                {
                    "priority": rec["priority"],
                    "category": rec["category"],
                    "description": rec["description"],
                    "next_steps": rec["actions"][:3]
                }
                for rec in recommendations[:5]
            ]
        }
        
        return report
    
    def save_report(self, report: Dict[str, Any], output_path: str = "test-results/feedback-analysis-report.json"):
        """Save feedback analysis report to file."""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"\n📊 Feedback analysis report saved to: {output_file}")

def main():
    """Main analysis function."""
    analyzer = FeedbackAnalyzer()
    
    # Run feedback analysis
    report = analyzer.analyze_feedback()
    
    # Print summary
    print(f"\n📈 Feedback Analysis Summary:")
    print(f"   Total Feedback Items: {report['summary']['total_feedback_items']}")
    print(f"   Positive Feedback: {report['summary']['positive_feedback']}")
    print(f"   Negative Feedback: {report['summary']['negative_feedback']}")
    print(f"   Sentiment Ratio: {report['summary']['sentiment_ratio']:.2f}")
    
    # Print top recommendations
    if report['recommendations']:
        print(f"\n🎯 Top Recommendations:")
        for i, rec in enumerate(report['recommendations'][:3], 1):
            print(f"   {i}. {rec['category']}: {rec['description']}")
    
    # Print content needing attention
    needs_attention = report['content_performance']['needs_attention']
    if needs_attention:
        print(f"\n⚠️  Content Needing Attention:")
        for item in needs_attention[:3]:
            print(f"   • {item['file']} (Score: {item['engagement_score']:.1f})")
    
    # Save detailed report
    analyzer.save_report(report)
    
    print("\n✅ Feedback analysis completed!")
    return 0

if __name__ == "__main__":
    exit(main())