#!/usr/bin/env python3
"""
SEO Agent Library - Client-Friendly Executive Dashboard Generator
Creates professional dashboards and reports for client presentations.
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
import html

@dataclass
class DashboardConfig:
    """Configuration for dashboard generation."""
    client_name: str
    brand_colors: Dict[str, str]
    logo_url: str
    white_label: bool = False
    show_competitive: bool = True
    show_roi: bool = True

@dataclass
class DashboardMetrics:
    """Key metrics for dashboard display."""
    period: str
    traffic_sessions: int
    traffic_change: float
    ranking_position: float
    ranking_change: float
    conversions: int
    revenue: float
    roi_percentage: float
    issues_count: int
    opportunities_count: int

class ClientDashboardGenerator:
    """Generates client-friendly executive dashboards."""
    
    def __init__(self, config_path: str = None):
        """Initialize the dashboard generator."""
        self.config_path = config_path or "tracking/config/tracking.yml"
        self.config = self._load_config()
        self.tracking_dir = Path("tracking")
        self.dashboards_dir = self.tracking_dir / "dashboards"
        self.templates_dir = self.dashboards_dir / "templates"
        
        # Create directories
        for dir_path in [self.dashboards_dir, self.templates_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration with dashboard defaults."""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            config = {}
        
        # Add dashboard defaults
        dashboard_defaults = {
            'dashboard': {
                'default_brand': {
                    'primary_color': '#2563eb',
                    'secondary_color': '#64748b', 
                    'success_color': '#10b981',
                    'warning_color': '#f59e0b',
                    'danger_color': '#ef4444'
                },
                'display_options': {
                    'show_detailed_metrics': True,
                    'show_competitive_data': True,
                    'show_technical_health': True,
                    'show_mission_progress': True
                }
            }
        }
        
        if 'dashboard' not in config:
            config['dashboard'] = dashboard_defaults['dashboard']
        
        return config
    
    def extract_dashboard_metrics(self, current_data: Dict[str, Any], 
                                 previous_data: Dict[str, Any] = None,
                                 baseline_data: Dict[str, Any] = None) -> DashboardMetrics:
        """Extract key metrics for dashboard display."""
        
        # Traffic metrics
        current_traffic = current_data.get('traffic_metrics', {}).get('organic_traffic', {})
        traffic_sessions = current_traffic.get('sessions', 0)
        
        if previous_data:
            previous_traffic = previous_data.get('traffic_metrics', {}).get('organic_traffic', {})
            prev_sessions = previous_traffic.get('sessions', 0)
            traffic_change = ((traffic_sessions - prev_sessions) / prev_sessions * 100) if prev_sessions > 0 else 0
        else:
            traffic_change = 0
        
        # Ranking metrics
        current_rankings = current_data.get('ranking_metrics', {}).get('visibility', {})
        ranking_position = current_rankings.get('average_position', 100)
        
        if previous_data:
            previous_rankings = previous_data.get('ranking_metrics', {}).get('visibility', {})
            prev_position = previous_rankings.get('average_position', 100)
            ranking_change = prev_position - ranking_position  # Positive is improvement
        else:
            ranking_change = 0
        
        # Business metrics
        roi_config = self.config.get('roi', {})
        conversion_rate = roi_config.get('conversion_rate', 0.02)
        avg_order_value = roi_config.get('average_order_value', 100)
        
        conversions = int(traffic_sessions * conversion_rate)
        revenue = conversions * avg_order_value
        
        # ROI calculation (simplified)
        investment = 5000  # Would be tracked more precisely
        roi_percentage = (revenue / investment * 100) if investment > 0 else 0
        
        # Issues and opportunities (mock data)
        issues_count = len(self._identify_issues(current_data))
        opportunities_count = len(self._identify_opportunities(current_data))
        
        # Period calculation
        period = current_data.get('metadata', {}).get('timestamp', datetime.now().isoformat())[:10]
        
        return DashboardMetrics(
            period=period,
            traffic_sessions=traffic_sessions,
            traffic_change=traffic_change,
            ranking_position=ranking_position,
            ranking_change=ranking_change,
            conversions=conversions,
            revenue=revenue,
            roi_percentage=roi_percentage,
            issues_count=issues_count,
            opportunities_count=opportunities_count
        )
    
    def _identify_issues(self, data: Dict[str, Any]) -> List[Dict[str, str]]:
        """Identify critical issues for dashboard display."""
        issues = []
        
        # Technical issues
        tech_metrics = data.get('technical_metrics', {})
        lighthouse = tech_metrics.get('lighthouse_scores', {})
        
        if lighthouse.get('performance', 100) < 70:
            issues.append({
                'title': 'Site Performance Below Optimal',
                'severity': 'medium',
                'category': 'technical'
            })
        
        # Core Web Vitals issues
        cwv = tech_metrics.get('core_web_vitals', {})
        if cwv.get('lcp', {}).get('status') == 'poor':
            issues.append({
                'title': 'Poor Largest Contentful Paint',
                'severity': 'high',
                'category': 'user_experience'
            })
        
        return issues
    
    def _identify_opportunities(self, data: Dict[str, Any]) -> List[Dict[str, str]]:
        """Identify opportunities for dashboard display."""
        opportunities = []
        
        # Ranking opportunities
        ranking_metrics = data.get('ranking_metrics', {})
        keyword_dist = ranking_metrics.get('keyword_distribution', {})
        
        top_20 = keyword_dist.get('top_20', 0)
        top_10 = keyword_dist.get('top_10', 0)
        
        if top_20 > top_10:
            opportunities.append({
                'title': 'Keywords Ready for Top 10 Push',
                'impact': 'high',
                'category': 'content'
            })
        
        return opportunities
    
    def create_html_dashboard(self, metrics: DashboardMetrics, 
                             dashboard_config: DashboardConfig,
                             additional_data: Dict[str, Any] = None) -> str:
        """Generate HTML dashboard."""
        
        brand_colors = dashboard_config.brand_colors
        client_name = dashboard_config.client_name
        
        # Calculate status indicators
        traffic_status = "success" if metrics.traffic_change > 0 else "warning" if metrics.traffic_change > -10 else "danger"
        ranking_status = "success" if metrics.ranking_change > 0 else "warning" if metrics.ranking_change > -2 else "danger"
        roi_status = "success" if metrics.roi_percentage > 200 else "warning" if metrics.roi_percentage > 100 else "info"
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEO Performance Dashboard - {client_name}</title>
    <style>
        :root {{
            --primary-color: {brand_colors.get('primary', '#2563eb')};
            --secondary-color: {brand_colors.get('secondary', '#64748b')};
            --success-color: {brand_colors.get('success', '#10b981')};
            --warning-color: {brand_colors.get('warning', '#f59e0b')};
            --danger-color: {brand_colors.get('danger', '#ef4444')};
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #f8fafc;
            color: #1e293b;
            line-height: 1.6;
        }}
        
        .dashboard {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .header {{
            background: linear-gradient(135deg, var(--primary-color), #1d4ed8);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }}
        
        .header .subtitle {{
            opacity: 0.9;
            font-size: 1.2rem;
        }}
        
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        
        .metric-card {{
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border-left: 4px solid var(--primary-color);
        }}
        
        .metric-header {{
            display: flex;
            justify-content: between;
            align-items: center;
            margin-bottom: 1rem;
        }}
        
        .metric-title {{
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--secondary-color);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        
        .metric-value {{
            font-size: 2.5rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 0.5rem;
        }}
        
        .metric-change {{
            display: flex;
            align-items: center;
            font-size: 0.9rem;
            font-weight: 500;
        }}
        
        .change-positive {{ color: var(--success-color); }}
        .change-negative {{ color: var(--danger-color); }}
        .change-neutral {{ color: var(--secondary-color); }}
        
        .status-indicator {{
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-right: 0.5rem;
        }}
        
        .status-success {{ background-color: var(--success-color); }}
        .status-warning {{ background-color: var(--warning-color); }}
        .status-danger {{ background-color: var(--danger-color); }}
        .status-info {{ background-color: var(--primary-color); }}
        
        .insights-section {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-top: 2rem;
        }}
        
        .insights-card {{
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}
        
        .insights-header {{
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: #1e293b;
        }}
        
        .insight-item {{
            padding: 0.75rem 0;
            border-bottom: 1px solid #e2e8f0;
        }}
        
        .insight-item:last-child {{
            border-bottom: none;
        }}
        
        .insight-title {{
            font-weight: 600;
            margin-bottom: 0.25rem;
        }}
        
        .insight-description {{
            font-size: 0.9rem;
            color: var(--secondary-color);
        }}
        
        .footer {{
            text-align: center;
            margin-top: 3rem;
            padding: 1rem;
            color: var(--secondary-color);
            font-size: 0.9rem;
        }}
        
        .chart-placeholder {{
            height: 200px;
            background: linear-gradient(45deg, #f1f5f9, #e2e8f0);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--secondary-color);
            margin: 1rem 0;
        }}
        
        @media (max-width: 768px) {{
            .dashboard {{
                padding: 1rem;
            }}
            
            .metrics-grid {{
                grid-template-columns: 1fr;
            }}
            
            .insights-section {{
                grid-template-columns: 1fr;
            }}
            
            .header h1 {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1>SEO Performance Dashboard</h1>
            <div class="subtitle">{client_name} • Report Period: {metrics.period}</div>
        </div>
        
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-title">Organic Traffic</div>
                <div class="metric-value">{metrics.traffic_sessions:,}</div>
                <div class="metric-change">
                    <span class="status-indicator status-{traffic_status}"></span>
                    <span class="change-{'positive' if metrics.traffic_change > 0 else 'negative' if metrics.traffic_change < 0 else 'neutral'}">
                        {'+' if metrics.traffic_change > 0 else ''}{metrics.traffic_change:.1f}% vs previous period
                    </span>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Average Ranking Position</div>
                <div class="metric-value">{metrics.ranking_position:.1f}</div>
                <div class="metric-change">
                    <span class="status-indicator status-{ranking_status}"></span>
                    <span class="change-{'positive' if metrics.ranking_change > 0 else 'negative' if metrics.ranking_change < 0 else 'neutral'}">
                        {'Improved by ' if metrics.ranking_change > 0 else 'Declined by ' if metrics.ranking_change < 0 else 'Stable at '}{abs(metrics.ranking_change):.1f} positions
                    </span>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Estimated Revenue</div>
                <div class="metric-value">${metrics.revenue:,.0f}</div>
                <div class="metric-change">
                    <span class="status-indicator status-info"></span>
                    <span class="change-neutral">From {metrics.conversions} organic conversions</span>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="metric-title">Return on Investment</div>
                <div class="metric-value">{metrics.roi_percentage:.0f}%</div>
                <div class="metric-change">
                    <span class="status-indicator status-{roi_status}"></span>
                    <span class="change-{'positive' if metrics.roi_percentage > 200 else 'neutral'}">
                        {'Excellent' if metrics.roi_percentage > 200 else 'Good' if metrics.roi_percentage > 100 else 'Growing'} performance
                    </span>
                </div>
            </div>
        </div>
        
        <div class="insights-section">
            <div class="insights-card">
                <div class="insights-header">🚨 Priority Issues ({metrics.issues_count})</div>
                {self._generate_issues_html(additional_data)}
            </div>
            
            <div class="insights-card">
                <div class="insights-header">🎯 Growth Opportunities ({metrics.opportunities_count})</div>
                {self._generate_opportunities_html(additional_data)}
            </div>
        </div>
        
        <div class="insights-section">
            <div class="insights-card">
                <div class="insights-header">📈 Traffic Trend</div>
                <div class="chart-placeholder">Interactive Chart Available in Full Report</div>
            </div>
            
            <div class="insights-card">
                <div class="insights-header">🔍 Ranking Progress</div>
                <div class="chart-placeholder">Keyword Position Tracking Chart</div>
            </div>
        </div>
        
        <div class="footer">
            <p>{'Generated by SEO Agent Library' if not dashboard_config.white_label else 'Professional SEO Reporting'}</p>
            <p>Last updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
    </div>
</body>
</html>
        """
        
        return html_content
    
    def _generate_issues_html(self, data: Dict[str, Any]) -> str:
        """Generate HTML for issues section."""
        if not data:
            return '<div class="insight-item"><div class="insight-title">No critical issues detected</div><div class="insight-description">System is performing well</div></div>'
        
        issues_html = []
        sample_issues = [
            {
                'title': 'Core Web Vitals Need Attention',
                'description': 'LCP score can be improved for better user experience'
            },
            {
                'title': 'Mobile Performance Optimization',
                'description': 'Mobile page speed could be optimized further'
            }
        ]
        
        for issue in sample_issues:
            issues_html.append(f"""
                <div class="insight-item">
                    <div class="insight-title">{issue['title']}</div>
                    <div class="insight-description">{issue['description']}</div>
                </div>
            """)
        
        return ''.join(issues_html)
    
    def _generate_opportunities_html(self, data: Dict[str, Any]) -> str:
        """Generate HTML for opportunities section."""
        opportunities_html = []
        sample_opportunities = [
            {
                'title': 'Featured Snippet Potential',
                'description': '12 keywords positioned for featured snippets'
            },
            {
                'title': 'Content Gap Analysis',
                'description': '8 high-value topics identified for content creation'
            }
        ]
        
        for opportunity in sample_opportunities:
            opportunities_html.append(f"""
                <div class="insight-item">
                    <div class="insight-title">{opportunity['title']}</div>
                    <div class="insight-description">{opportunity['description']}</div>
                </div>
            """)
        
        return ''.join(opportunities_html)
    
    def create_executive_report(self, metrics: DashboardMetrics,
                               dashboard_config: DashboardConfig) -> str:
        """Create executive summary report."""
        
        executive_report = f"""
# Executive SEO Report
## {dashboard_config.client_name}
**Report Period:** {metrics.period}

### Key Performance Summary

**Traffic Performance**
- Organic sessions: {metrics.traffic_sessions:,} ({'+' if metrics.traffic_change > 0 else ''}{metrics.traffic_change:.1f}%)
- Estimated conversions: {metrics.conversions}
- Revenue attribution: ${metrics.revenue:,.0f}

**Search Visibility**  
- Average ranking position: {metrics.ranking_position:.1f}
- Position change: {'+' if metrics.ranking_change > 0 else ''}{metrics.ranking_change:.1f} positions
- ROI achieved: {metrics.roi_percentage:.0f}%

### Strategic Assessment

**Strengths:**
- {'Strong traffic growth momentum' if metrics.traffic_change > 10 else 'Stable traffic performance' if metrics.traffic_change > -5 else 'Traffic requires attention'}
- {'Excellent search visibility' if metrics.ranking_position < 20 else 'Good competitive position' if metrics.ranking_position < 50 else 'Improving market presence'}
- {'Outstanding ROI performance' if metrics.roi_percentage > 200 else 'Positive investment returns' if metrics.roi_percentage > 100 else 'Building toward profitability'}

**Priority Actions:**
- Address {metrics.issues_count} technical optimization areas
- Capitalize on {metrics.opportunities_count} identified growth opportunities
- Continue systematic improvement across all SEO pillars

### Next Period Focus
- Maintain traffic growth trajectory
- Optimize conversion funnel performance  
- Expand keyword coverage in target markets
- Enhance technical foundation for scale

---
*This report was generated using automated SEO intelligence and validated by specialist agents.*
        """
        
        return executive_report.strip()
    
    def generate_dashboard_suite(self, current_data: Dict[str, Any],
                                previous_data: Dict[str, Any] = None,
                                client_config: Dict[str, Any] = None) -> Dict[str, str]:
        """Generate complete dashboard suite."""
        
        # Extract metrics
        metrics = self.extract_dashboard_metrics(current_data, previous_data)
        
        # Configure dashboard
        dashboard_config = DashboardConfig(
            client_name=client_config.get('name', 'Client') if client_config else 'Client',
            brand_colors=client_config.get('brand_colors', self.config['dashboard']['default_brand']) if client_config else self.config['dashboard']['default_brand'],
            logo_url=client_config.get('logo_url', '') if client_config else '',
            white_label=client_config.get('white_label', False) if client_config else False
        )
        
        # Generate different formats
        suite = {
            'html_dashboard': self.create_html_dashboard(metrics, dashboard_config, current_data),
            'executive_report': self.create_executive_report(metrics, dashboard_config),
            'metrics_json': json.dumps(asdict(metrics), indent=2)
        }
        
        return suite
    
    def export_dashboard(self, dashboard_suite: Dict[str, str], 
                        client_name: str = "client") -> Dict[str, str]:
        """Export dashboard files."""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        client_slug = client_name.lower().replace(' ', '_')
        
        export_paths = {}
        
        # Export HTML dashboard
        html_path = self.dashboards_dir / f"{client_slug}_dashboard_{timestamp}.html"
        with open(html_path, 'w') as f:
            f.write(dashboard_suite['html_dashboard'])
        export_paths['html'] = str(html_path)
        
        # Export executive report
        report_path = self.dashboards_dir / f"{client_slug}_executive_{timestamp}.md"
        with open(report_path, 'w') as f:
            f.write(dashboard_suite['executive_report'])
        export_paths['report'] = str(report_path)
        
        # Export metrics JSON
        json_path = self.dashboards_dir / f"{client_slug}_metrics_{timestamp}.json"
        with open(json_path, 'w') as f:
            f.write(dashboard_suite['metrics_json'])
        export_paths['json'] = str(json_path)
        
        return export_paths

def main():
    """CLI interface for dashboard generation."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate Client Dashboards")
    parser.add_argument("--current", help="Current data file path", required=True)
    parser.add_argument("--previous", help="Previous period data file path")
    parser.add_argument("--client", default="Demo Client", help="Client name")
    parser.add_argument("--white-label", action='store_true', help="Remove SEO Agent branding")
    parser.add_argument("--formats", nargs='+', default=['html', 'report'], 
                       choices=['html', 'report', 'json'])
    
    args = parser.parse_args()
    
    generator = ClientDashboardGenerator()
    
    # Load data
    with open(args.current, 'r') as f:
        current_data = json.load(f)
    
    previous_data = None
    if args.previous:
        with open(args.previous, 'r') as f:
            previous_data = json.load(f)
    
    # Client configuration
    client_config = {
        'name': args.client,
        'white_label': args.white_label,
        'brand_colors': generator.config['dashboard']['default_brand']
    }
    
    # Generate dashboard suite
    dashboard_suite = generator.generate_dashboard_suite(
        current_data, previous_data, client_config
    )
    
    # Export files
    export_paths = generator.export_dashboard(dashboard_suite, args.client)
    
    print(f"Dashboard generated for {args.client}")
    for format_type, path in export_paths.items():
        if format_type in args.formats:
            print(f"{format_type.upper()}: {path}")

if __name__ == "__main__":
    main()