#!/usr/bin/env python3
"""
SEO Agent Library - Automated Marketing Case Study Generator
Transforms tracking data into compelling success stories and sales materials.
"""

import json
import yaml
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
import statistics
from dataclasses import dataclass, asdict
from collections import defaultdict
import re

@dataclass
class CaseStudyMetrics:
    """Key metrics for case study generation."""
    traffic_increase_percent: float
    traffic_increase_absolute: int
    ranking_improvement: int
    revenue_impact: float
    time_saved: int
    roi_percentage: float
    mission_count: int
    timeframe: str

@dataclass
class ClientProfile:
    """Client profile for case study personalization."""
    industry: str
    company_size: str
    challenge_type: str
    goals: List[str]
    website_type: str

class MarketingCaseStudyGenerator:
    """Generates compelling marketing case studies from tracking data."""
    
    def __init__(self, config_path: str = None):
        """Initialize the marketing generator."""
        self.config_path = config_path or "tracking/config/tracking.yml"
        self.config = self._load_config()
        self.tracking_dir = Path("tracking")
        self.marketing_dir = self.tracking_dir / "marketing"
        self.case_studies_dir = self.marketing_dir / "case-studies"
        self.templates_dir = self.marketing_dir / "templates"
        
        # Create directories
        for dir_path in [self.marketing_dir, self.case_studies_dir, self.templates_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration with marketing-specific defaults."""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            config = {}
        
        # Add marketing-specific defaults
        marketing_defaults = {
            'marketing': {
                'brand_name': 'SEO Agent Library',
                'brand_tagline': 'Elite SEO Operations Through AI Coordination',
                'contact_info': {
                    'website': 'https://seoagent.ai',
                    'email': 'success@seoagent.ai',
                    'phone': '+1-800-SEO-AGENT'
                },
                'success_metrics': {
                    'traffic_threshold': 25,  # Minimum % increase to highlight
                    'ranking_threshold': 5,   # Minimum position improvement
                    'roi_threshold': 200      # Minimum ROI % to feature
                }
            }
        }
        
        if 'marketing' not in config:
            config['marketing'] = marketing_defaults['marketing']
        
        return config
    
    def analyze_case_study_data(self, baseline_data: Dict[str, Any], 
                               current_data: Dict[str, Any]) -> CaseStudyMetrics:
        """Analyze data to extract key metrics for case studies."""
        
        # Traffic analysis
        baseline_traffic = baseline_data.get('traffic_metrics', {}).get('organic_traffic', {})
        current_traffic = current_data.get('traffic_metrics', {}).get('organic_traffic', {})
        
        baseline_sessions = baseline_traffic.get('sessions', 0)
        current_sessions = current_traffic.get('sessions', 0)
        
        if baseline_sessions > 0:
            traffic_increase_percent = ((current_sessions - baseline_sessions) / baseline_sessions) * 100
        else:
            traffic_increase_percent = 100.0 if current_sessions > 0 else 0.0
        
        traffic_increase_absolute = current_sessions - baseline_sessions
        
        # Ranking analysis
        baseline_rankings = baseline_data.get('ranking_metrics', {}).get('visibility', {})
        current_rankings = current_data.get('ranking_metrics', {}).get('visibility', {})
        
        baseline_position = baseline_rankings.get('average_position', 100)
        current_position = current_rankings.get('average_position', 100)
        ranking_improvement = baseline_position - current_position  # Lower is better
        
        # ROI calculation
        roi_config = self.config.get('roi', {})
        session_value = roi_config.get('organic_session_value', 2.50)
        conversion_rate = roi_config.get('conversion_rate', 0.02)
        avg_order_value = roi_config.get('average_order_value', 100)
        
        revenue_impact = traffic_increase_absolute * session_value * conversion_rate * avg_order_value
        
        # Estimate investment (could be tracked more precisely)
        estimated_investment = 5000  # Placeholder
        roi_percentage = (revenue_impact / estimated_investment) * 100 if estimated_investment > 0 else 0
        
        # Time calculations
        baseline_date = datetime.fromisoformat(baseline_data.get('metadata', {}).get('timestamp', '2024-01-01'))
        current_date = datetime.fromisoformat(current_data.get('metadata', {}).get('timestamp', '2024-02-01'))
        timeframe_days = (current_date - baseline_date).days
        
        if timeframe_days < 30:
            timeframe = f"{timeframe_days} days"
        elif timeframe_days < 365:
            timeframe = f"{timeframe_days // 30} months"
        else:
            timeframe = f"{timeframe_days // 365} years"
        
        return CaseStudyMetrics(
            traffic_increase_percent=traffic_increase_percent,
            traffic_increase_absolute=traffic_increase_absolute,
            ranking_improvement=ranking_improvement,
            revenue_impact=revenue_impact,
            time_saved=40,  # Hours saved through automation
            roi_percentage=roi_percentage,
            mission_count=3,  # Could be calculated from mission data
            timeframe=timeframe
        )
    
    def generate_headline_variations(self, metrics: CaseStudyMetrics, 
                                   client_profile: ClientProfile) -> List[str]:
        """Generate compelling headline variations for case studies."""
        
        headlines = []
        
        # Traffic-focused headlines
        if metrics.traffic_increase_percent >= self.config['marketing']['success_metrics']['traffic_threshold']:
            headlines.extend([
                f"How {client_profile.industry} Company Increased Organic Traffic by {metrics.traffic_increase_percent:.0f}% in {metrics.timeframe}",
                f"{metrics.traffic_increase_percent:.0f}% Organic Traffic Growth: {client_profile.industry} Success Story",
                f"From {metrics.traffic_increase_absolute:,} Visitors to Revenue: {client_profile.industry} SEO Transformation"
            ])
        
        # ROI-focused headlines
        if metrics.roi_percentage >= self.config['marketing']['success_metrics']['roi_threshold']:
            headlines.extend([
                f"{metrics.roi_percentage:.0f}% ROI: How SEO Agent Library Transformed {client_profile.industry} Business",
                f"${metrics.revenue_impact:,.0f} in Additional Revenue: {client_profile.industry} Case Study",
                f"From Investment to {metrics.roi_percentage:.0f}% Returns in {metrics.timeframe}"
            ])
        
        # Ranking-focused headlines
        if metrics.ranking_improvement >= self.config['marketing']['success_metrics']['ranking_threshold']:
            headlines.extend([
                f"Climbing {metrics.ranking_improvement} Positions: {client_profile.industry} SEO Success",
                f"How {client_profile.company_size} Company Dominated Search Results in {metrics.timeframe}",
                f"Top 10 Rankings Achieved: {client_profile.industry} SEO Breakthrough"
            ])
        
        # Time-saving headlines
        headlines.extend([
            f"Saving {metrics.time_saved} Hours Monthly: Automated SEO Success Story",
            f"From Manual to Automated: {client_profile.industry} SEO Efficiency Gains",
            f"{metrics.mission_count} Missions, {metrics.timeframe} Timeline: Complete SEO Transformation"
        ])
        
        return headlines
    
    def generate_case_study_narrative(self, metrics: CaseStudyMetrics, 
                                    client_profile: ClientProfile) -> Dict[str, str]:
        """Generate narrative sections for case study."""
        
        # Challenge section
        challenge_narratives = {
            'low_traffic': f"Like many {client_profile.industry} businesses, our client was struggling with limited organic visibility. Their website wasn't attracting enough qualified traffic to support business growth.",
            'poor_rankings': f"Despite having quality content, their {client_profile.website_type} wasn't ranking well for industry keywords, leaving significant market share on the table.",
            'manual_seo': f"Their team was spending countless hours on manual SEO tasks, limiting their ability to focus on strategic growth initiatives.",
            'competitive_pressure': f"Competitors were dominating search results for key {client_profile.industry} terms, making it difficult to capture market share."
        }
        
        challenge = challenge_narratives.get(client_profile.challenge_type, challenge_narratives['low_traffic'])
        
        # Solution section
        solution = f"""
        We deployed SEO Agent Library's coordinated AI specialist system to address their challenges systematically:
        
        - **@seo-strategist** analyzed market opportunities and competitive gaps
        - **@seo-technical** optimized Core Web Vitals and site performance  
        - **@seo-content** identified and filled content gaps
        - **@seo-researcher** uncovered high-value keyword opportunities
        - **@seo-analyst** provided continuous performance monitoring
        - **@seo-builder** implemented technical improvements
        
        All agents worked in coordination to deliver comprehensive SEO improvements while saving {metrics.time_saved} hours monthly through automation.
        """
        
        # Results section
        results = f"""
        The results exceeded expectations across all key metrics:
        
        **Traffic Growth**
        - {metrics.traffic_increase_percent:.0f}% increase in organic sessions
        - {metrics.traffic_increase_absolute:,} additional monthly visitors
        - Consistent upward trend maintained over {metrics.timeframe}
        
        **Search Visibility** 
        - Average ranking improved by {metrics.ranking_improvement} positions
        - Multiple keywords reached first page
        - Expanded presence for industry terms
        
        **Business Impact**
        - ${metrics.revenue_impact:,.0f} in attributed revenue
        - {metrics.roi_percentage:.0f}% return on investment
        - {metrics.mission_count} successful SEO missions completed
        
        **Operational Efficiency**
        - {metrics.time_saved} hours saved monthly through automation
        - Team freed to focus on strategic initiatives
        - Scalable system for ongoing growth
        """
        
        return {
            'challenge': challenge.strip(),
            'solution': solution.strip(),
            'results': results.strip()
        }
    
    def create_social_proof_elements(self, metrics: CaseStudyMetrics) -> Dict[str, str]:
        """Generate social proof elements for marketing."""
        
        # Key metrics for social sharing
        key_stats = [
            f"{metrics.traffic_increase_percent:.0f}% traffic increase",
            f"${metrics.revenue_impact:,.0f} revenue impact",
            f"{metrics.roi_percentage:.0f}% ROI achieved",
            f"{metrics.time_saved} hours saved monthly"
        ]
        
        # Tweet-sized success snippets
        tweet_snippets = [
            f"🚀 {metrics.traffic_increase_percent:.0f}% organic traffic growth in {metrics.timeframe} using SEO Agent Library's coordinated AI system",
            f"💰 ${metrics.revenue_impact:,.0f} in additional revenue from automated SEO optimization",
            f"⏰ Saving {metrics.time_saved} hours monthly while achieving {metrics.roi_percentage:.0f}% ROI",
            f"📈 From manual SEO to {metrics.mission_count} automated missions = {metrics.traffic_increase_percent:.0f}% growth"
        ]
        
        # LinkedIn post format
        linkedin_post = f"""
        SEO Success Story: {metrics.traffic_increase_percent:.0f}% Traffic Growth in {metrics.timeframe}
        
        The Challenge: Manual SEO processes limiting growth potential
        
        The Solution: SEO Agent Library's coordinated AI specialists
        - Automated technical optimization
        - Strategic content development  
        - Continuous performance monitoring
        - Competitive intelligence
        
        The Results:
        ✅ {metrics.traffic_increase_percent:.0f}% organic traffic increase
        ✅ ${metrics.revenue_impact:,.0f} revenue impact
        ✅ {metrics.roi_percentage:.0f}% return on investment
        ✅ {metrics.time_saved} hours saved monthly
        
        When AI agents work in coordination, results compound exponentially.
        
        What's your biggest SEO challenge?
        """
        
        return {
            'key_stats': key_stats,
            'tweet_snippets': tweet_snippets,
            'linkedin_post': linkedin_post.strip()
        }
    
    def generate_case_study_formats(self, metrics: CaseStudyMetrics, 
                                   client_profile: ClientProfile,
                                   output_formats: List[str] = None) -> Dict[str, str]:
        """Generate case study in multiple formats."""
        
        if output_formats is None:
            output_formats = ['full', 'executive', 'social', 'sales_deck']
        
        headlines = self.generate_headline_variations(metrics, client_profile)
        narrative = self.generate_case_study_narrative(metrics, client_profile)
        social_proof = self.create_social_proof_elements(metrics)
        
        formats = {}
        
        # Full case study format
        if 'full' in output_formats:
            formats['full'] = f"""
# {headlines[0]}

## Executive Summary
{client_profile.industry} company achieved {metrics.traffic_increase_percent:.0f}% organic traffic growth and {metrics.roi_percentage:.0f}% ROI in {metrics.timeframe} using SEO Agent Library's coordinated AI specialist system.

## The Challenge
{narrative['challenge']}

## Our Approach
{narrative['solution']}

## Results & Impact
{narrative['results']}

## Key Takeaways
- Coordinated AI agents deliver exponential results
- Automation saves {metrics.time_saved} hours monthly
- Strategic SEO drives measurable business growth
- {metrics.roi_percentage:.0f}% ROI proves investment value

## About SEO Agent Library
{self.config['marketing']['brand_tagline']}

Contact us to achieve similar results: {self.config['marketing']['contact_info']['email']}
"""
        
        # Executive summary format
        if 'executive' in output_formats:
            formats['executive'] = f"""
**{headlines[1]}**

**Challenge:** {client_profile.challenge_type.replace('_', ' ').title()}
**Solution:** SEO Agent Library coordination system
**Timeline:** {metrics.timeframe}

**Key Results:**
• {metrics.traffic_increase_percent:.0f}% organic traffic increase
• ${metrics.revenue_impact:,.0f} revenue impact  
• {metrics.roi_percentage:.0f}% return on investment
• {metrics.time_saved} hours saved monthly

**Business Impact:** Automated SEO coordination delivered measurable growth while freeing team for strategic initiatives.
"""
        
        # Social media format
        if 'social' in output_formats:
            formats['social'] = social_proof['linkedin_post']
        
        # Sales deck format
        if 'sales_deck' in output_formats:
            formats['sales_deck'] = f"""
# Case Study: {metrics.traffic_increase_percent:.0f}% Growth in {metrics.timeframe}

## Slide 1: The Challenge
"{narrative['challenge']}"

## Slide 2: Our Solution
- 6 AI specialists working in coordination
- Automated technical optimization
- Strategic content development
- Continuous monitoring & optimization

## Slide 3: Results That Matter
- **{metrics.traffic_increase_percent:.0f}%** traffic increase
- **${metrics.revenue_impact:,.0f}** revenue impact
- **{metrics.roi_percentage:.0f}%** return on investment
- **{metrics.time_saved} hours** saved monthly

## Slide 4: Why This Works
Coordinated AI agents deliver exponential results through:
✓ Systematic optimization approach
✓ Automated task execution  
✓ Continuous performance monitoring
✓ Strategic decision-making support
"""
        
        return formats
    
    def create_competitive_benchmark(self, current_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create competitive benchmarking data."""
        
        # Mock competitive data - would integrate with real tools
        industry_benchmarks = {
            'average_organic_sessions': 15000,
            'average_conversion_rate': 0.025,
            'average_page_speed': 75,
            'average_core_web_vitals': 80
        }
        
        current_metrics = current_data.get('traffic_metrics', {}).get('organic_traffic', {})
        current_sessions = current_metrics.get('sessions', 0)
        
        competitive_position = {
            'traffic_vs_average': ((current_sessions - industry_benchmarks['average_organic_sessions']) / 
                                 industry_benchmarks['average_organic_sessions']) * 100,
            'performance_percentile': 75,  # Would calculate from real data
            'market_opportunities': [
                'Voice search optimization potential',
                'Featured snippet opportunities', 
                'Local SEO expansion',
                'Content gap exploitation'
            ]
        }
        
        return competitive_position
    
    def export_case_study(self, case_study_data: Dict[str, Any], 
                         export_format: str = 'markdown') -> str:
        """Export case study in specified format."""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"case_study_{timestamp}.{export_format}"
        filepath = self.case_studies_dir / filename
        
        if export_format == 'markdown':
            content = case_study_data.get('full', '')
        elif export_format == 'json':
            content = json.dumps(case_study_data, indent=2)
        else:
            content = case_study_data.get('full', '')
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        return str(filepath)

def main():
    """CLI interface for case study generation."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate Marketing Case Studies")
    parser.add_argument("--baseline", help="Baseline data file path")
    parser.add_argument("--current", help="Current data file path") 
    parser.add_argument("--industry", default="Technology", help="Client industry")
    parser.add_argument("--formats", nargs='+', default=['full'], 
                       help="Output formats")
    parser.add_argument("--export", default='markdown',
                       choices=['markdown', 'json', 'html'])
    
    args = parser.parse_args()
    
    generator = MarketingCaseStudyGenerator()
    
    # Load data (would integrate with tracking system)
    if args.baseline and args.current:
        with open(args.baseline, 'r') as f:
            baseline_data = json.load(f)
        with open(args.current, 'r') as f:
            current_data = json.load(f)
        
        # Create client profile
        client_profile = ClientProfile(
            industry=args.industry,
            company_size="Mid-market", 
            challenge_type="low_traffic",
            goals=["Increase organic traffic", "Improve ROI"],
            website_type="corporate website"
        )
        
        # Generate case study
        metrics = generator.analyze_case_study_data(baseline_data, current_data)
        case_study = generator.generate_case_study_formats(metrics, client_profile, args.formats)
        
        # Export results
        export_path = generator.export_case_study(case_study, args.export)
        print(f"Case study generated: {export_path}")
        
        # Display preview
        if 'executive' in case_study:
            print("\n" + "="*50)
            print("EXECUTIVE SUMMARY PREVIEW")
            print("="*50)
            print(case_study['executive'])
    else:
        print("Please provide --baseline and --current data files")

if __name__ == "__main__":
    main()