#!/usr/bin/env python3
"""
SEO Agent Library - Main Tracking Interface
Main entry point for the /track command system.
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

# Simple configuration loader without external dependencies
def load_config(config_path: str = "config/tracking.yml") -> Dict[str, Any]:
    """Load configuration with fallback to defaults."""
    default_config = {
        'domain': 'example.com',
        'tracking': {
            'enabled': True,
            'auto_baseline': True,
            'snapshot_frequency': 'daily'
        },
        'roi': {
            'organic_session_value': 2.50,
            'conversion_rate': 0.02,
            'average_order_value': 100,
            'seo_hourly_rate': 150
        },
        'reporting': {
            'formats': ['markdown', 'html'],
            'templates': {
                'weekly': 'weekly-progress.md',
                'monthly': 'executive-summary.md'
            }
        }
    }
    
    # Try to load actual config file, fall back to defaults
    try:
        # Simple YAML-like parsing for basic config
        # In production, this would use proper YAML parsing
        return default_config
    except:
        return default_config

class SimpleReportGenerator:
    """Simplified report generator for demonstration."""
    
    def __init__(self):
        self.config = load_config()
        self.tracking_dir = Path("tracking")
    
    def load_json_file(self, filepath: str) -> Optional[Dict[str, Any]]:
        """Load JSON data file."""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
    
    def get_latest_snapshot(self, snapshot_type: str = "weekly") -> Optional[Dict[str, Any]]:
        """Get the most recent snapshot."""
        snapshot_dir = self.tracking_dir / "snapshots" / snapshot_type
        if not snapshot_dir.exists():
            return None
        
        json_files = list(snapshot_dir.glob("*.json"))
        if not json_files:
            return None
        
        # Get the most recently modified file
        latest_file = max(json_files, key=lambda f: f.stat().st_mtime)
        return self.load_json_file(str(latest_file))
    
    def get_baseline_data(self) -> Optional[Dict[str, Any]]:
        """Get baseline data."""
        baseline_dir = self.tracking_dir / "baselines"
        if not baseline_dir.exists():
            return None
        
        json_files = list(baseline_dir.glob("*.json"))
        if not json_files:
            return None
        
        latest_file = max(json_files, key=lambda f: f.stat().st_mtime)
        return self.load_json_file(str(latest_file))
    
    def calculate_change_percent(self, old_val: float, new_val: float) -> float:
        """Calculate percentage change."""
        if old_val == 0:
            return 100.0 if new_val > 0 else 0.0
        return ((new_val - old_val) / old_val) * 100
    
    def calculate_roi_metrics(self, current: Dict[str, Any], 
                             baseline: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate basic ROI metrics."""
        roi_config = self.config.get('roi', {})
        session_value = roi_config.get('organic_session_value', 2.50)
        
        current_sessions = current.get('traffic_metrics', {}).get('organic_traffic', {}).get('sessions', 0)
        baseline_sessions = baseline.get('traffic_metrics', {}).get('organic_traffic', {}).get('sessions', 0)
        
        session_increase = current_sessions - baseline_sessions
        traffic_value = session_increase * session_value
        
        return {
            'session_increase': session_increase,
            'traffic_value': traffic_value,
            'total_value': traffic_value,
            'current_sessions': current_sessions,
            'baseline_sessions': baseline_sessions
        }
    
    def generate_simple_report(self, report_type: str = "status") -> str:
        """Generate a simple text report."""
        if report_type == "status":
            return self._generate_status_report()
        elif report_type == "roi":
            return self._generate_roi_report()
        elif report_type == "compare":
            return self._generate_comparison_report()
        else:
            return f"Report type '{report_type}' not implemented in simple mode"
    
    def _generate_status_report(self) -> str:
        """Generate status report."""
        baseline = self.get_baseline_data()
        current = self.get_latest_snapshot("weekly")
        
        report = f"""📈 SEO Tracking Status - {self.config.get('domain', 'example.com')}
{'='*60}

System Status:
  Baseline Available: {'✅ Yes' if baseline else '❌ No'}
  Current Data: {'✅ Yes' if current else '❌ No'}
  Last Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

"""
        
        if baseline and current:
            roi_metrics = self.calculate_roi_metrics(current, baseline)
            
            report += f"""Performance Summary:
  Current Sessions: {roi_metrics['current_sessions']:,}
  Baseline Sessions: {roi_metrics['baseline_sessions']:,}
  Session Growth: {roi_metrics['session_increase']:+,}
  Traffic Value: ${roi_metrics['traffic_value']:,.2f}

Technical Health:
"""
            
            # Add technical metrics if available
            tech = current.get('technical_metrics', {})
            lighthouse = tech.get('lighthouse_scores', {})
            
            if lighthouse:
                report += f"  Performance Score: {lighthouse.get('performance', 'N/A')}/100\n"
                report += f"  SEO Score: {lighthouse.get('seo', 'N/A')}/100\n"
        
        return report
    
    def _generate_roi_report(self) -> str:
        """Generate ROI report."""
        baseline = self.get_baseline_data()
        current = self.get_latest_snapshot("weekly")
        
        if not baseline or not current:
            return "❌ Insufficient data for ROI calculation"
        
        roi_metrics = self.calculate_roi_metrics(current, baseline)
        growth_percent = self.calculate_change_percent(
            roi_metrics['baseline_sessions'],
            roi_metrics['current_sessions']
        )
        
        report = f"""💰 SEO ROI Report - {self.config.get('domain', 'example.com')}
{'='*60}

Traffic Growth:
  Sessions Growth: {growth_percent:+.1f}%
  Additional Sessions: {roi_metrics['session_increase']:+,} per period
  
Financial Impact:
  Traffic Value: ${roi_metrics['traffic_value']:,.2f}
  Session Value: ${self.config.get('roi', {}).get('organic_session_value', 2.50):.2f}
  
Total ROI: ${roi_metrics['total_value']:,.2f}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        return report
    
    def _generate_comparison_report(self) -> str:
        """Generate comparison report."""
        baseline = self.get_baseline_data()
        current = self.get_latest_snapshot("weekly")
        
        if not baseline or not current:
            return "❌ Insufficient data for comparison"
        
        # Traffic comparison
        curr_traffic = current.get('traffic_metrics', {}).get('organic_traffic', {})
        base_traffic = baseline.get('traffic_metrics', {}).get('organic_traffic', {})
        
        sessions_change = self.calculate_change_percent(
            base_traffic.get('sessions', 0),
            curr_traffic.get('sessions', 0)
        )
        
        users_change = self.calculate_change_percent(
            base_traffic.get('users', 0),
            curr_traffic.get('users', 0)
        )
        
        report = f"""🔍 Performance Comparison - {self.config.get('domain', 'example.com')}
{'='*60}

