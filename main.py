#!/usr/bin/env python3
"""
Instagram Ban Analyzer - Main Entry Point
A tool to analyze Instagram accounts for potential ban risks.
"""

import sys
import os

# Add the current directory to Python path to fix imports
sys.path.insert(0, os.path.dirname(__file__))

from src.analyzer import InstagramAccountAnalyzer
from src.ban_engine import BanRecommendationEngine
from src.report_generator import ReportGenerator

def main():
    """Main function to run the Instagram Ban Analyzer"""
    ReportGenerator.show_banner()
    
    username = input(f"{ReportGenerator.Color.CYAN}Enter Instagram username to analyze: {ReportGenerator.Color.END}")
    
    if not username.strip():
        print(f"{ReportGenerator.Color.RED}Error: Username cannot be empty!{ReportGenerator.Color.END}")
        return
    
    print(f"\n{ReportGenerator.Color.YELLOW}Analyzing account: @{username}{ReportGenerator.Color.END}")
    ReportGenerator.typing_effect(f"{ReportGenerator.Color.GREEN}Fetching account data...{ReportGenerator.Color.END}")
    
    try:
        report = ReportGenerator.generate_ban_report(username)
        ReportGenerator.display_report(report)
        
    except KeyboardInterrupt:
        print(f"\n{ReportGenerator.Color.RED}Analysis interrupted by user.{ReportGenerator.Color.END}")
    except Exception as e:
        print(f"\n{ReportGenerator.Color.RED}Error during analysis: {e}{ReportGenerator.Color.END}")

if __name__ == "__main__":
    main()