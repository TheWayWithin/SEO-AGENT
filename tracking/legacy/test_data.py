#!/usr/bin/env python3
"""
SEO Agent Library - Test Data Generator
Creates sample data for testing the report generation system.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any
import random

class TestDataGenerator:
    """Generates realistic test data for SEO tracking."""
    
    def __init__(self):
        self.tracking_dir = Path("tracking")
        self.ensure_directories()
        
    def ensure_directories(self):
        """Ensure all required directories exist."""
        directories = [
            self.tracking_dir / "baselines",
            self.tracking_dir / "snapshots" / "daily", 
            self.tracking_dir / "snapshots" / "weekly",
            self.tracking_dir / "snapshots" / "monthly",
            self.tracking_dir / "snapshots" / "mission-based"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def generate_baseline_data(self) -> Dict[str, Any]:
        """Generate realistic baseline data."""
        return {
            "metadata": {
                "timestamp": "2024-01-01T00:00:00Z",
                "domain": "example.com",
                "baseline_type": "initial",
                "created_by": "@seo-analyst",
                "version": "1.0"
            },
            "technical_metrics": {
                "core_web_vitals": {
                    "lcp": {
                        "value": 2.8,
                        "unit": "seconds",
                        "status": "needs_improvement"
                    },
                    "fid": {
                        "value": 180,
                        "unit": "milliseconds", 
                        "status": "needs_improvement"
                    },
                    "cls": {
                        "value": 0.15,
                        "unit": "score",
                        "status": "needs_improvement"
                    }
                },
                "lighthouse_scores": {
                    "performance": 68,
                    "accessibility": 85,
                    "best_practices": 78,
                    "seo": 72,
                    "pwa": 45
                },
                "technical_health": {
                    "crawl_errors": 23,
                    "broken_links": 8,
                    "redirect_chains": 12,
                    "duplicate_content": 15,
                    "missing_meta": 34,
                    "schema_errors": 6
                }
            },
            "traffic_metrics": {
                "organic_traffic": {
                    "sessions": 12450,
                    "users": 10230,
                    "new_users": 8950,
                    "pageviews": 18670,
                    "pages_per_session": 1.5,
                    "avg_session_duration": 165,
                    "bounce_rate": 68.5
                },
                "conversions": {
                    "total_conversions": 185,
                    "conversion_rate": 1.48,
                    "goal_completions": [],
                    "ecommerce_transactions": 89,
                    "revenue": 12500.00
                }
            },
            "ranking_metrics": {
                "visibility": {
                    "average_position": 24.8,
                    "impressions": 45600,
                    "clicks": 1890,
                    "ctr": 4.14
                },
                "keyword_distribution": {
                    "total_keywords": 1250,
                    "top_3": 45,
                    "top_10": 125,
                    "top_20": 245,
                    "top_50": 485,
                    "top_100": 780
                }
            },
            "content_metrics": {
                "content_inventory": {
                    "total_pages": 450,
                    "indexed_pages": 380,
                    "blog_posts": 125,
                    "product_pages": 89
                }
            },
            "authority_metrics": {
                "domain_authority": {
                    "domain_rating": 42
                },
                "backlinks": {
                    "total_backlinks": 2340,
                    "referring_domains": 145
                }
            }
        }
    
    def generate_improved_snapshot(self, baseline: Dict[str, Any], 
                                 improvement_factor: float = 1.25) -> Dict[str, Any]:
        """Generate an improved snapshot based on baseline."""
        snapshot = baseline.copy()
        
        # Update metadata
        snapshot["metadata"]["timestamp"] = datetime.now().isoformat()
        snapshot["metadata"]["baseline_type"] = "current"
        
        # Improve technical metrics
        tech = snapshot["technical_metrics"]
        tech["lighthouse_scores"]["performance"] = min(95, int(tech["lighthouse_scores"]["performance"] * 1.25))
        tech["lighthouse_scores"]["seo"] = min(98, int(tech["lighthouse_scores"]["seo"] * 1.15))
        tech["technical_health"]["crawl_errors"] = max(0, int(tech["technical_health"]["crawl_errors"] * 0.2))
        tech["technical_health"]["broken_links"] = max(0, int(tech["technical_health"]["broken_links"] * 0.1))
        
        # Improve Core Web Vitals
        tech["core_web_vitals"]["lcp"]["value"] = max(1.2, tech["core_web_vitals"]["lcp"]["value"] * 0.7)
        tech["core_web_vitals"]["lcp"]["status"] = "good"
        tech["core_web_vitals"]["fid"]["value"] = max(50, tech["core_web_vitals"]["fid"]["value"] * 0.4)
        tech["core_web_vitals"]["fid"]["status"] = "good"
        tech["core_web_vitals"]["cls"]["value"] = max(0.05, tech["core_web_vitals"]["cls"]["value"] * 0.5)
        tech["core_web_vitals"]["cls"]["status"] = "good"
        
        # Improve traffic metrics
        traffic = snapshot["traffic_metrics"]["organic_traffic"]
        traffic["sessions"] = int(traffic["sessions"] * improvement_factor)
        traffic["users"] = int(traffic["users"] * improvement_factor)
        traffic["new_users"] = int(traffic["new_users"] * improvement_factor)
        traffic["pageviews"] = int(traffic["pageviews"] * improvement_factor)
        traffic["pages_per_session"] = min(3.5, traffic["pages_per_session"] * 1.15)
        traffic["avg_session_duration"] = min(300, traffic["avg_session_duration"] * 1.20)
        traffic["bounce_rate"] = max(35.0, traffic["bounce_rate"] * 0.85)
        
        # Improve conversions
        conversions = snapshot["traffic_metrics"]["conversions"]
        conversions["total_conversions"] = int(conversions["total_conversions"] * improvement_factor)
        conversions["conversion_rate"] = min(3.5, conversions["conversion_rate"] * 1.15)
        conversions["ecommerce_transactions"] = int(conversions["ecommerce_transactions"] * improvement_factor)
        conversions["revenue"] = conversions["revenue"] * improvement_factor
        
        # Improve rankings
        rankings = snapshot["ranking_metrics"]
        rankings["visibility"]["average_position"] = max(8.5, rankings["visibility"]["average_position"] * 0.7)
        rankings["visibility"]["impressions"] = int(rankings["visibility"]["impressions"] * 1.35)
        rankings["visibility"]["clicks"] = int(rankings["visibility"]["clicks"] * improvement_factor)
        rankings["visibility"]["ctr"] = min(8.5, rankings["visibility"]["ctr"] * 1.15)
        
        # Improve keyword distribution
        kwd = rankings["keyword_distribution"] 
        kwd["top_3"] = int(kwd["top_3"] * 1.4)
        kwd["top_10"] = int(kwd["top_10"] * 1.3)
        kwd["top_20"] = int(kwd["top_20"] * 1.25)
        
        return snapshot
    
    def generate_snapshot_series(self, baseline: Dict[str, Any], 
                               count: int = 8) -> list:
        """Generate a series of progressive snapshots."""
        snapshots = []
        
        for i in range(count):
            # Progressive improvement over time
            improvement = 1.0 + (i * 0.05)  # 5% improvement each period
            
            snapshot = self.generate_improved_snapshot(baseline, improvement)
            
            # Add some realistic variance
            variance = random.uniform(0.95, 1.05)
            traffic = snapshot["traffic_metrics"]["organic_traffic"]
            traffic["sessions"] = int(traffic["sessions"] * variance)
            traffic["users"] = int(traffic["users"] * variance)
            
            # Update timestamp
            days_ago = (count - i - 1) * 7  # Weekly snapshots
            timestamp = (datetime.now() - timedelta(days=days_ago)).isoformat()
            snapshot["metadata"]["timestamp"] = timestamp
            
            snapshots.append(snapshot)
        
        return snapshots
    
    def save_test_data(self):
        """Save all test data to appropriate directories."""
        print("🧪 Generating SEO test data...")
        
        # Generate baseline
        baseline = self.generate_baseline_data()
        baseline_path = self.tracking_dir / "baselines" / "baseline_20240101.json"
        
        with open(baseline_path, 'w') as f:
            json.dump(baseline, f, indent=2)
        print(f"✅ Baseline saved: {baseline_path}")
        
        # Generate weekly snapshots
        weekly_snapshots = self.generate_snapshot_series(baseline, 8)
        
        for i, snapshot in enumerate(weekly_snapshots):
            timestamp = snapshot["metadata"]["timestamp"][:10].replace("-", "")
            filename = f"weekly_{timestamp}_{i:02d}.json"
            snapshot_path = self.tracking_dir / "snapshots" / "weekly" / filename
            
            with open(snapshot_path, 'w') as f:
                json.dump(snapshot, f, indent=2)
        
        print(f"✅ Generated {len(weekly_snapshots)} weekly snapshots")
        
        # Generate monthly snapshot (latest improvement)
        monthly_snapshot = self.generate_improved_snapshot(baseline, 1.45)
        monthly_path = self.tracking_dir / "snapshots" / "monthly" / "monthly_202401.json"
        
        with open(monthly_path, 'w') as f:
            json.dump(monthly_snapshot, f, indent=2)
        print(f"✅ Monthly snapshot saved: {monthly_path}")
        
        # Generate mission-based snapshot
        mission_snapshot = self.generate_improved_snapshot(baseline, 1.35)
        mission_snapshot["metadata"]["mission_name"] = "Technical SEO Optimization"
        mission_snapshot["metadata"]["mission_id"] = "TECH_001"
        
        mission_path = self.tracking_dir / "snapshots" / "mission-based" / "mission_tech_001.json"
        
        with open(mission_path, 'w') as f:
            json.dump(mission_snapshot, f, indent=2)
        print(f"✅ Mission snapshot saved: {mission_path}")
        
        print("\n📊 Test data generation complete!")
        print("Ready to test report generation with realistic SEO data.")

def main():
    """Generate test data for the SEO tracking system."""
    generator = TestDataGenerator()
    generator.save_test_data()
    
    # Test basic report generation
    print("\n🧪 Testing report generation...")
    
    try:
        from report_engine import ReportEngine
        from report_exports import ReportManager
        
        # Initialize systems
        engine = ReportEngine()
        manager = ReportManager()
        
        print("✅ Report engine initialized")
        
        # Test basic data loading
        baseline = engine.get_baseline_data()
        current = engine.get_latest_snapshot("weekly")
        
        if baseline and current:
            print("✅ Test data loaded successfully")
            
            # Test ROI calculation
            roi_metrics = engine.calculate_roi_metrics(current, baseline)
            print(f"✅ ROI calculation: ${roi_metrics['total_value']:,.2f} total value")
            
            # Test report generation
            files = manager.generate_and_export('weekly', ['markdown'])
            print(f"✅ Test report generated: {list(files.values())[0]}")
            
        else:
            print("❌ Test data not loaded properly")
            
    except ImportError as e:
        print(f"⚠️ Could not test report generation: {e}")
        print("Run the individual modules to test functionality")

if __name__ == "__main__":
    main()