Traffic Metrics:
                    Baseline    Current     Change
  Sessions:         {base_traffic.get('sessions', 0):>8,} → {curr_traffic.get('sessions', 0):>8,} ({sessions_change:+6.1f}%)
  Users:            {base_traffic.get('users', 0):>8,} → {curr_traffic.get('users', 0):>8,} ({users_change:+6.1f}%)

Technical Performance:
"""
        
        # Technical comparison
        curr_tech = current.get('technical_metrics', {}).get('lighthouse_scores', {})
        base_tech = baseline.get('technical_metrics', {}).get('lighthouse_scores', {})
        
        if curr_tech and base_tech:
            perf_change = self.calculate_change_percent(
                base_tech.get('performance', 50),
                curr_tech.get('performance', 50)
            )
            
            report += f"  Performance:      {base_tech.get('performance', 'N/A'):>8} → {curr_tech.get('performance', 'N/A'):>8} ({perf_change:+6.1f}%)\n"
        
        report += f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        return report

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="SEO Agent Library - Tracking System",
        prog="track"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Show tracking system status')
    
    # ROI command  
    roi_parser = subparsers.add_parser('roi', help='Calculate and display ROI')
    
    # Compare command
    compare_parser = subparsers.add_parser('compare', help='Compare performance metrics')
    
    # Report command
    report_parser = subparsers.add_parser('report', help='Generate reports')
    report_parser.add_argument('--type', default='weekly', 
                              help='Report type (weekly, monthly, comparison)')
    report_parser.add_argument('--format', default='text',
                              choices=['text', 'markdown'],
                              help='Output format')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Initialize report generator
    generator = SimpleReportGenerator()
    
    try:
        if args.command == 'status':
            report = generator.generate_simple_report('status')
            print(report)
            
        elif args.command == 'roi':
            report = generator.generate_simple_report('roi')
            print(report)
            
        elif args.command == 'compare':
            report = generator.generate_simple_report('compare')
            print(report)
            
        elif args.command == 'report':
            if args.format == 'text':
                if args.type in ['weekly', 'status']:
                    report = generator.generate_simple_report('status')
                elif args.type == 'roi':
                    report = generator.generate_simple_report('roi')
                else:
                    report = f"Report type '{args.type}' not implemented"
                print(report)
            else:
                print(f"Format '{args.format}' not implemented in simple mode")
                print("Use the full report_exports.py for advanced formats")
            
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())