from typing import Dict, List
import random
from .analyzer import Color

class BanRecommendationEngine:
    """Generate ban recommendations based on account analysis"""

    BAN_REASONS = {
        'spam_behavior': {
            'name': 'Spam Behavior',
            'thresholds': {'following_ratio': 10, 'daily_actions': 200, 'engagement_rate': 0.5},
            'weight': 0.8,
            'emoji': '📢',
            'color': Color.YELLOW
        },
        'fake_engagement': {
            'name': 'Fake Engagement',
            'thresholds': {'engagement_rate': 0.8, 'followers_growth': 1000},
            'weight': 0.7,
            'emoji': '🤖',
            'color': Color.CYAN
        },
        'inappropriate_content': {
            'name': 'Inappropriate Content',
            'thresholds': {'reports_received': 5},
            'weight': 0.9,
            'emoji': '🚫',
            'color': Color.RED
        },
        'mass_following': {
            'name': 'Mass Following',
            'thresholds': {'following_ratio': 5, 'daily_actions': 150},
            'weight': 0.6,
            'emoji': '👥',
            'color': Color.ORANGE
        },
        'suspicious_activity': {
            'name': 'Suspicious Activity',
            'thresholds': {'avg_daily_actions': 100, 'account_age_days': 30},
            'weight': 0.5,
            'emoji': '🔍',
            'color': Color.PURPLE
        },
        'impersonation': {
            'name': 'Impersonation',
            'thresholds': {'reports_received': 3},
            'weight': 0.85,
            'emoji': '🎭',
            'color': Color.PINK
        },
        'bullying': {
            'name': 'Bullying',
            'thresholds': {'reports_received': 7},
            'weight': 0.85,
            'emoji': '😢',
            'color': Color.MAGENTA
        }
    }

    @staticmethod
    def calculate_ban_probability(stats: Dict) -> Dict:
        """Calculate ban probability and reasons"""
        score = 0.0
        max_score = 0.0
        reasons = []

        following_ratio = stats['following'] / max(stats['followers'], 1)

        for reason_id, reason_data in BanRecommendationEngine.BAN_REASONS.items():
            max_score += reason_data['weight']
            reason_score = 0.0

            # Check each threshold for this reason
            thresholds = reason_data['thresholds']
            
            if 'following_ratio' in thresholds and following_ratio > thresholds['following_ratio']:
                reason_score += 0.3
                
            if 'daily_actions' in thresholds and stats['avg_daily_actions'] > thresholds['daily_actions']:
                reason_score += 0.3
                
            if 'engagement_rate' in thresholds and stats['engagement_rate'] < thresholds['engagement_rate']:
                reason_score += 0.2
                
            if 'reports_received' in thresholds and stats['reports_received'] >= thresholds['reports_received']:
                reason_score += min(0.4, stats['reports_received'] * 0.1)
                
            if 'account_age_days' in thresholds and stats['account_age_days'] < thresholds['account_age_days']:
                reason_score += 0.2

            if reason_score > 0:
                score += reason_score * reason_data['weight']
                reasons.append({
                    'reason': reason_data['name'],
                    'confidence': round(reason_score * 100),
                    'weight': reason_data['weight'],
                    'emoji': reason_data['emoji'],
                    'color': reason_data['color']
                })

        ban_probability = min(round((score / max_score) * 100), 100) if max_score > 0 else 0

        return {
            'ban_probability': ban_probability,
            'reasons': sorted(reasons, key=lambda x: x['confidence'], reverse=True),
            'risk_level': BanRecommendationEngine._get_risk_level(ban_probability)
        }

    @staticmethod
    def _get_risk_level(probability: int) -> str:
        if probability >= 80:
            return f"{Color.RED}{Color.BOLD}CRITICAL{Color.END}"
        elif probability >= 60:
            return f"{Color.ORANGE}{Color.BOLD}HIGH{Color.END}"
        elif probability >= 40:
            return f"{Color.YELLOW}{Color.BOLD}MEDIUM{Color.END}"
        elif probability >= 20:
            return f"{Color.BLUE}{Color.BOLD}LOW{Color.END}"
        else:
            return f"{Color.GREEN}{Color.BOLD}MINIMAL{Color.END}"