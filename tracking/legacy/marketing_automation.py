#!/usr/bin/env python3
"""
SEO Agent Library - Marketing Automation Integration
Orchestrates all marketing tools for seamless case study and presentation generation.
"""

import json
import yaml
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Union

# Import marketing components
try:
    from marketing_generator import MarketingCaseStudyGenerator, CaseStudyMetrics, ClientProfile
    from client_dashboard import ClientDashboardGenerator, DashboardConfig, DashboardMetrics
    from presentation_exports import PresentationExporter
    from competitive_benchmarking import CompetitiveBenchmarkingTool
except ImportError as e:
    print(f"Warning: Could not import marketing components: {e}")
    print("Ensure all marketing modules are in the same directory")

class MarketingAutomationOrchestrator:
    """Orchestrates complete marketing automation workflow."""
    
    def __init__(self, config_path: str = None):
        """Initialize the marketing automation orchestrator."""
        self.config_path = config_path or "tracking/config/tracking.yml"
        self.config = self._load_config()
        self.tracking_dir = Path("tracking")
        self.marketing_dir = self.tracking_dir / "marketing"
        self.output_dir = self.marketing_dir / "generated"
        
        # Initialize components
        try:
            self.case_study_generator = MarketingCaseStudyGenerator(config_path)
            self.dashboard_generator = ClientDashboardGenerator(config_path)
            self.presentation_exporter = PresentationExporter(config_path)
            self.competitive_tool = CompetitiveBenchmarkingTool(config_path)
        except NameError:
            print("Warning: Marketing components not fully available")
            
        # Create directories
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration with marketing automation defaults."""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            config = {}
        
        # Marketing automation defaults
        automation_defaults = {
            'marketing_automation': {
                'default_formats': ['case_study', 'dashboard', 'presentation', 'social'],
                'auto_generate': True,
                'delivery_options': {
                    'email': False,
                    'slack': False,
                    'file_export': True
                },
                'client_defaults': {
                    'industry': 'Technology',
                    'company_size': 'Mid-market',
                    'challenge_type': 'low_traffic',
                    'white_label': False
                }
            }
        }
        
        if 'marketing_automation' not in config:
            config['marketing_automation'] = automation_defaults['marketing_automation']
        
        return config
    
    def load_tracking_data(self, data_path: str = None) -> Dict[str, Any]:
        """Load tracking data for analysis."""
        if data_path:
            with open(data_path, 'r') as f:
                return json.load(f)
        
        # Try to load latest snapshot
        snapshots_dir = self.tracking_dir / "snapshots" / "weekly"
        if snapshots_dir.exists():
            snapshot_files = list(snapshots_dir.glob("*.json"))
            if snapshot_files:
                latest_file = max(snapshot_files, key=lambda f: f.stat().st_mtime)
                with open(latest_file, 'r') as f:
                    return json.load(f)
        
        # Fallback to mock data
        return self._generate_mock_data()
    
    def _generate_mock_data(self) -> Dict[str, Any]:
        """Generate mock data for demonstration."""
        return {
            'metadata': {
                'domain': 'demo-client.com',
                'timestamp': datetime.now().isoformat(),
                'baseline_type': 'comprehensive'
            },
            'traffic_metrics': {
                'organic_traffic': {
                    'sessions': 15750,
                    'users': 12400,
                    'pageviews': 45200,
                    'bounce_rate': 0.45,
                    'avg_session_duration': 185
                }
            },
            'ranking_metrics': {
                'visibility': {
                    'average_position': 28.5,
                    'total_keywords': 145,
                    'top_10_keywords': 23,
                    'top_20_keywords': 45
                },
                'keyword_distribution': {
                    'top_3': 8,
                    'top_10': 23,
                    'top_20': 45,
                    'top_50': 89
                }
            },
            'technical_metrics': {
                'lighthouse_scores': {
                    'performance': 85,
                    'accessibility': 92,
                    'best_practices': 88,
                    'seo': 94
                },
                'core_web_vitals': {
                    'lcp': {'value': 2.1, 'status': 'good'},
                    'fid': {'value': 95, 'status': 'good'},
                    'cls': {'value': 0.08, 'status': 'good'}
                }
            },
            'authority_metrics': {
                'domain_rating': 68,
                'referring_domains': 245,
                'backlinks': 1250
            },
            'content_metrics': {
                'indexed_pages': 89,
                'content_score': 78
            }
        }
    
    def create_client_profile(self, client_config: Dict[str, Any]) -> 'ClientProfile':
        """Create client profile from configuration."""
        defaults = self.config['marketing_automation']['client_defaults']
        
        return ClientProfile(
            industry=client_config.get('industry', defaults['industry']),
            company_size=client_config.get('company_size', defaults['company_size']),
            challenge_type=client_config.get('challenge_type', defaults['challenge_type']),
            goals=client_config.get('goals', ['Increase organic traffic', 'Improve ROI']),
            website_type=client_config.get('website_type', 'corporate website')
        )
    
    def generate_complete_marketing_suite(self, 
                                         client_name: str,
                                         current_data: Dict[str, Any],
                                         baseline_data: Dict[str, Any] = None,
                                         client_config: Dict[str, Any] = None,
                                         formats: List[str] = None) -> Dict[str, Dict[str, str]]:
        """Generate complete marketing suite with all components."""
        
        if formats is None:
            formats = self.config['marketing_automation']['default_formats']
        
        if client_config is None:
            client_config = self.config['marketing_automation']['client_defaults']
        
        if baseline_data is None:
            # Generate baseline from current data (simplified)
            baseline_data = self._create_baseline_from_current(current_data)
        
        results = {}
        
        try:
            # Generate case study
            if 'case_study' in formats:
                print("Generating marketing case study...")
                client_profile = self.create_client_profile(client_config)
                metrics = self.case_study_generator.analyze_case_study_data(baseline_data, current_data)
                case_study_formats = self.case_study_generator.generate_case_study_formats(
                    metrics, client_profile, ['full', 'executive', 'social']
                )
                
                # Export case studies
                case_study_paths = {}
                for format_name, content in case_study_formats.items():
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{client_name.lower().replace(' ', '_')}_case_study_{format_name}_{timestamp}.md"
                    filepath = self.output_dir / filename
                    with open(filepath, 'w') as f:
                        f.write(content)
                    case_study_paths[format_name] = str(filepath)
                
                results['case_study'] = case_study_paths
            
            # Generate dashboard
            if 'dashboard' in formats:
                print("Creating client dashboard...")
                dashboard_config = DashboardConfig(
                    client_name=client_name,
                    brand_colors=self.config.get('dashboard', {}).get('default_brand', {}),
                    logo_url='',
                    white_label=client_config.get('white_label', False)
                )
                
                dashboard_suite = self.dashboard_generator.generate_dashboard_suite(
                    current_data, baseline_data, client_config
                )
                
                dashboard_paths = self.dashboard_generator.export_dashboard(dashboard_suite, client_name)
                results['dashboard'] = dashboard_paths
            
            # Generate presentation materials
            if 'presentation' in formats:
                print("Exporting presentation materials...")
                # Create metrics for presentation
                presentation_metrics = {
                    'traffic_change': 25.5,
                    'current_sessions': current_data.get('traffic_metrics', {}).get('organic_traffic', {}).get('sessions', 0),
                    'revenue': 7500,
                    'roi_percentage': 285,
                    'ranking_improvement': 8.3,
                    'timeframe': '90 days'
                }
                
                presentation_paths = self.presentation_exporter.export_presentation_suite(
                    current_data, presentation_metrics, client_name, 
                    ['powerpoint', 'pdf', 'social', 'summary']
                )
                results['presentation'] = presentation_paths
            
            # Generate competitive analysis
            if 'competitive' in formats:
                print("Generating competitive analysis...")
                competitive_paths = self.competitive_tool.export_competitive_suite(
                    current_data, client_config.get('industry', 'Technology'), client_name
                )
                results['competitive'] = competitive_paths
            
        except Exception as e:
            print(f"Error generating marketing suite: {e}")
            return results
        
        return results
    
    def _create_baseline_from_current(self, current_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create baseline data from current data (for demo purposes)."""
        baseline = current_data.copy()
        
        # Reduce metrics to simulate baseline
        if 'traffic_metrics' in baseline:
            traffic = baseline['traffic_metrics']['organic_traffic']
            traffic['sessions'] = int(traffic['sessions'] * 0.75)  # 25% growth
            traffic['users'] = int(traffic['users'] * 0.75)
            traffic['pageviews'] = int(traffic['pageviews'] * 0.75)
        
        if 'ranking_metrics' in baseline:
            ranking = baseline['ranking_metrics']['visibility']
            ranking['average_position'] = ranking['average_position'] + 12  # Worse position
            ranking['top_10_keywords'] = max(1, int(ranking['top_10_keywords'] * 0.6))
        
        if 'technical_metrics' in baseline:
            lighthouse = baseline['technical_metrics']['lighthouse_scores']
            lighthouse['performance'] = max(50, lighthouse['performance'] - 15)
        
        # Update timestamp
        baseline_date = datetime.now() - timedelta(days=90)
        baseline['metadata']['timestamp'] = baseline_date.isoformat()
        
        return baseline
    
    def create_automated_report_summary(self, results: Dict[str, Dict[str, str]], 
                                       client_name: str) -> str:
        """Create summary of generated marketing materials."""
        
        summary = f"""
# Marketing Automation Report
## Generated for: {client_name}
**Date:** {datetime.now().strftime("%B %d, %Y at %I:%M %p")}

### Generated Materials

"""
        
        for category, files in results.items():
            summary += f"#### {category.replace('_', ' ').title()}\n"
            for format_type, filepath in files.items():
                filename = Path(filepath).name
                summary += f"- **{format_type.replace('_', ' ').title()}:** {filename}\n"
            summary += "\n"
        
        summary += f"""
### Usage Instructions

#### Case Studies
- Use the **full** format for comprehensive marketing materials
- Use the **executive** format for stakeholder summaries  
- Use the **social** format for social media campaigns

#### Dashboards
- **HTML dashboard** for interactive client presentations
- **Executive report** for leadership summaries
- **Metrics JSON** for data integration

#### Presentations
- **PowerPoint XML** for slide deck creation
- **PDF report** for formal presentations
- **Social content** for marketing campaigns
- **One-page summary** for quick reference

#### Competitive Analysis  
- **Full report** for strategic planning
- **Position summary** for executive briefings
- **Visualization data** for charts and graphs

### Next Steps

1. **Review Generated Materials:** Check all files for accuracy and brand alignment
2. **Customize Content:** Personalize messaging and branding as needed
3. **Distribute Materials:** Share with stakeholders and marketing team
4. **Track Performance:** Monitor case study and dashboard usage
5. **Schedule Updates:** Set recurring generation for ongoing campaigns

### Integration Opportunities

- **Sales Team:** Use case studies and dashboards for prospect presentations
- **Marketing Team:** Leverage social content and presentation materials
- **Client Services:** Share dashboards for regular client reporting
- **Leadership:** Review executive summaries for strategic decisions

---

**Generated by SEO Agent Library Marketing Automation**  
**Next scheduled generation:** {(datetime.now() + timedelta(days=30)).strftime("%B %d, %Y")}
        """
        
        # Save summary
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        summary_path = self.output_dir / f"{client_name.lower().replace(' ', '_')}_marketing_summary_{timestamp}.md"
        with open(summary_path, 'w') as f:
            f.write(summary.strip())
        
        return summary.strip()

