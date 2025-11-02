#!/usr/bin/env python3
"""
Instagram Ban Analyzer Pro - Main Entry Point
Advanced tool to analyze Instagram accounts for potential ban risks with real data.
"""

import sys
import os
from report_generator import ReportGenerator, Color

def main():
    """Main function to run the Instagram Ban Analyzer Pro"""
    try:
        ReportGenerator.show_banner()
        
        print(f"\n{Color.CYAN}🤖 Welcome to Instagram Ban Analyzer Pro!{Color.END}")
        print(f"{Color.YELLOW}This tool analyzes both PUBLIC and PRIVATE Instagram accounts.{Color.END}")
        
        while True:
            username = input(f"\n{Color.CYAN}Enter Instagram username (or 'quit' to exit): {Color.END}").strip().lower()
            
            if username in ['quit', 'exit', 'q']:
                print(f"{Color.GREEN}👋 Thank you for using Instagram Ban Analyzer Pro!{Color.END}")
                break
                
            if not username:
                print(f"{Color.RED}❌ Error: Username cannot be empty!{Color.END}")
                continue
                
            if len(username) < 3:
                print(f"{Color.RED}❌ Error: Username too short!{Color.END}")
                continue
                
            print(f"\n{Color.YELLOW}🎯 Analyzing account: @{username}{Color.END}")
            
            try:
                # Generate comprehensive report
                report = ReportGenerator.generate_comprehensive_report(username)
                
                # Display the report
                ReportGenerator.display_report(report)
                
                # Option to save report
                save_choice = input(f"\n{Color.CYAN}💾 Save report to file? (y/N): {Color.END}").strip().lower()
                if save_choice in ['y', 'yes']:
                    filename = f"instagram_analysis_{username}_{report['report_id'].split('_')[-1]}.txt"
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(ReportGenerator.generate_text_report(report))
                    print(f"{Color.GREEN}✅ Report saved as: {filename}{Color.END}")
                    
            except KeyboardInterrupt:
                print(f"\n{Color.RED}⏹️  Analysis interrupted by user.{Color.END}")
                continue
            except Exception as e:
                print(f"\n{Color.RED}❌ Error during analysis: {str(e)}{Color.END}")
                continue
                
            # Ask if user wants to analyze another account
            another = input(f"\n{Color.CYAN}🔄 Analyze another account? (Y/n): {Color.END}").strip().lower()
            if another in ['n', 'no']:
                print(f"{Color.GREEN}👋 Thank you for using Instagram Ban Analyzer Pro!{Color.END}")
                break
                
    except KeyboardInterrupt:
        print(f"\n{Color.RED}👋 Program terminated by user.{Color.END}")
    except Exception as e:
        print(f"\n{Color.RED}💥 Critical error: {str(e)}{Color.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()
