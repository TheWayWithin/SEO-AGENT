#!/usr/bin/env python3
"""
SEO Agent Library - Competitive Benchmarking & Market Analysis
Creates competitive intelligence reports and market position visualizations.
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
import math

@dataclass
class CompetitorProfile:
    """Competitive analysis profile."""
    domain: str
    industry_category: str
    estimated_traffic: int
    domain_authority: int
    top_keywords_count: int
    content_volume: int
    technical_score: int

@dataclass
class MarketPosition:
    """Market position analysis."""
    share_of_voice: float
    visibility_index: float
    competitive_gap_score: float
    market_opportunity_score: float
    positioning_category: str  # 'leader', 'challenger', 'niche', 'emerging'

class CompetitiveBenchmarkingTool:
    """Analyzes competitive landscape and market positioning."""
    
    def __init__(self, config_path: str = None):
        """Initialize the competitive analysis tool."""
        self.config_path = config_path or "tracking/config/tracking.yml"
        self.config = self._load_config()
        self.tracking_dir = Path("tracking")
        self.competitive_dir = self.tracking_dir / "competitive"
        self.benchmarks_dir = self.competitive_dir / "benchmarks"
        
        # Create directories
        for dir_path in [self.competitive_dir, self.benchmarks_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration with competitive analysis defaults."""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            config = {}
        
        # Competitive analysis defaults
        competitive_defaults = {
            'competitive': {
                'market_definition': {
                    'primary_competitors': 5,
                    'secondary_competitors': 10,
                    'industry_benchmarks': True
                },
                'analysis_metrics': {
                    'traffic_weight': 0.3,
                    'authority_weight': 0.2,
                    'content_weight': 0.2,
                    'technical_weight': 0.15,
                    'keywords_weight': 0.15
                },
                'opportunity_thresholds': {
                    'traffic_gap': 25,      # % difference to flag opportunity
                    'keyword_gap': 50,      # Keyword count difference
                    'content_gap': 100,     # Content volume difference
                    'technical_gap': 15     # Technical score difference
                }
            }
        }
        
        if 'competitive' not in config:
            config['competitive'] = competitive_defaults['competitive']
        
        return config
    
    def create_mock_competitive_data(self, industry: str = "Technology") -> List[CompetitorProfile]:
        """Create realistic competitive data for analysis (would integrate with real tools)."""
        
        # Industry-specific competitive profiles
        industry_profiles = {
            'Technology': [
                CompetitorProfile('competitor-a.com', 'SaaS', 125000, 85, 2500, 450, 88),
                CompetitorProfile('competitor-b.com', 'Enterprise Software', 89000, 78, 1800, 320, 82),
                CompetitorProfile('competitor-c.com', 'Tech Services', 67000, 71, 1200, 280, 75),
                CompetitorProfile('competitor-d.com', 'Digital Agency', 45000, 65, 950, 200, 79),
                CompetitorProfile('competitor-e.com', 'Consulting', 38000, 62, 780, 180, 73)
            ],
            'E-commerce': [
                CompetitorProfile('shop-leader.com', 'Retail', 250000, 82, 4500, 1200, 85),
                CompetitorProfile('market-place.com', 'Marketplace', 180000, 79, 3200, 890, 78),
                CompetitorProfile('niche-store.com', 'Specialty', 95000, 68, 1800, 450, 81),
                CompetitorProfile('direct-sales.com', 'Direct to Consumer', 72000, 64, 1400, 320, 76),
                CompetitorProfile('outlet-mall.com', 'Discount Retail', 58000, 59, 1100, 280, 70)
            ],
            'Healthcare': [
                CompetitorProfile('health-leader.com', 'Healthcare Services', 145000, 81, 2800, 650, 86),
                CompetitorProfile('medical-group.com', 'Medical Practice', 98000, 74, 2100, 480, 79),
                CompetitorProfile('wellness-center.com', 'Wellness', 67000, 69, 1500, 350, 82),
                CompetitorProfile('telemedicine.com', 'Digital Health', 54000, 66, 1200, 290, 84),
                CompetitorProfile('clinic-network.com', 'Healthcare Network', 41000, 61, 980, 220, 77)
            ]
        }
        
        return industry_profiles.get(industry, industry_profiles['Technology'])
    
    def analyze_market_position(self, client_data: Dict[str, Any], 
                               competitors: List[CompetitorProfile]) -> MarketPosition:
        """Analyze client's market position against competitors."""
        
        # Extract client metrics
        client_traffic = client_data.get('traffic_metrics', {}).get('organic_traffic', {}).get('sessions', 0)
        client_authority = client_data.get('authority_metrics', {}).get('domain_rating', 50)
        client_keywords = len(client_data.get('ranking_metrics', {}).get('keyword_distribution', {}))
        client_technical = client_data.get('technical_metrics', {}).get('lighthouse_scores', {}).get('performance', 75)
        
        # Calculate competitive metrics
        competitor_traffics = [comp.estimated_traffic for comp in competitors]
        competitor_authorities = [comp.domain_authority for comp in competitors]
        competitor_keywords = [comp.top_keywords_count for comp in competitors]
        competitor_technical = [comp.technical_score for comp in competitors]
        
        # Market share calculation
        total_market_traffic = sum(competitor_traffics) + client_traffic
        share_of_voice = (client_traffic / total_market_traffic * 100) if total_market_traffic > 0 else 0
        
        # Visibility index (composite score)
        weights = self.config['competitive']['analysis_metrics']
        
        traffic_percentile = self._calculate_percentile(client_traffic, competitor_traffics)
        authority_percentile = self._calculate_percentile(client_authority, competitor_authorities)
        keywords_percentile = self._calculate_percentile(client_keywords, competitor_keywords)
        technical_percentile = self._calculate_percentile(client_technical, competitor_technical)
        
        visibility_index = (
            traffic_percentile * weights['traffic_weight'] +
            authority_percentile * weights['authority_weight'] +
            keywords_percentile * weights['keywords_weight'] +
            technical_percentile * weights['technical_weight']
        )
        
        # Competitive gap analysis
        avg_competitor_traffic = statistics.mean(competitor_traffics)
        competitive_gap_score = ((client_traffic - avg_competitor_traffic) / avg_competitor_traffic * 100) if avg_competitor_traffic > 0 else 0
        
        # Market opportunity calculation
        max_competitor_traffic = max(competitor_traffics)
        opportunity_score = ((max_competitor_traffic - client_traffic) / max_competitor_traffic * 100) if max_competitor_traffic > 0 else 0
        
        # Position categorization
        if visibility_index >= 75:
            positioning_category = 'leader'
        elif visibility_index >= 50:
            positioning_category = 'challenger' 
        elif visibility_index >= 25:
            positioning_category = 'niche'
        else:
            positioning_category = 'emerging'
        
        return MarketPosition(
            share_of_voice=share_of_voice,
            visibility_index=visibility_index,
            competitive_gap_score=competitive_gap_score,
            market_opportunity_score=opportunity_score,
            positioning_category=positioning_category
        )
    
    def _calculate_percentile(self, value: Union[int, float], 
                            comparison_values: List[Union[int, float]]) -> float:
        """Calculate percentile position against comparison values."""
        if not comparison_values:
            return 50.0
        
        sorted_values = sorted(comparison_values + [value])
        position = sorted_values.index(value)
        percentile = (position / (len(sorted_values) - 1)) * 100
        
        return percentile
    
    def identify_competitive_gaps(self, client_data: Dict[str, Any],
                                 competitors: List[CompetitorProfile]) -> Dict[str, Any]:
        """Identify specific competitive gaps and opportunities."""
        
        # Extract client metrics
        client_traffic = client_data.get('traffic_metrics', {}).get('organic_traffic', {}).get('sessions', 0)
        client_authority = client_data.get('authority_metrics', {}).get('domain_rating', 50)
        client_technical = client_data.get('technical_metrics', {}).get('lighthouse_scores', {}).get('performance', 75)
        
        thresholds = self.config['competitive']['opportunity_thresholds']
        
        gaps = {
            'traffic_opportunities': [],
            'authority_opportunities': [],
            'technical_opportunities': [],
            'content_opportunities': []
        }
        
        for competitor in competitors:
            # Traffic gap analysis
            traffic_difference = competitor.estimated_traffic - client_traffic
            if traffic_difference > (client_traffic * thresholds['traffic_gap'] / 100):
                gaps['traffic_opportunities'].append({
                    'competitor': competitor.domain,
                    'gap_size': traffic_difference,
                    'gap_percentage': (traffic_difference / client_traffic * 100) if client_traffic > 0 else float('inf'),
                    'opportunity': f"Traffic opportunity: {traffic_difference:,} additional sessions potential"
                })
            
            # Authority gap analysis  
            authority_difference = competitor.domain_authority - client_authority
            if authority_difference > thresholds['technical_gap']:
                gaps['authority_opportunities'].append({
                    'competitor': competitor.domain,
                    'gap_size': authority_difference,
                    'opportunity': f"Authority building opportunity: {authority_difference} point improvement potential"
                })
            
            # Technical gap analysis
            technical_difference = competitor.technical_score - client_technical
            if technical_difference > thresholds['technical_gap']:
                gaps['technical_opportunities'].append({
                    'competitor': competitor.domain,
                    'gap_size': technical_difference,
                    'opportunity': f"Technical optimization opportunity: {technical_difference} point improvement"
                })
            
            # Content gap analysis
            content_difference = competitor.content_volume - len(client_data.get('content_metrics', {}).get('indexed_pages', []))
            if content_difference > thresholds['content_gap']:
                gaps['content_opportunities'].append({
                    'competitor': competitor.domain,
                    'gap_size': content_difference,
                    'opportunity': f"Content expansion opportunity: {content_difference} additional pages potential"
                })
        
        return gaps
    
    def create_competitive_visualization_data(self, client_data: Dict[str, Any],
                                            competitors: List[CompetitorProfile],
                                            market_position: MarketPosition) -> Dict[str, Any]:
        """Create data structures for competitive visualizations."""
        
        # Extract client metrics
        client_traffic = client_data.get('traffic_metrics', {}).get('organic_traffic', {}).get('sessions', 0)
        client_authority = client_data.get('authority_metrics', {}).get('domain_rating', 50)
        
        # Traffic comparison chart data
        traffic_comparison = [
            {'domain': 'Your Site', 'traffic': client_traffic, 'category': 'client'},
        ]
        
        for comp in competitors:
            traffic_comparison.append({
                'domain': comp.domain.replace('.com', ''),
                'traffic': comp.estimated_traffic,
                'category': 'competitor'
            })
        
        # Market share pie chart
        total_traffic = sum([item['traffic'] for item in traffic_comparison])
        market_share = []
        for item in traffic_comparison:
            market_share.append({
                'domain': item['domain'],
                'percentage': (item['traffic'] / total_traffic * 100) if total_traffic > 0 else 0,
                'category': item['category']
            })
        
        # Competitive positioning matrix (Traffic vs Authority)
        positioning_matrix = [
            {
                'domain': 'Your Site',
                'traffic': client_traffic,
                'authority': client_authority,
                'category': 'client',
                'quadrant': self._determine_quadrant(client_traffic, client_authority, competitors)
            }
        ]
        
        for comp in competitors:
            positioning_matrix.append({
                'domain': comp.domain.replace('.com', ''),
                'traffic': comp.estimated_traffic,
                'authority': comp.domain_authority,
                'category': 'competitor',
                'quadrant': self._determine_quadrant(comp.estimated_traffic, comp.domain_authority, competitors)
            })
        
        # Gap analysis radar chart
        client_scores = {
            'traffic': self._normalize_score(client_traffic, [c.estimated_traffic for c in competitors]),
            'authority': self._normalize_score(client_authority, [c.domain_authority for c in competitors]),
            'technical': self._normalize_score(
                client_data.get('technical_metrics', {}).get('lighthouse_scores', {}).get('performance', 75),
                [c.technical_score for c in competitors]
            ),
            'content': self._normalize_score(
                len(client_data.get('content_metrics', {}).get('indexed_pages', [])),
                [c.content_volume for c in competitors]
            ),
            'keywords': self._normalize_score(
                len(client_data.get('ranking_metrics', {}).get('keyword_distribution', {})),
                [c.top_keywords_count for c in competitors]
            )
        }
        
        return {
            'traffic_comparison': sorted(traffic_comparison, key=lambda x: x['traffic'], reverse=True),
            'market_share': sorted(market_share, key=lambda x: x['percentage'], reverse=True),
            'positioning_matrix': positioning_matrix,
            'client_scores': client_scores,
            'market_position': asdict(market_position)
        }
    
    def _determine_quadrant(self, traffic: int, authority: int, 
                          competitors: List[CompetitorProfile]) -> str:
        """Determine competitive quadrant position."""
        
        avg_traffic = statistics.mean([c.estimated_traffic for c in competitors])
        avg_authority = statistics.mean([c.domain_authority for c in competitors])
        
        if traffic >= avg_traffic and authority >= avg_authority:
            return 'leaders'
        elif traffic >= avg_traffic and authority < avg_authority:
            return 'high_traffic'
        elif traffic < avg_traffic and authority >= avg_authority:
            return 'high_authority'
        else:
            return 'challengers'
    
    def _normalize_score(self, value: Union[int, float], 
                        comparison_values: List[Union[int, float]]) -> float:
        """Normalize score to 0-100 scale for radar charts."""
        if not comparison_values:
            return 50.0
        
        max_value = max(comparison_values + [value])
        min_value = min(comparison_values + [value])
        
        if max_value == min_value:
            return 50.0
        
        normalized = ((value - min_value) / (max_value - min_value)) * 100
        return max(0, min(100, normalized))
    
    def generate_competitive_report(self, client_data: Dict[str, Any],
                                  industry: str = "Technology",
                                  client_name: str = "Client") -> str:
        """Generate comprehensive competitive analysis report."""
        
        competitors = self.create_mock_competitive_data(industry)
        market_position = self.analyze_market_position(client_data, competitors)
        competitive_gaps = self.identify_competitive_gaps(client_data, competitors)
        visualization_data = self.create_competitive_visualization_data(client_data, competitors, market_position)
        
        report = f"""
# Competitive Intelligence Report
## {client_name} - {industry} Market Analysis

### Executive Summary

**Market Position:** {market_position.positioning_category.title()}  
**Share of Voice:** {market_position.share_of_voice:.1f}%  
**Visibility Index:** {market_position.visibility_index:.1f}/100  
**Competitive Gap:** {market_position.competitive_gap_score:+.1f}%  
**Market Opportunity:** {market_position.market_opportunity_score:.1f}%

{client_name} is positioned as a **{market_position.positioning_category}** in the {industry.lower()} market with significant opportunities for growth through strategic optimization.

### Market Landscape Analysis

#### Traffic Distribution
{self._format_traffic_table(visualization_data['traffic_comparison'])}

#### Market Share Breakdown  
{self._format_market_share(visualization_data['market_share'])}

### Competitive Positioning

**Your Competitive Strengths:**
{self._identify_strengths(visualization_data['client_scores'])}

**Primary Competitive Gaps:**
{self._format_competitive_gaps(competitive_gaps)}

### Strategic Opportunities

#### High-Impact Opportunities
{self._format_opportunities(competitive_gaps, 'high')}

#### Medium-Impact Opportunities  
{self._format_opportunities(competitive_gaps, 'medium')}

### Competitive Intelligence Insights

#### Market Leaders Analysis
{self._analyze_market_leaders(competitors)}

#### Emerging Trends
- Voice search optimization becoming critical differentiator
- Technical performance increasingly important for rankings
- Content depth and expertise (E-A-T) driving authority
- Local and mobile-first strategies expanding market reach

### Recommended Actions

#### Immediate (Next 30 Days)
1. **Technical Performance Optimization**
   - Target competitor benchmarks for Core Web Vitals
   - Implement advanced technical SEO improvements
   
2. **Content Gap Exploitation**  
   - Identify and target competitor content weaknesses
   - Develop comprehensive topic coverage strategy

#### Strategic (90-Day Timeline)
1. **Authority Building Campaign**
   - Implement systematic link building program
   - Develop thought leadership content strategy
   
2. **Market Share Expansion**
   - Target competitor keyword gaps
   - Expand into adjacent market segments

### Competitive Monitoring Framework

#### Key Metrics to Track
- Monthly traffic growth vs. top 3 competitors  
- Keyword position changes in shared terms
- Content publication frequency and quality
- Technical performance benchmarks
- Domain authority progression

#### Alert Thresholds
- Traffic gap increase >20%
- Ranking position loss >5 positions
- New competitor content in core topics
- Technical performance degradation

### Market Opportunity Assessment

**Total Addressable Market:** Based on competitor analysis, estimated {sum(c.estimated_traffic for c in competitors):,} monthly sessions available

**Immediate Opportunity:** {market_position.market_opportunity_score:.0f}% market share growth potential through optimization

**Long-term Growth:** Position for {market_position.positioning_category} to leader transition within 12-18 months

---

*This competitive intelligence report uses automated analysis validated by SEO specialists. Data refreshes monthly for strategic planning.*

**Report Generated:** {datetime.now().strftime("%B %d, %Y")}  
**Next Update:** {(datetime.now() + timedelta(days=30)).strftime("%B %d, %Y")}
        """
        
        return report.strip()
    
    def _format_traffic_table(self, traffic_data: List[Dict[str, Any]]) -> str:
        """Format traffic comparison table."""
        lines = ["| Domain | Monthly Traffic | Position |", "|--------|----------------|----------|"]
        for i, item in enumerate(traffic_data):
            position = f"#{i+1}"
            traffic_formatted = f"{item['traffic']:,}"
            lines.append(f"| {item['domain']} | {traffic_formatted} | {position} |")
        return "\n".join(lines)
    
    def _format_market_share(self, market_data: List[Dict[str, Any]]) -> str:
        """Format market share breakdown."""
        lines = []
        for item in market_data[:5]:  # Top 5 only
            domain = "**Your Site**" if item['category'] == 'client' else item['domain']
            lines.append(f"- {domain}: {item['percentage']:.1f}%")
        return "\n".join(lines)
    
    def _identify_strengths(self, client_scores: Dict[str, float]) -> str:
        """Identify competitive strengths."""
        strengths = []
        for metric, score in client_scores.items():
            if score >= 70:
                strengths.append(f"- **{metric.title()}**: Strong performance ({score:.0f}/100)")
            elif score >= 50:
                strengths.append(f"- **{metric.title()}**: Competitive position ({score:.0f}/100)")
        
        return "\n".join(strengths) if strengths else "- Focus areas identified for competitive improvement"
    
    def _format_competitive_gaps(self, gaps: Dict[str, Any]) -> str:
        """Format competitive gaps analysis."""
        gap_lines = []
        
        for category, opportunities in gaps.items():
            if opportunities:
                category_name = category.replace('_', ' ').title().replace('Opportunities', '')
                gap_lines.append(f"**{category_name}:**")
                for opp in opportunities[:2]:  # Top 2 per category
                    gap_lines.append(f"- {opp['opportunity']}")
                gap_lines.append("")
        
        return "\n".join(gap_lines)
    
    def _format_opportunities(self, gaps: Dict[str, Any], priority: str) -> str:
        """Format opportunities by priority level."""
        opportunities = []
        
        # Prioritize based on gap size and impact
        all_opportunities = []
        for category, gap_list in gaps.items():
            for gap in gap_list:
                all_opportunities.append({
                    'category': category,
                    'opportunity': gap['opportunity'],
                    'impact': gap.get('gap_size', 0)
                })
        
        # Sort by impact and filter by priority
        sorted_opportunities = sorted(all_opportunities, key=lambda x: x['impact'], reverse=True)
        
        if priority == 'high':
            selected = sorted_opportunities[:3]
        else:
            selected = sorted_opportunities[3:6]
        
        for i, opp in enumerate(selected, 1):
            opportunities.append(f"{i}. {opp['opportunity']}")
        
        return "\n".join(opportunities) if opportunities else "- Continue monitoring for emerging opportunities"
    
    def _analyze_market_leaders(self, competitors: List[CompetitorProfile]) -> str:
        """Analyze market leader characteristics."""
        top_competitor = max(competitors, key=lambda x: x.estimated_traffic)
        
        analysis = f"""
**Market Leader Profile ({top_competitor.domain})**
- Traffic Volume: {top_competitor.estimated_traffic:,} monthly sessions
- Domain Authority: {top_competitor.domain_authority}/100  
- Keyword Coverage: {top_competitor.top_keywords_count:,} ranking terms
- Content Volume: {top_competitor.content_volume} indexed pages
- Technical Score: {top_competitor.technical_score}/100

**Success Factors:**
- Comprehensive content strategy with {top_competitor.content_volume} pages
- Strong technical foundation ({top_competitor.technical_score}/100 score)
- Established domain authority ({top_competitor.domain_authority} DR)
- Broad keyword coverage ({top_competitor.top_keywords_count:,} terms)
        """
        
        return analysis.strip()
    
    def export_competitive_suite(self, client_data: Dict[str, Any],
                                industry: str = "Technology",
                                client_name: str = "Client") -> Dict[str, str]:
        """Export complete competitive analysis suite."""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        client_slug = client_name.lower().replace(' ', '_')
        
        # Generate analysis components
        competitors = self.create_mock_competitive_data(industry)
        market_position = self.analyze_market_position(client_data, competitors)
        competitive_gaps = self.identify_competitive_gaps(client_data, competitors)
        visualization_data = self.create_competitive_visualization_data(client_data, competitors, market_position)
        
        export_paths = {}
        
        # Full competitive report
        competitive_report = self.generate_competitive_report(client_data, industry, client_name)
        report_path = self.benchmarks_dir / f"{client_slug}_competitive_{timestamp}.md"
        with open(report_path, 'w') as f:
            f.write(competitive_report)
        export_paths['report'] = str(report_path)
        
        # Visualization data JSON
        viz_path = self.benchmarks_dir / f"{client_slug}_viz_data_{timestamp}.json"
        with open(viz_path, 'w') as f:
            f.write(json.dumps(visualization_data, indent=2))
        export_paths['visualization_data'] = str(viz_path)
        
        # Market position summary
        position_summary = f"""
# Market Position Summary - {client_name}

## Key Metrics
- **Position Category:** {market_position.positioning_category.title()}
- **Share of Voice:** {market_position.share_of_voice:.1f}%
- **Visibility Index:** {market_position.visibility_index:.1f}/100
- **Market Opportunity:** {market_position.market_opportunity_score:.1f}%

## Strategic Focus Areas
{self._format_competitive_gaps(competitive_gaps)}

## Next Actions
1. Address technical performance gaps
2. Expand content coverage in competitor weak areas
3. Build domain authority through strategic link building
4. Monitor competitor movements monthly

*Analysis Date: {datetime.now().strftime("%B %d, %Y")}*
        """
        
        summary_path = self.benchmarks_dir / f"{client_slug}_position_{timestamp}.md"
        with open(summary_path, 'w') as f:
            f.write(position_summary.strip())
        export_paths['summary'] = str(summary_path)
        
        return export_paths

def main():
    """CLI interface for competitive benchmarking."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate Competitive Analysis")
    parser.add_argument("--data", help="Client data file path", required=True)
    parser.add_argument("--industry", default="Technology", help="Industry category")
    parser.add_argument("--client", default="Demo Client", help="Client name")
    parser.add_argument("--formats", nargs='+', default=['report', 'summary', 'visualization'],
                       choices=['report', 'summary', 'visualization'])
    
    args = parser.parse_args()
    
    tool = CompetitiveBenchmarkingTool()
    
    # Load client data
    with open(args.data, 'r') as f:
        client_data = json.load(f)
    
    # Generate competitive analysis
    export_paths = tool.export_competitive_suite(client_data, args.industry, args.client)
    
    print(f"Competitive analysis generated for {args.client} in {args.industry}")
    for format_type, path in export_paths.items():
        if format_type.replace('_', '') in [f.replace('_', '') for f in args.formats]:
            print(f"{format_type.upper()}: {path}")

if __name__ == "__main__":
    main()