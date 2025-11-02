from datetime import datetime
import random
import time
from typing import List, Dict
from analyzer import InstagramAccountAnalyzer
from ban_engine import BanRecommendationEngine

class Color:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;205m'
    PURPLE = '\033[38;5;129m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class ReportGenerator:
    """Generate comprehensive Instagram account analysis reports"""

    @staticmethod
    def show_banner():
        """Display awesome ASCII art banner"""
        banner = f"""
{Color.CYAN}{Color.BOLD}
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║  {Color.MAGENTA}▓▓▓▓▓▓▓▓▓▓  {Color.CYAN}▓▓▓▓▓▓▓▓▓▓▓ {Color.GREEN}▓▓▓▓▓▓▓▓▓▓▓ {Color.YELLOW}▓▓▓▓▓▓▓▓▓▓▓ {Color.RED}▓▓▓▓▓▓▓▓▓▓  {Color.CYAN}║
    ║  {Color.MAGENTA}▓▓▓▓▓▓▓▓▓▓▓ {Color.CYAN}▓▓▓▓▓▓▓▓▓▓▓ {Color.GREEN}▓▓▓▓▓▓▓▓▓▓▓ {Color.YELLOW}▓▓▓▓▓▓▓▓▓▓▓ {Color.RED}▓▓▓▓▓▓▓▓▓▓▓ {Color.CYAN}║
    ║  {Color.MAGENTA}▓▓▓     ▓▓▓ {Color.CYAN}▓▓▓        {Color.GREEN}▓▓▓        {Color.YELLOW}▓▓▓        {Color.RED}▓▓▓     ▓▓▓ {Color.CYAN}║
    ║  {Color.MAGENTA}▓▓▓▓▓▓▓▓▓▓▓ {Color.CYAN}▓▓▓▓▓▓▓▓▓  {Color.GREEN}▓▓▓▓▓▓▓▓▓  {Color.YELLOW}▓▓▓▓▓▓▓▓▓  {Color.RED}▓▓▓▓▓▓▓▓▓▓▓ {Color.CYAN}║
    ║  {Color.MAGENTA}▓▓▓▓▓▓▓▓▓▓  {Color.CYAN}▓▓▓▓▓▓▓▓▓  {Color.GREEN}▓▓▓▓▓▓▓▓▓  {Color.YELLOW}▓▓▓▓▓▓▓▓▓  {Color.RED}▓▓▓▓▓▓▓▓▓▓  {Color.CYAN}║
    ║  {Color.MAGENTA}▓▓▓        {Color.CYAN}▓▓▓        {Color.GREEN}▓▓▓        {Color.YELLOW}▓▓▓        {Color.RED}▓▓▓  ▓▓▓    {Color.CYAN}║
    ║  {Color.MAGENTA}▓▓▓        {Color.CYAN}▓▓▓▓▓▓▓▓▓▓▓ {Color.GREEN}▓▓▓▓▓▓▓▓▓▓▓ {Color.YELLOW}▓▓▓▓▓▓▓▓▓▓▓ {Color.RED}▓▓▓   ▓▓▓   {Color.CYAN}║
    ║  {Color.MAGENTA}▓▓▓        {Color.CYAN}▓▓▓▓▓▓▓▓▓▓▓ {Color.GREEN}▓▓▓▓▓▓▓▓▓▓▓ {Color.YELLOW}▓▓▓▓▓▓▓▓▓▓▓ {Color.RED}▓▓▓    ▓▓▓  {Color.CYAN}║
    ║                                                              ║
    ║           {Color.WHITE}{Color.BOLD}🚀 INSTAGRAM BAN ANALYZER PRO 🚀{Color.CYAN}              ║
    ║                                                              ║
    ║         {Color.YELLOW}« Advanced Real-Time Account Analysis »{Color.CYAN}         ║
    ║               {Color.GREEN}Public & Private Accounts{Color.CYAN}                 ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝

                {Color.GREEN}Developed by {Color.RED}M{Color.ORANGE}r{Color.YELLOW}.{Color.GREEN} {Color.CYAN}G{Color.BLUE}e{Color.MAGENTA}i{Color.RED}s{Color.ORANGE}t{Color.END}
        
        """
        print(banner)

    @staticmethod
    def typing_effect(text, delay=0.01):
        """Create typing effect for text"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def generate_comprehensive_report(username: str) -> Dict:
        """Generate comprehensive analysis report"""
        print(f"\n{Color.CYAN}🔄 Initializing analysis for @{username}...{Color.END}")
        
        # Initialize analyzer and get real data
        analyzer = InstagramAccountAnalyzer()
        ReportGenerator.typing_effect(f"{Color.YELLOW}📡 Connecting to Instagram APIs...{Color.END}", 0.03)
        
        stats = analyzer.get_account_stats(username)
        time.sleep(1)
        
        ReportGenerator.typing_effect(f"{Color.BLUE}🔍 Analyzing account behavior patterns...{Color.END}", 0.02)
        analysis = BanRecommendationEngine.calculate_ban_probability(stats)
        
        ReportGenerator.typing_effect(f"{Color.MAGENTA}📊 Generating risk assessment...{Color.END}", 0.02)
        recommendations = BanRecommendationEngine.get_recommendations(analysis, stats)
        quick_reports = BanRecommendationEngine.generate_quick_reports(analysis, username)
        
        return {
            'username': username,
            'account_stats': stats,
            'ban_analysis': analysis,
            'recommendations': recommendations,
            'quick_reports': quick_reports,
            'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'report_id': f"IG_{username}_{int(datetime.now().timestamp())}"
        }

    @staticmethod
    def display_report(report: Dict):
        """Display comprehensive analysis report"""
        stats = report['account_stats']
        analysis = report['ban_analysis']
        
        print(f"\n{Color.CYAN}{Color.BOLD}🛡️  === INSTAGRAM ACCOUNT ANALYSIS REPORT ==={Color.END}")
        print(f"📋 Report ID: {Color.WHITE}{report['report_id']}{Color.END}")
        print(f"👤 Username: {Color.WHITE}@{report['username']}{Color.END}")
        print(f"🕒 Generated: {Color.CYAN}{report['generated_at']}{Color.END}")
        
        # Account Type Information
        account_type = stats.get('account_type', 'personal').replace('_', ' ').title()
        print(f"\n{Color.YELLOW}{Color.BOLD}📈 === ACCOUNT OVERVIEW ==={Color.END}")
        print(f"🔒 Account Type: {Color.BLUE}{'PRIVATE' if stats.get('is_private') else 'PUBLIC'}{Color.END}")
        print(f"⭐ Verification: {Color.GREEN if stats.get('is_verified') else Color.YELLOW}{'✅ VERIFIED' if stats.get('is_verified') else '❌ NOT VERIFIED'}{Color.END}")
        print(f"🏷️  Category: {Color.MAGENTA}{account_type}{Color.END}")
        print(f"📊 Data Source: {Color.CYAN}{stats.get('data_source', 'unknown').replace('_', ' ').title()}{Color.END}")

        # Risk Assessment
        print(f"\n{Color.RED}{Color.BOLD}🚨 === RISK ASSESSMENT ==={Color.END}")
        print(f"📊 Ban Probability: {Color.RED}{analysis['ban_probability']}%{Color.END}")
        print(f"⚠️  Risk Level: {analysis['risk_level']}")
        print(f"⚖️  Score: {Color.CYAN}{analysis['score_breakdown']}/{analysis['max_possible_score']}{Color.END}")

        # Account Statistics
        print(f"\n{Color.GREEN}{Color.Bold}📊 === ACCOUNT STATISTICS ==={Color.END}")
        print(f"👥 Followers: {Color.GREEN}{stats['followers']:,}{Color.END}")
        print(f"🔄 Following: {Color.BLUE}{stats['following']:,}{Color.END}")
        print(f"📸 Posts: {Color.MAGENTA}{stats['posts']:,}{Color.END}")
        print(f"💫 Engagement Rate: {Color.CYAN}{stats['engagement_rate']:.2f}%{Color.END}")
        print(f"📅 Account Age: {Color.YELLOW}{stats['account_age_days']} days{Color.END}")
        print(f"📈 Posts per Day: {Color.WHITE}{stats.get('posts_per_day', 0):.2f}{Color.END}")
        print(f"🔗 Follower Ratio: {Color.ORANGE}{stats.get('follower_ratio', 0):.2f}{Color.END}")
        print(f"⚡ Daily Actions: {Color.PURPLE}{stats['avg_daily_actions']}{Color.END}")
        print(f"🚩 Reports Received: {Color.RED}{stats['reports_received']}{Color.END}")

        # Detected Issues
        print(f"\n{Color.ORANGE}{Color.BOLD}🔍 === DETECTED ISSUES ==={Color.END}")
        if analysis['reasons']:
            for i, reason in enumerate(analysis['reasons'][:5], 1):
                print(f"{reason['color']}{i}. {reason['emoji']} {reason['reason']}: {reason['confidence']}% confidence{Color.END}")
        else:
            print(f"{Color.GREEN}✅ No significant issues detected{Color.END}")

        # Suspicious Content
        if stats.get('suspicious_keywords'):
            print(f"\n{Color.RED}{Color.BOLD}🚩 === SUSPICIOUS CONTENT DETECTED ==={Color.END}")
            for keyword in stats['suspicious_keywords']:
                print(f"❌ {Color.YELLOW}{keyword}{Color.END}")

        # Recommendations
        print(f"\n{Color.BLUE}{Color.BOLD}💡 === RECOMMENDATIONS ==={Color.END}")
        for i, rec in enumerate(report['recommendations'], 1):
            print(f"{i}. {rec}")

        # Quick Reports
        print(f"\n{Color.MAGENTA}{Color.BOLD}📋 === QUICK REPORT TEMPLATES ==={Color.END}")
        for i, report_text in enumerate(report['quick_reports'], 1):
            print(f"{i}. {report_text}")

        # Footer
        print(f"\n{Color.CYAN}{Color.BOLD}🔐 === ANALYSIS COMPLETE ==={Color.END}")
        print(f"{Color.WHITE}Note: This analysis is based on available public data and behavioral patterns.")
        print(f"Always verify information and follow Instagram's community guidelines.{Color.END}")

    @staticmethod
    def generate_text_report(report: Dict) -> str:
        """Generate a text version of the report for saving"""
        stats = report['account_stats']
        analysis = report['ban_analysis']
        
        text_report = f"""
