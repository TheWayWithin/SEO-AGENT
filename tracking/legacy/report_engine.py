#!/usr/bin/env python3
"""
SEO Agent Library - Report Generation Engine
Processes tracking data into actionable insights and business reports.
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
class MetricChange:
    """Represents a metric change with percentage and trend."""
    previous: Union[int, float]
    current: Union[int, float]
    change_percent: float
    change_absolute: Union[int, float]
    trend: str  # 'up', 'down', 'stable'
    status: str  # 'good', 'warning', 'critical'

class ReportEngine:
    """Core report generation engine for SEO Agent Library."""
    
    def __init__(self, config_path: str = None):
        """Initialize the report engine with configuration."""
        self.config_path = config_path or "tracking/config/tracking.yml"
        self.config = self._load_config()
        self.tracking_dir = Path("tracking")
        self.snapshots_dir = self.tracking_dir / "snapshots"
        self.reports_dir = self.tracking_dir / "reports"
        self.templates_dir = self.tracking_dir / "templates"
        
        # Create directories if they don't exist
        for dir_path in [self.reports_dir / "automated", 
                        self.reports_dir / "executive", 
                        self.reports_dir / "case-studies"]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self) -> Dict[str, Any]:
        """Load tracking configuration."""
        try:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            # Return default config if file doesn't exist
            return {
                'domain': 'example.com',
                'roi': {
                    'organic_session_value': 2.50,
                    'conversion_rate': 0.02,
                    'average_order_value': 100,
                    'seo_hourly_rate': 150
                },
                'alerts': {
                    'traffic_drop': -15,
                    'ranking_drop': 3,
                    'core_web_vitals': 90,
                    'crawl_errors': 10
                }
            }
    
    def calculate_change(self, previous: Union[int, float], 
                        current: Union[int, float], 
                        reverse_trend: bool = False) -> MetricChange:
        """Calculate metric change with trend and status."""
        if previous == 0:
            change_percent = 100.0 if current > 0 else 0.0
            change_absolute = current
        else:
            change_percent = ((current - previous) / previous) * 100
            change_absolute = current - previous
        
        # Determine trend
        if abs(change_percent) < 2:
            trend = 'stable'
        elif change_percent > 0:
            trend = 'down' if reverse_trend else 'up'
        else:
            trend = 'up' if reverse_trend else 'down'
        
        # Determine status
        if abs(change_percent) < 5:
            status = 'good'
        elif abs(change_percent) < 15:
            status = 'warning'
        else:
            status = 'critical'
        
        return MetricChange(
            previous=previous,
            current=current,
            change_percent=change_percent,
            change_absolute=change_absolute,
            trend=trend,
            status=status
        )
    
    def load_snapshot_data(self, filepath: str) -> Optional[Dict[str, Any]]:
        """Load data from a snapshot file."""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading snapshot {filepath}: {e}")
            return None
    
    def get_latest_snapshot(self, snapshot_type: str = "weekly") -> Optional[Dict[str, Any]]:
        """Get the most recent snapshot of specified type."""
        snapshot_dir = self.snapshots_dir / snapshot_type
        if not snapshot_dir.exists():
            return None
        
        snapshot_files = list(snapshot_dir.glob("*.json"))
        if not snapshot_files:
            return None
        
        latest_file = max(snapshot_files, key=lambda f: f.stat().st_mtime)
        return self.load_snapshot_data(str(latest_file))
    
    def get_baseline_data(self) -> Optional[Dict[str, Any]]:
        """Get baseline data for comparison."""
        baseline_dir = self.tracking_dir / "baselines"
        if not baseline_dir.exists():
            return None
        
        baseline_files = list(baseline_dir.glob("*.json"))
        if not baseline_files:
            return None
        
        # Use the most recent baseline
        latest_baseline = max(baseline_files, key=lambda f: f.stat().st_mtime)
        return self.load_snapshot_data(str(latest_baseline))
    
    def get_snapshot_series(self, snapshot_type: str = "weekly", 
                           count: int = 8) -> List[Dict[str, Any]]:
        """Get a series of snapshots for trend analysis."""
        snapshot_dir = self.snapshots_dir / snapshot_type
        if not snapshot_dir.exists():
            return []
        
        snapshot_files = sorted(
            snapshot_dir.glob("*.json"),
            key=lambda f: f.stat().st_mtime,
            reverse=True
        )
        
        snapshots = []
        for file_path in snapshot_files[:count]:
            data = self.load_snapshot_data(str(file_path))
            if data:
                snapshots.append(data)
        
        return list(reversed(snapshots))  # Return chronological order
    
    def calculate_roi_metrics(self, current_data: Dict[str, Any], 
                             baseline_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate ROI and business impact metrics."""
        roi_config = self.config.get('roi', {})
        session_value = roi_config.get('organic_session_value', 2.50)
        conversion_rate = roi_config.get('conversion_rate', 0.02)
        avg_order_value = roi_config.get('average_order_value', 100)
        hourly_rate = roi_config.get('seo_hourly_rate', 150)
        
        # Extract traffic metrics
        current_traffic = current_data.get('traffic_metrics', {}).get('organic_traffic', {})
        baseline_traffic = baseline_data.get('traffic_metrics', {}).get('organic_traffic', {})
        
        current_sessions = current_traffic.get('sessions', 0)
        baseline_sessions = baseline_traffic.get('sessions', 0)
        
        # Calculate traffic value
        session_increase = current_sessions - baseline_sessions
        traffic_value = session_increase * session_value
        
        # Calculate conversion impact
        conversions = current_sessions * conversion_rate
        revenue_impact = conversions * avg_order_value
        
        # Calculate time savings (estimate based on automation)
        hours_saved = 10  # Placeholder - could be calculated from mission data
        cost_savings = hours_saved * hourly_rate
        
        return {
            'traffic_value': traffic_value,
            'session_increase': session_increase,
            'conversions': conversions,
            'revenue_impact': revenue_impact,
            'cost_savings': cost_savings,
            'hours_saved': hours_saved,
            'total_value': traffic_value + revenue_impact + cost_savings
        }
    
    def detect_issues_and_opportunities(self, data: Dict[str, Any], 
                                       previous_data: Dict[str, Any] = None) -> Dict[str, List[Dict[str, Any]]]:
        """Detect critical issues and opportunities from data analysis."""
        issues = []
        opportunities = []
        
        # Technical health checks
        tech_metrics = data.get('technical_metrics', {})
        cwv = tech_metrics.get('core_web_vitals', {})
        lighthouse = tech_metrics.get('lighthouse_scores', {})
        
        # Core Web Vitals issues
        if cwv.get('lcp', {}).get('status') == 'poor':
            issues.append({
                'title': 'Poor Largest Contentful Paint',
                'severity': 'high',
                'impact': 'User experience and search rankings',
                'action': 'Optimize image loading and server response times',
                'owner': '@seo-technical'
            })
        
        # Performance issues
        perf_score = lighthouse.get('performance', 100)
        if perf_score < self.config.get('alerts', {}).get('core_web_vitals', 90):
            issues.append({
                'title': f'Low Performance Score ({perf_score}/100)',
                'severity': 'medium',
                'impact': 'Search rankings and user experience',
                'action': 'Run performance audit and optimize critical rendering path',
                'owner': '@seo-technical'
            })
        
        # Traffic trend analysis
        if previous_data:
            current_traffic = data.get('traffic_metrics', {}).get('organic_traffic', {})
            previous_traffic = previous_data.get('traffic_metrics', {}).get('organic_traffic', {})
            
            traffic_change = self.calculate_change(
                previous_traffic.get('sessions', 0),
                current_traffic.get('sessions', 0)
            )
            
            if traffic_change.change_percent < self.config.get('alerts', {}).get('traffic_drop', -15):
                issues.append({
                    'title': f'Significant Traffic Drop ({traffic_change.change_percent:.1f}%)',
                    'severity': 'critical',
                    'impact': 'Business revenue and lead generation',
                    'action': 'Investigate ranking drops and technical issues',
                    'owner': '@seo-analyst'
                })
        
        # Ranking opportunities
        ranking_metrics = data.get('ranking_metrics', {})
        keyword_dist = ranking_metrics.get('keyword_distribution', {})
        
        top_20_keywords = keyword_dist.get('top_20', 0)
        top_10_keywords = keyword_dist.get('top_10', 0)
        
        if top_20_keywords > top_10_keywords * 2:
            opportunities.append({
                'opportunity': 'Keywords Ready for Top 10 Push',
                'description': f'{top_20_keywords - top_10_keywords} keywords ranking 11-20 could be optimized',
                'impact': 'High - significant traffic increase potential',
                'effort': 'Medium - content optimization and link building'
            })
        
        return {'issues': issues, 'opportunities': opportunities}
    
    def generate_trend_analysis(self, snapshots: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate trend analysis from snapshot series."""
        if len(snapshots) < 2:
            return {}
        
        # Extract time series data
        sessions_data = []
        rankings_data = []
        performance_data = []
        
        for snapshot in snapshots:
            # Traffic data
            traffic = snapshot.get('traffic_metrics', {}).get('organic_traffic', {})
            sessions_data.append(traffic.get('sessions', 0))
            
            # Ranking data
            rankings = snapshot.get('ranking_metrics', {}).get('visibility', {})
            rankings_data.append(rankings.get('average_position', 100))
            
            # Performance data
            tech = snapshot.get('technical_metrics', {}).get('lighthouse_scores', {})
            performance_data.append(tech.get('performance', 50))
        
        # Calculate trends
        def calculate_trend(data_series):
            if len(data_series) < 2:
                return 'stable'
            
            # Simple linear regression slope
            n = len(data_series)
            x = list(range(n))
            y = data_series
            
            sum_x = sum(x)
            sum_y = sum(y)
            sum_xy = sum(x[i] * y[i] for i in range(n))
            sum_x2 = sum(x[i] ** 2 for i in range(n))
            
            if n * sum_x2 - sum_x ** 2 == 0:
                return 'stable'
                
            slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
            
            if abs(slope) < 0.1:
                return 'stable'
            elif slope > 0:
                return 'improving'
            else:
                return 'declining'
        
        return {
            'sessions_trend': calculate_trend(sessions_data),
            'rankings_trend': calculate_trend(rankings_data),
            'performance_trend': calculate_trend(performance_data),
            'data_points': len(snapshots)
        }
    
    def format_number(self, value: Union[int, float], format_type: str = 'default') -> str:
        """Format numbers for display in reports."""
        if format_type == 'currency':
            return f"${value:,.2f}"
        elif format_type == 'percentage':
            return f"{value:.1f}%"
        elif format_type == 'integer':
            return f"{int(value):,}"
        elif format_type == 'decimal':
            return f"{value:.2f}"
        else:
            if isinstance(value, int):
                return f"{value:,}"
            else:
                return f"{value:.2f}"
    
    def generate_ascii_chart(self, data: List[Union[int, float]], 
                           width: int = 40, height: int = 8) -> str:
        """Generate simple ASCII chart for trend visualization."""
        if not data or len(data) < 2:
            return "Insufficient data for chart"
        
        min_val = min(data)
        max_val = max(data)
        
        if max_val == min_val:
            return "█" * width  # Flat line
        
        # Normalize data to chart height
        normalized = []
        for val in data:
            norm = int(((val - min_val) / (max_val - min_val)) * (height - 1))
            normalized.append(norm)
        
        # Create chart
        chart_lines = []
        for row in range(height - 1, -1, -1):
            line = ""
            for col in range(len(normalized)):
                if normalized[col] >= row:
                    line += "█"
                else:
                    line += " "
            chart_lines.append(line)
        
        return "\n".join(chart_lines)
    
    def create_executive_summary(self, current_data: Dict[str, Any], 
                                baseline_data: Dict[str, Any], 
                                previous_data: Dict[str, Any] = None) -> str:
        """Generate executive summary text."""
        roi_metrics = self.calculate_roi_metrics(current_data, baseline_data)
        
        # Calculate key changes
        current_traffic = current_data.get('traffic_metrics', {}).get('organic_traffic', {})
        baseline_traffic = baseline_data.get('traffic_metrics', {}).get('organic_traffic', {})
        
        traffic_change = self.calculate_change(
            baseline_traffic.get('sessions', 0),
            current_traffic.get('sessions', 0)
        )
        
        summary_parts = []
        
        # Traffic summary
        if traffic_change.trend == 'up':
            summary_parts.append(
                f"Organic traffic increased by {traffic_change.change_percent:.1f}% "
                f"({traffic_change.change_absolute:,} additional sessions)"
            )
        elif traffic_change.trend == 'down':
            summary_parts.append(
                f"Organic traffic declined by {abs(traffic_change.change_percent):.1f}% "
                f"({abs(traffic_change.change_absolute):,} fewer sessions)"
            )
        else:
            summary_parts.append("Organic traffic remained stable with minimal fluctuation")
        
        # ROI summary
        if roi_metrics['total_value'] > 0:
            summary_parts.append(
                f"SEO initiatives generated ${roi_metrics['total_value']:,.2f} in estimated value "
                f"through improved traffic and operational efficiency"
            )
        
        # Technical health
        tech_metrics = current_data.get('technical_metrics', {})
        lighthouse = tech_metrics.get('lighthouse_scores', {})
        perf_score = lighthouse.get('performance', 50)
        
        if perf_score >= 90:
            summary_parts.append("Site maintains excellent technical performance")
        elif perf_score >= 70:
            summary_parts.append("Site technical performance is good with room for optimization")
        else:
            summary_parts.append("Site technical performance requires immediate attention")
        
        return ". ".join(summary_parts) + "."

def main():
    """CLI interface for report generation."""
    import argparse
    
    parser = argparse.ArgumentParser(description="SEO Agent Report Generator")
    parser.add_argument("--type", choices=["weekly", "monthly", "comparison", "roi"], 
                       default="weekly", help="Report type to generate")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--format", choices=["markdown", "json", "html"], 
                       default="markdown", help="Output format")
    
    args = parser.parse_args()
    
    engine = ReportEngine()
    print(f"Generating {args.type} report in {args.format} format...")
    
    # Basic functionality - would be extended by specific report generators
    if args.type == "weekly":
        current = engine.get_latest_snapshot("weekly")
        baseline = engine.get_baseline_data()
        
        if current and baseline:
            roi_metrics = engine.calculate_roi_metrics(current, baseline)
            summary = engine.create_executive_summary(current, baseline)
            
            print(f"Executive Summary: {summary}")
            print(f"ROI Metrics: ${roi_metrics['total_value']:,.2f} total value generated")
        else:
            print("Insufficient data for report generation")

if __name__ == "__main__":
    main()