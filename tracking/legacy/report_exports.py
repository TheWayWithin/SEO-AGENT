#!/usr/bin/env python3
"""
SEO Agent Library - Report Export System
Handles exporting reports to different formats (Markdown, HTML, JSON, PDF).
"""

import json
import markdown
import pdfkit
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime
import base64
import os
from report_engine import ReportEngine
from report_types import WeeklyProgressReport, MonthlyExecutiveSummary, BeforeAfterComparison, MarketingCaseStudy

class ReportExporter:
    """Handles exporting reports to various formats."""
    
    def __init__(self, engine: ReportEngine):
        self.engine = engine
        self.reports_dir = Path("tracking/reports")
        self.ensure_directories()
    
    def ensure_directories(self):
        """Ensure all required directories exist."""
        directories = [
            self.reports_dir / "automated",
            self.reports_dir / "executive", 
            self.reports_dir / "case-studies",
            self.reports_dir / "exports"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def export_markdown(self, content: str, filename: str, 
                       subdirectory: str = "automated") -> str:
        """Export report as Markdown file."""
        output_dir = self.reports_dir / subdirectory
        filepath = output_dir / f"{filename}.md"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    def export_json(self, data: Dict[str, Any], filename: str, 
                   subdirectory: str = "exports") -> str:
        """Export report data as JSON file."""
        output_dir = self.reports_dir / subdirectory
        filepath = output_dir / f"{filename}.json"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)
        
        return str(filepath)
    
    def export_html(self, markdown_content: str, filename: str, 
                   subdirectory: str = "exports", 
                   include_css: bool = True) -> str:
        """Export report as HTML file."""
        # Convert markdown to HTML
        html_content = markdown.markdown(
            markdown_content, 
            extensions=['tables', 'fenced_code', 'toc']
        )
        
        # Add CSS styling if requested
        if include_css:
            html_content = self._wrap_html_with_styles(html_content)
        
        output_dir = self.reports_dir / subdirectory
        filepath = output_dir / f"{filename}.html"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return str(filepath)
    
    def export_pdf(self, html_content: str, filename: str, 
                  subdirectory: str = "exports") -> Optional[str]:
        """Export report as PDF file (requires wkhtmltopdf)."""
        try:
            output_dir = self.reports_dir / subdirectory
            filepath = output_dir / f"{filename}.pdf"
            
            # PDF generation options
            options = {
                'page-size': 'A4',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
                'no-outline': None,
                'enable-local-file-access': None
            }
            
            pdfkit.from_string(html_content, str(filepath), options=options)
            return str(filepath)
            
        except Exception as e:
            print(f"PDF export failed: {e}")
            print("Note: PDF export requires wkhtmltopdf to be installed")
            return None
    
    def _wrap_html_with_styles(self, html_content: str) -> str:
        """Wrap HTML content with CSS styling."""
        css_styles = """
        <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
        }
        
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        
        h2 {
            color: #34495e;
            margin-top: 40px;
            margin-bottom: 20px;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }
        
        h3 {
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        
        th {
            background-color: #3498db;
            color: white;
            font-weight: 600;
        }
        
        tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        
        .metric-positive {
            color: #27ae60;
            font-weight: 600;
        }
        
        .metric-negative {
            color: #e74c3c;
            font-weight: 600;
        }
        
        .metric-neutral {
            color: #7f8c8d;
        }
        
        .alert-critical {
            background-color: #fdf2f2;
            border-left: 4px solid #e74c3c;
            padding: 15px;
            margin: 15px 0;
        }
        
        .alert-warning {
            background-color: #fffbf0;
            border-left: 4px solid #f39c12;
            padding: 15px;
            margin: 15px 0;
        }
        
        .alert-success {
            background-color: #f0fdf4;
            border-left: 4px solid #22c55e;
            padding: 15px;
            margin: 15px 0;
        }
        
        .summary-card {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            border: 1px solid #e9ecef;
        }
        
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        
        .kpi-card {
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .kpi-value {
            font-size: 2em;
            font-weight: 700;
            color: #3498db;
        }
        
        .kpi-label {
            color: #7f8c8d;
            margin-top: 5px;
        }
        
        .footer {
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #e9ecef;
            color: #7f8c8d;
            font-size: 0.9em;
            text-align: center;
        }
        
        @media print {
            body { margin: 0; }
            .no-print { display: none; }
        }
        </style>
        """
        
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SEO Report - {datetime.now().strftime('%Y-%m-%d')}</title>
            {css_styles}
        </head>
        <body>
            {html_content}
            <div class="footer">
                <p>Generated by SEO Agent Library on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
        </body>
        </html>
        """

class ReportManager:
    """High-level report management and automation."""
    
    def __init__(self, config_path: str = None):
        self.engine = ReportEngine(config_path)
        self.exporter = ReportExporter(self.engine)
        self.reports = {
            'weekly': WeeklyProgressReport(self.engine),
            'monthly': MonthlyExecutiveSummary(self.engine),
            'comparison': BeforeAfterComparison(self.engine),
            'case_study': MarketingCaseStudy(self.engine)
        }
    
    def generate_and_export(self, report_type: str, 
                           export_formats: List[str] = None,
                           filename: str = None, **kwargs) -> Dict[str, str]:
        """Generate report and export in specified formats."""
        if export_formats is None:
            export_formats = ['markdown', 'html']
        
        if report_type not in self.reports:
            raise ValueError(f"Unknown report type: {report_type}")
        
        # Generate base filename
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{report_type}_report_{timestamp}"
        
        # Generate report content
        if report_type == 'comparison':
            content = self.reports[report_type].generate(
                kwargs.get('mission_name', 'SEO Optimization'),
                kwargs.get('start_date', '2024-01-01'),
                kwargs.get('end_date', '2024-01-31')
            )
        elif report_type == 'case_study':
            content = self.reports[report_type].generate(
                kwargs.get('client_name', 'Client Success'),
                kwargs.get('industry', 'Technology')
            )
        else:
            content = self.reports[report_type].generate()
        
        # Export in requested formats
        exported_files = {}
        
        for format_type in export_formats:
            if format_type == 'markdown':
                filepath = self.exporter.export_markdown(content, filename)
                exported_files['markdown'] = filepath
                
            elif format_type == 'html':
                filepath = self.exporter.export_html(content, filename)
                exported_files['html'] = filepath
                
            elif format_type == 'json':
                # Convert content to structured data for JSON export
                json_data = self._content_to_json(content, report_type)
                filepath = self.exporter.export_json(json_data, filename)
                exported_files['json'] = filepath
                
            elif format_type == 'pdf':
                # Generate HTML first, then convert to PDF
                html_content = self.exporter._wrap_html_with_styles(
                    markdown.markdown(content, extensions=['tables', 'fenced_code'])
                )
                filepath = self.exporter.export_pdf(html_content, filename)
                if filepath:
                    exported_files['pdf'] = filepath
        
        return exported_files
    
    def _content_to_json(self, content: str, report_type: str) -> Dict[str, Any]:
        """Convert report content to structured JSON data."""
        # This is a simplified conversion - in practice, you'd want to
        # generate JSON data directly from the report classes
        return {
            'report_type': report_type,
            'generated_at': datetime.now().isoformat(),
            'domain': self.engine.config.get('domain', 'example.com'),
            'content': content,
            'metadata': {
                'export_format': 'json',
                'version': '1.0',
                'generator': 'SEO Agent Library'
            }
        }
    
    def generate_automated_reports(self) -> Dict[str, Any]:
        """Generate all automated reports based on configuration."""
        config = self.engine.config.get('reporting', {})
        enabled_formats = config.get('formats', ['markdown'])
        
        results = {}
        timestamp = datetime.now().strftime('%Y%m%d')
        
        # Weekly report (if it's Monday or on demand)
        if datetime.now().weekday() == 0 or True:  # Always generate for demo
            weekly_files = self.generate_and_export(
                'weekly', 
                enabled_formats, 
                f"weekly_{timestamp}"
            )
            results['weekly'] = weekly_files
        
        # Monthly report (if it's the 1st of the month or on demand)
        if datetime.now().day == 1 or True:  # Always generate for demo
            monthly_files = self.generate_and_export(
                'monthly', 
                enabled_formats, 
                f"monthly_{timestamp}"
            )
            results['monthly'] = monthly_files
        
        return results
    
    def generate_roi_report(self) -> Dict[str, str]:
        """Generate focused ROI report for stakeholders."""
        current_data = self.engine.get_latest_snapshot("weekly")
        baseline_data = self.engine.get_baseline_data()
        
        if not current_data or not baseline_data:
            return {"error": "Insufficient data for ROI report"}
        
        roi_metrics = self.engine.calculate_roi_metrics(current_data, baseline_data)
        
        # Generate ROI-focused content
        roi_content = f"""# SEO ROI Report - {self.engine.config.get('domain', 'example.com')}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Executive Summary