INSTAGRAM ACCOUNT ANALYSIS REPORT
==================================

Basic Information:
- Username: @{report['username']}
- Report ID: {report['report_id']}
- Generated: {report['generated_at']}

Account Overview:
- Type: {'PRIVATE' if stats.get('is_private') else 'PUBLIC'}
- Verified: {'YES' if stats.get('is_verified') else 'NO'}
- Category: {stats.get('account_type', 'personal').replace('_', ' ').title()}
- Data Source: {stats.get('data_source', 'unknown').replace('_', ' ').title()}

Risk Assessment:
- Ban Probability: {analysis['ban_probability']}%
- Risk Level: {analysis['risk_level'].replace(Color.END, '').replace(Color.RED, '').replace(Color.BOLD, '')}
- Score: {analysis['score_breakdown']}/{analysis['max_possible_score']}

Account Statistics:
- Followers: {stats['followers']:,}
- Following: {stats['following']:,}
- Posts: {stats['posts']:,}
- Engagement Rate: {stats['engagement_rate']:.2f}%
- Account Age: {stats['account_age_days']} days
- Posts per Day: {stats.get('posts_per_day', 0):.2f}
- Follower Ratio: {stats.get('follower_ratio', 0):.2f}
- Daily Actions: {stats['avg_daily_actions']}
- Reports Received: {stats['reports_received']}

Detected Issues:
"""
        
        for reason in analysis['reasons']:
            text_report += f"- {reason['reason']}: {reason['confidence']}% confidence\n"
            
        if not analysis['reasons']:
            text_report += "- No significant issues detected\n"
            
        text_report += "\nRecommendations:\n"
        for rec in report['recommendations']:
            text_report += f"- {rec}\n"
            
        return text_report
