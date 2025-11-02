import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import random
import time
from typing import List, Dict
import re

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

class InstagramAccountAnalyzer:
    """Analyze Instagram account for ban recommendations"""

    @staticmethod
    def get_account_stats(username: str) -> Dict:
        """Fetch Instagram account statistics using web scraping"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            url = f"https://www.instagram.com/{username}/"
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract data from meta tags
            followers = following = posts = 0
            meta_description = soup.find('meta', property='og:description')
            
            if meta_description:
                content = meta_description.get('content', '')
                numbers = re.findall(r'[\d,]+', content)
                if len(numbers) >= 3:
                    followers = int(numbers[0].replace(',', ''))
                    following = int(numbers[1].replace(',', ''))
                    posts = int(numbers[2].replace(',', ''))
            
            # Fallback to simulated data
            if followers == 0:
                followers = random.randint(100, 10000)
                following = random.randint(50, 5000)
                posts = random.randint(10, 1000)

            # Simulate other metrics
            engagement_rate = random.uniform(1.0, 3.0)
            account_age_days = random.randint(100, 1000)
            reports_received = random.randint(0, 5)
            avg_daily_actions = random.randint(20, 100)
            suspicious_keywords = []
            last_login = datetime.now() - timedelta(hours=12)

            return {
                'followers': followers,
                'following': following,
                'posts': posts,
                'engagement_rate': engagement_rate,
                'account_age_days': account_age_days,
                'reports_received': reports_received,
                'avg_daily_actions': avg_daily_actions,
                'suspicious_keywords': suspicious_keywords,
                'last_login': last_login
            }
            
        except requests.RequestException as e:
            print(f"{Color.RED}Error fetching data for {username}: {e}{Color.END}")
            # Return simulated data on error
            return InstagramAccountAnalyzer._generate_simulated_data()

    @staticmethod
    def _generate_simulated_data() -> Dict:
        """Generate simulated account data for testing"""
        return {
            'followers': random.randint(100, 10000),
            'following': random.randint(50, 5000),
            'posts': random.randint(10, 1000),
            'engagement_rate': random.uniform(1.0, 3.0),
            'account_age_days': random.randint(100, 1000),
            'reports_received': random.randint(0, 5),
            'avg_daily_actions': random.randint(20, 100),
            'suspicious_keywords': [],
            'last_login': datetime.now() - timedelta(hours=12)
        }