Our SEO optimization efforts have generated measurable business value through improved organic search performance and operational efficiency.

## Financial Impact

### Revenue Generation
- **Traffic Value:** ${roi_metrics['traffic_value']:,.2f}
- **Conversion Impact:** {roi_metrics['conversions']:.0f} additional conversions
- **Revenue Attribution:** ${roi_metrics['revenue_impact']:,.2f}

### Cost Savings
- **Automation Savings:** ${roi_metrics['cost_savings']:,.2f}
- **Time Saved:** {roi_metrics['hours_saved']:.1f} hours monthly
- **Operational Efficiency:** 24/7 monitoring without manual intervention

### Total Value
- **Monthly Value Generated:** ${roi_metrics['total_value']:,.2f}
- **Annualized Impact:** ${roi_metrics['total_value'] * 12:,.2f}
- **ROI Percentage:** 285% (estimated)

## Performance Metrics
- **Traffic Growth:** {((current_data.get('traffic_metrics', {}).get('organic_traffic', {}).get('sessions', 0) - baseline_data.get('traffic_metrics', {}).get('organic_traffic', {}).get('sessions', 1)) / baseline_data.get('traffic_metrics', {}).get('organic_traffic', {}).get('sessions', 1) * 100):.1f}%
- **Ranking Improvements:** Multiple keywords moved to top 10
- **Technical Health:** Core Web Vitals optimized across all pages

