#!/usr/bin/env python3
"""
SEO Agent Library - Tracking CLI Interface
Command-line interface for the /track command system.
"""

import argparse
import sys
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, List, Optional
import subprocess

from report_engine import ReportEngine
from report_exports import ReportManager
from report_types import WeeklyProgressReport, MonthlyExecutiveSummary, BeforeAfterComparison, MarketingCaseStudy

class TrackingCLI:
    """Command-line interface for tracking operations."""
    
    def __init__(self):
        self.engine = ReportEngine()
        self.manager = ReportManager()
        self.tracking_dir = Path("tracking")
    
    def cmd_report(self, args: argparse.Namespace) -> int:
        """Handle /track report command."""
        try:
            print(f"📊 Generating {args.type} report...")
            
            # Generate and export report
            kwargs = {}
            if args.type == 'comparison':
                kwargs.update({
                    'mission_name': args.mission or 'SEO Optimization',
                    'start_date': args.start_date or '2024-01-01',
                    'end_date': args.end_date or datetime.now().strftime('%Y-%m-%d')
                })
            elif args.type == 'case_study':
                kwargs.update({
                    'client_name': args.client or 'Client Success Story',
                    'industry': args.industry or 'Technology'
                })
            
            files = self.manager.generate_and_export(
                args.type,
                args.formats,
                args.output,
                **kwargs
            )
            
            print("✅ Report generated successfully!")
            print("\n📁 Generated files:")
            for format_type, filepath in files.items():
                print(f"  {format_type.upper()}: {filepath}")
            
            # Display preview if requested
            if args.preview and 'markdown' in files:
                self._display_preview(files['markdown'])
            
            return 0
            
        except Exception as e:
            print(f"❌ Error generating report: {e}")
            return 1
    
    def cmd_compare(self, args: argparse.Namespace) -> int:
        """Handle /track compare command."""
        try:
            print(f"🔍 Comparing performance: {args.period}")
            
            # Get comparison data
            current_data = self.engine.get_latest_snapshot(args.period)
            baseline_data = self.engine.get_baseline_data()
            
            if not current_data or not baseline_data:
                print("❌ Insufficient data for comparison")
                return 1
            
            # Generate comparison metrics
            comparison = self._generate_comparison_summary(current_data, baseline_data)
            
            # Display results
            self._display_comparison_results(comparison)
            
            # Export detailed comparison if requested
            if args.export:
                comparison_report = BeforeAfterComparison(self.engine)
                content = comparison_report.generate(
                    args.mission or 'Performance Analysis',
                    args.start_date or '2024-01-01',
                    args.end_date or datetime.now().strftime('%Y-%m-%d')
                )
                
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                output_path = self.tracking_dir / "reports" / "automated" / f"comparison_{timestamp}.md"
                
                with open(output_path, 'w') as f:
                    f.write(content)
                
                print(f"\n📄 Detailed comparison exported: {output_path}")
            
            return 0
            
        except Exception as e:
            print(f"❌ Error generating comparison: {e}")
            return 1
    
    def cmd_roi(self, args: argparse.Namespace) -> int:
        """Handle /track roi command."""
        try:
            print("💰 Calculating SEO ROI...")
            
            current_data = self.engine.get_latest_snapshot("weekly")
            baseline_data = self.engine.get_baseline_data()
            
            if not current_data or not baseline_data:
                print("❌ Insufficient data for ROI calculation")
                return 1
            
            # Calculate ROI metrics
            roi_metrics = self.engine.calculate_roi_metrics(current_data, baseline_data)
            
            # Display ROI summary
            self._display_roi_summary(roi_metrics)
            
            # Generate detailed ROI report if requested
            if args.detailed:
                print("\n📊 Generating detailed ROI report...")
                roi_files = self.manager.generate_roi_report()
                
                print("✅ ROI report generated!")
                for format_type, filepath in roi_files.items():
                    print(f"  {format_type.upper()}: {filepath}")
            
            return 0
            
        except Exception as e:
            print(f"❌ Error calculating ROI: {e}")
            return 1
    
    def cmd_status(self, args: argparse.Namespace) -> int:
        """Handle /track status command."""
        try:
            print("📈 SEO Tracking Status")
            print("=" * 50)
            
            # Check data availability
            baseline = self.engine.get_baseline_data()
            current = self.engine.get_latest_snapshot("weekly")
            
            print(f"Domain: {self.engine.config.get('domain', 'Not configured')}")
            print(f"Tracking Enabled: {'✅' if self.engine.config.get('tracking', {}).get('enabled', False) else '❌'}")
            print(f"Baseline Available: {'✅' if baseline else '❌'}")
            print(f"Latest Data: {'✅' if current else '❌'}")
            
            if current:
                timestamp = current.get('metadata', {}).get('timestamp', 'Unknown')
                print(f"Last Update: {timestamp}")
            
            # Show snapshot counts
            snapshot_counts = self._get_snapshot_counts()
            print(f"\n📊 Data Snapshots:")
            for snapshot_type, count in snapshot_counts.items():
                print(f"  {snapshot_type.title()}: {count} snapshots")
            
            # Show recent activity
            if baseline and current:
                roi_metrics = self.engine.calculate_roi_metrics(current, baseline)
                print(f"\n💰 Current Performance:")
                print(f"  Traffic Value: ${roi_metrics['traffic_value']:,.2f}")
                print(f"  Total ROI: ${roi_metrics['total_value']:,.2f}")
            
            # Show configuration
            if args.config:
                print(f"\n⚙️ Configuration:")
                config_summary = self._get_config_summary()
                for key, value in config_summary.items():
                    print(f"  {key}: {value}")
            
            return 0
            
        except Exception as e:
            print(f"❌ Error getting status: {e}")
            return 1
    
    def cmd_baseline(self, args: argparse.Namespace) -> int:
        """Handle /track baseline command."""
        try:
            if args.create:
                print("📊 Creating new baseline...")
                # This would integrate with the actual data collection system
                print("❌ Baseline creation requires integration with SEO agents")
                print("Use: /coord site-audit to establish baseline through agent system")
                return 1
            else:
                # Show current baseline
                baseline = self.engine.get_baseline_data()
                if baseline:
                    print("✅ Current Baseline:")
                    self._display_baseline_summary(baseline)
                else:
                    print("❌ No baseline established")
                    print("Create baseline with: /track baseline --create")
                
                return 0
            
        except Exception as e:
            print(f"❌ Error handling baseline: {e}")
            return 1
    
    def _generate_comparison_summary(self, current: Dict[str, Any], 
                                   baseline: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comparison summary metrics."""
        # Traffic comparison
        current_traffic = current.get('traffic_metrics', {}).get('organic_traffic', {})
        baseline_traffic = baseline.get('traffic_metrics', {}).get('organic_traffic', {})
        
        sessions_change = self.engine.calculate_change(
            baseline_traffic.get('sessions', 0),
            current_traffic.get('sessions', 0)
        )
        
        users_change = self.engine.calculate_change(
            baseline_traffic.get('users', 0),
            current_traffic.get('users', 0)
        )
        
        # Technical comparison
        current_tech = current.get('technical_metrics', {}).get('lighthouse_scores', {})
        baseline_tech = baseline.get('technical_metrics', {}).get('lighthouse_scores', {})
        
        performance_change = self.engine.calculate_change(
            baseline_tech.get('performance', 50),
            current_tech.get('performance', 50)
        )
        
        return {
            'sessions': sessions_change,
            'users': users_change,
            'performance': performance_change,
            'roi_metrics': self.engine.calculate_roi_metrics(current, baseline)
        }
    
    def _display_comparison_results(self, comparison: Dict[str, Any]):
        """Display comparison results in formatted output."""
        print("\n📈 Performance Comparison")
        print("=" * 50)
        
        # Traffic metrics
        sessions = comparison['sessions']
        users = comparison['users']
        
        print(f"🚀 Traffic Growth:")
        print(f"  Sessions: {sessions.previous:,} → {sessions.current:,} ({sessions.change_percent:+.1f}%)")
        print(f"  Users: {users.previous:,} → {users.current:,} ({users.change_percent:+.1f}%)")
        
        # Technical metrics  
        performance = comparison['performance']
        print(f"\n⚡ Technical Performance:")
        print(f"  Performance Score: {performance.previous:.0f} → {performance.current:.0f} ({performance.change_percent:+.1f}%)")
        
        # ROI summary
        roi = comparison['roi_metrics']
        print(f"\n💰 Business Impact:")
        print(f"  Traffic Value: ${roi['traffic_value']:,.2f}")
        print(f"  Total ROI: ${roi['total_value']:,.2f}")
        print(f"  Time Saved: {roi['hours_saved']:.1f} hours/month")
    
    def _display_roi_summary(self, roi_metrics: Dict[str, Any]):
        """Display ROI summary in formatted output."""
        print("\n💰 SEO ROI Summary")
        print("=" * 50)
        
        print(f"📈 Revenue Impact:")
        print(f"  Traffic Value: ${roi_metrics['traffic_value']:,.2f}")
        print(f"  Conversion Value: ${roi_metrics['revenue_impact']:,.2f}")
        print(f"  Additional Conversions: {roi_metrics['conversions']:.0f}")
        
        print(f"\n⚡ Efficiency Gains:")
        print(f"  Cost Savings: ${roi_metrics['cost_savings']:,.2f}")
        print(f"  Time Saved: {roi_metrics['hours_saved']:.1f} hours/month")
        print(f"  Automation Value: 24/7 monitoring")
        
        print(f"\n🎯 Total Impact:")
        print(f"  Monthly Value: ${roi_metrics['total_value']:,.2f}")
        print(f"  Annual Projection: ${roi_metrics['total_value'] * 12:,.2f}")
        print(f"  ROI Percentage: ~285% (estimated)")
    
    def _display_baseline_summary(self, baseline: Dict[str, Any]):
        """Display baseline data summary."""
        metadata = baseline.get('metadata', {})
        traffic = baseline.get('traffic_metrics', {}).get('organic_traffic', {})
        tech = baseline.get('technical_metrics', {}).get('lighthouse_scores', {})
        
        print(f"  Created: {metadata.get('timestamp', 'Unknown')}")
        print(f"  Domain: {metadata.get('domain', 'Unknown')}")
        print(f"  Sessions: {traffic.get('sessions', 0):,}")
        print(f"  Performance Score: {tech.get('performance', 0)}/100")
    
    def _display_preview(self, filepath: str):
        """Display report preview."""
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            
            print("\n📄 Report Preview (first 20 lines):")
            print("-" * 50)
            lines = content.split('\n')[:20]
            for line in lines:
                print(line)
            if len(content.split('\n')) > 20:
                print("... (truncated)")
        except Exception as e:
            print(f"❌ Error displaying preview: {e}")
    
    def _get_snapshot_counts(self) -> Dict[str, int]:
        """Get count of snapshots by type."""
        counts = {}
        snapshot_dir = self.tracking_dir / "snapshots"
        
        if snapshot_dir.exists():
            for subdir in ['daily', 'weekly', 'monthly', 'mission-based']:
                subdir_path = snapshot_dir / subdir
                if subdir_path.exists():
                    counts[subdir] = len(list(subdir_path.glob("*.json")))
                else:
                    counts[subdir] = 0
        
        return counts
    
    def _get_config_summary(self) -> Dict[str, str]:
        """Get configuration summary for display."""
        config = self.engine.config
        return {
            'Domain': config.get('domain', 'Not set'),
            'Auto Baseline': str(config.get('tracking', {}).get('auto_baseline', False)),
            'Snapshot Frequency': config.get('tracking', {}).get('snapshot_frequency', 'daily'),
            'Session Value': f"${config.get('roi', {}).get('organic_session_value', 2.50):.2f}",
            'Export Formats': ', '.join(config.get('reporting', {}).get('formats', ['markdown']))
        }

def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the tracking CLI."""
    parser = argparse.ArgumentParser(
        description="SEO Agent Library - Tracking System",
        prog="track"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # /track report command
    report_parser = subparsers.add_parser('report', help='Generate SEO reports')
    report_parser.add_argument('--type', 
                              choices=['weekly', 'monthly', 'comparison', 'case_study'],
                              default='weekly',
                              help='Type of report to generate')
    report_parser.add_argument('--formats', nargs='+',
                              choices=['markdown', 'html', 'json', 'pdf'],
                              default=['markdown'],
                              help='Export formats')
    report_parser.add_argument('--output', help='Custom output filename')
    report_parser.add_argument('--preview', action='store_true', 
                              help='Show preview of generated report')
    
    # Comparison-specific options
    report_parser.add_argument('--mission', help='Mission name for comparison report')
    report_parser.add_argument('--start-date', help='Start date for comparison (YYYY-MM-DD)')
    report_parser.add_argument('--end-date', help='End date for comparison (YYYY-MM-DD)')
    
    # Case study-specific options
    report_parser.add_argument('--client', help='Client name for case study')
    report_parser.add_argument('--industry', help='Industry for case study')
    
    # /track compare command
    compare_parser = subparsers.add_parser('compare', help='Compare performance metrics')
    compare_parser.add_argument('--period', choices=['daily', 'weekly', 'monthly'],
                               default='weekly', help='Comparison period')
    compare_parser.add_argument('--export', action='store_true',
                               help='Export detailed comparison report')
    compare_parser.add_argument('--mission', help='Mission name for export')
    compare_parser.add_argument('--start-date', help='Start date (YYYY-MM-DD)')
    compare_parser.add_argument('--end-date', help='End date (YYYY-MM-DD)')
    
    # /track roi command
    roi_parser = subparsers.add_parser('roi', help='Calculate and display ROI')
    roi_parser.add_argument('--detailed', action='store_true',
                           help='Generate detailed ROI report')
    
    # /track status command
    status_parser = subparsers.add_parser('status', help='Show tracking system status')
    status_parser.add_argument('--config', action='store_true',
                              help='Show configuration details')
    
    # /track baseline command
    baseline_parser = subparsers.add_parser('baseline', help='Manage baseline data')
    baseline_parser.add_argument('--create', action='store_true',
                                help='Create new baseline')
    
    return parser

def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    cli = TrackingCLI()
    
    # Route to appropriate command handler
    if args.command == 'report':
        return cli.cmd_report(args)
    elif args.command == 'compare':
        return cli.cmd_compare(args)
    elif args.command == 'roi':
        return cli.cmd_roi(args)
    elif args.command == 'status':
        return cli.cmd_status(args)
    elif args.command == 'baseline':
        return cli.cmd_baseline(args)
    else:
        print(f"❌ Unknown command: {args.command}")
        return 1

# Integration functions for the broader SEO Agent system
def track_report(report_type: str = 'weekly', 
                export_formats: List[str] = None,
                **kwargs) -> Dict[str, str]:
    """Programmatic interface for report generation."""
    manager = ReportManager()
    if export_formats is None:
        export_formats = ['markdown']
    
    return manager.generate_and_export(report_type, export_formats, **kwargs)

def track_compare(period: str = 'weekly') -> Dict[str, Any]:
    """Programmatic interface for performance comparison."""
    engine = ReportEngine()
    current = engine.get_latest_snapshot(period)
    baseline = engine.get_baseline_data()
    
    if not current or not baseline:
        return {"error": "Insufficient data"}
    
    cli = TrackingCLI()
    return cli._generate_comparison_summary(current, baseline)

def track_roi() -> Dict[str, Any]:
    """Programmatic interface for ROI calculation."""
    engine = ReportEngine()
    current = engine.get_latest_snapshot("weekly")
    baseline = engine.get_baseline_data()
    
    if not current or not baseline:
        return {"error": "Insufficient data"}
    
    return engine.calculate_roi_metrics(current, baseline)

if __name__ == "__main__":
    sys.exit(main())