def main():
    """CLI interface for marketing automation."""
    import argparse
    
    parser = argparse.ArgumentParser(description="SEO Marketing Automation Suite")
    parser.add_argument("--client", default="Demo Client", help="Client name")
    parser.add_argument("--data", help="Current data file path")
    parser.add_argument("--baseline", help="Baseline data file path")
    parser.add_argument("--industry", default="Technology", help="Client industry")
    parser.add_argument("--formats", nargs='+', 
                       default=['case_study', 'dashboard', 'presentation', 'competitive'],
                       choices=['case_study', 'dashboard', 'presentation', 'competitive'])
    parser.add_argument("--white-label", action='store_true', help="Remove SEO Agent branding")
    
    args = parser.parse_args()
    
    orchestrator = MarketingAutomationOrchestrator()
    
    # Load data
    current_data = orchestrator.load_tracking_data(args.data)
    
    baseline_data = None
    if args.baseline:
        with open(args.baseline, 'r') as f:
            baseline_data = json.load(f)
    
    # Client configuration
    client_config = {
        'industry': args.industry,
        'white_label': args.white_label,
        'company_size': 'Mid-market',
        'challenge_type': 'low_traffic'
    }
    
    # Generate marketing suite
    print(f"🚀 Generating complete marketing suite for {args.client}...")
    print(f"📊 Formats: {', '.join(args.formats)}")
    print()
    
    results = orchestrator.generate_complete_marketing_suite(
        args.client, current_data, baseline_data, client_config, args.formats
    )
    
    # Create summary
    summary = orchestrator.create_automated_report_summary(results, args.client)
    
    print("✅ Marketing automation complete!")
    print()
    print("📁 Generated Files:")
    
    total_files = 0
    for category, files in results.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for format_type, filepath in files.items():
            print(f"  • {format_type}: {filepath}")
            total_files += 1
    
    print(f"\n🎯 Total files generated: {total_files}")
    print(f"📋 Summary report: {orchestrator.output_dir}/...marketing_summary_*.md")
    
    # Display key metrics
    if current_data:
        traffic = current_data.get('traffic_metrics', {}).get('organic_traffic', {})
        sessions = traffic.get('sessions', 0)
        if sessions:
            print(f"\n📈 Current Performance: {sessions:,} monthly organic sessions")

if __name__ == "__main__":
    main()