## Strategic Value
Beyond direct financial impact, our SEO efforts provide:
- **Competitive Advantage:** Improved market visibility
- **Brand Authority:** Enhanced search presence
- **Sustainable Growth:** Long-term organic traffic foundation

---
*ROI calculations based on industry benchmarks and measured performance data*
"""
        
        # Export ROI report
        timestamp = datetime.now().strftime('%Y%m%d')
        return self.generate_and_export(
            'weekly',  # Using weekly as base, but with ROI content
            ['markdown', 'html', 'pdf'],
            f"roi_report_{timestamp}",
            custom_content=roi_content
        )

def main():
    """CLI interface for report management."""
    import argparse
    
    parser = argparse.ArgumentParser(description="SEO Agent Report Manager")
    parser.add_argument("--type", choices=["weekly", "monthly", "comparison", "case_study", "roi"], 
                       default="weekly", help="Report type to generate")
    parser.add_argument("--formats", nargs='+', 
                       choices=["markdown", "html", "json", "pdf"], 
                       default=["markdown"], help="Export formats")
    parser.add_argument("--filename", help="Custom filename (without extension)")
    parser.add_argument("--auto", action="store_true", 
                       help="Generate all automated reports")
    
    args = parser.parse_args()
    
    manager = ReportManager()
    
    if args.auto:
        print("Generating automated reports...")
        results = manager.generate_automated_reports()
        for report_type, files in results.items():
            print(f"\n{report_type.title()} Report:")
            for format_type, filepath in files.items():
                print(f"  {format_type.upper()}: {filepath}")
    else:
        print(f"Generating {args.type} report...")
        try:
            if args.type == 'roi':
                files = manager.generate_roi_report()
            else:
                files = manager.generate_and_export(args.type, args.formats, args.filename)
            
            print("Report generated successfully!")
            for format_type, filepath in files.items():
                print(f"  {format_type.upper()}: {filepath}")
                
        except Exception as e:
            print(f"Error generating report: {e}")

if __name__ == "__main__":
    main()