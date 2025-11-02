from datetime import datetime
import random
import time
from typing import List, Dict

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
    """Generate and manage Instagram ban recommendations and report suggestions"""

    Color = Color  # Make Color class accessible

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
    ║              {Color.WHITE}{Color.BOLD}🚀 INSTAGRAM BAN ANALYZER PRO 🚀{Color.CYAN}              ║
    ║                                                              ║
    ║           {Color.YELLOW}« Advanced Account Analysis System »{Color.CYAN}           ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝

                {Color.GREEN}Developed by {Color.RED}M{Color.ORANGE}r{Color.YELLOW}.{Color.GREEN} {Color.CYAN}G{Color.BLUE}e{Color.MAGENTA}i{Color.RED}s{Color.ORANGE}t{Color.END}
        
        """
        print(banner)

    @staticmethod
    def typing_effect(text, delay=0.02):
        """Create typing effect for text"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def generate_quick_reports(username: str) -> List[str]:
        """Generate quick report suggestions"""
        from analyzer import InstagramAccountAnalyzer
        from ban_engine import BanRecommendationEngine
        
        stats = InstagramAccountAnalyzer.get_account_stats(username)
        analysis = BanRecommendationEngine.calculate_ban_probability(stats)

        top_reasons = analysis['reasons'][:random.randint(3, 5)]
        quick_reports = []
        
        for reason in top_reasons:
            quantity = random.randint(1, 5)
            quick_reports.append(f"{quantity}x {reason['reason']} {reason['emoji']}")

        return quick_reports

    @staticmethod
    def _generate_recommendations(analysis: Dict, stats: Dict) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        if analysis['ban_probability'] > 80:
            recommendations.append("🚨 Immediate action recommended: Consider reporting this account")
        elif analysis['ban_probability'] > 60:
            recommendations.append("⚠️ High risk account: Monitor activity closely")
        elif analysis['ban_probability'] > 40:
            recommendations.append("🔍 Moderate risk: Further investigation suggested")
        else:
            recommendations.append("✅ Low risk: Account appears normal")
            
        for reason in analysis['reasons'][:3]:
            recommendations.append(f"Address {reason['reason']} concerns (Confidence: {reason['confidence']}%)")
            
        return recommendations

    @staticmethod
    def generate_ban_report(username: str) -> Dict:
        """Generate comprehensive ban report"""
        from analyzer import InstagramAccountAnalyzer
        from ban_engine import BanRecommendationEngine
        
        stats = InstagramAccountAnalyzer.get_account_stats(username)
        analysis = BanRecommendationEngine.calculate_ban_probability(stats)
        recommendations = ReportGenerator._generate_recommendations(analysis, stats)
        quick_reports = ReportGenerator.generate_quick_reports(username)

        return {
            'username': username,
            'account_stats': stats,
            'ban_analysis': analysis,
            'recommendations': recommendations,
            'quick_reports': quick_reports,
            'generated_at': datetime.now().isoformat()
        }

    @staticmethod
    def display_report(report: Dict):
        """Display the analysis report in a formatted way"""
        print(f"\n{Color.CYAN}{Color.BOLD}=== ANALYSIS RESULTS ==={Color.END}")
        print(f"Username: {Color.WHITE}@{report['username']}{Color.END}")
        print(f"Ban Probability: {Color.RED}{report['ban_analysis']['ban_probability']}%{Color.END}")
        print(f"Risk Level: {report['ban_analysis']['risk_level']}")
        
        print(f"\n{Color.YELLOW}{Color.BOLD}=== ACCOUNT STATISTICS ==={Color.END}")
        stats = report['account_stats']
        print(f"Followers: {Color.GREEN}{stats['followers']:,}{Color.END}")
        print(f"Following: {Color.BLUE}{stats['following']:,}{Color.END}")
        print(f"Posts: {Color.MAGENTA}{stats['posts']:,}{Color.END}")
        print(f"Engagement Rate: {Color.CYAN}{stats['engagement_rate']:.2f}%{Color.END}")
        
        print(f"\n{Color.YELLOW}{Color.BOLD}=== DETECTED ISSUES ==={Color.END}")
        if report['ban_analysis']['reasons']:
            for reason in report['ban_analysis']['reasons']:
                print(f"{reason['color']}{reason['emoji']} {reason['reason']}: {reason['confidence']}% confidence{Color.END}")
        else:
            print(f"{Color.GREEN}✅ No significant issues detected{Color.END}")
        
        print(f"\n{Color.GREEN}{Color.BOLD}=== RECOMMENDATIONS ==={Color.END}")
        for rec in report['recommendations']:
            print(f"• {rec}")
        
        print(f"\n{Color.MAGENTA}{Color.BOLD}=== QUICK REPORTS ==={Color.END}")
        for quick_report in report['quick_reports']:
            print(f"📋 {quick_report}")
        
        print(f"\n{Color.CYAN}Report generated at: {report['generated_at']}{Color.END}")
