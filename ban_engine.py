from typing import Dict, List
import random
from datetime import datetime

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

class BanRecommendationEngine:
    """Advanced ban recommendation engine for Instagram accounts"""

    BAN_REASONS = {
        'spam_behavior': {
            'name': 'Spam Behavior',
            'thresholds': {
                'following_ratio': 2.0,
                'daily_actions': 150,
                'posts_per_day': 5.0
            },
            'weight': 0.8,
            'emoji': '📢',
            'color': Color.YELLOW,
            'private_adjustment': -0.1
        },
        'fake_engagement': {
            'name': 'Fake Engagement',
            'thresholds': {
                'engagement_rate': 0.8,
                'follower_ratio': 0.01
            },
            'weight': 0.7,
            'emoji': '🤖',
            'color': Color.CYAN,
            'private_adjustment': -0.05
        },
        'inappropriate_content': {
            'name': 'Inappropriate Content',
            'thresholds': {
                'reports_received': 3,
                'suspicious_keywords_count': 2
            },
            'weight': 0.9,
            'emoji': '🚫',
            'color': Color.RED,
            'private_adjustment': 0.0
        },
        'mass_following': {
            'name': 'Mass Following',
            'thresholds': {
                'following_ratio': 5.0,
                'daily_actions': 100
            },
            'weight': 0.6,
            'emoji': '👥',
            'color': Color.ORANGE,
            'private_adjustment': -0.1
        },
        'suspicious_activity': {
            'name': 'Suspicious Activity',
            'thresholds': {
                'account_age_days': 30,
                'posts_per_day': 10.0
            },
            'weight': 0.5,
            'emoji': '🔍',
            'color': Color.PURPLE,
            'private_adjustment': -0.05
        },
        'impersonation': {
            'name': 'Impersonation',
            'thresholds': {
                'reports_received': 2,
                'is_verified': False
            },
            'weight': 0.85,
            'emoji': '🎭',
            'color': Color.PINK,
            'private_adjustment': 0.0
        },
        'bullying_harassment': {
            'name': 'Bullying/Harassment',
            'thresholds': {
                'reports_received': 4
            },
            'weight': 0.9,
            'emoji': '😢',
            'color': Color.MAGENTA,
            'private_adjustment': 0.0
        },
        'commercial_spam': {
            'name': 'Commercial Spam',
            'thresholds': {
                'suspicious_keywords_count': 3,
                'external_url': True
            },
            'weight': 0.7,
            'emoji': '💼',
            'color': Color.ORANGE,
            'private_adjustment': -0.05
        }
    }

    @staticmethod
    def calculate_ban_probability(stats: Dict) -> Dict:
        """Calculate comprehensive ban probability"""
        score = 0.0
        max_score = 0.0
        reasons = []
        
        is_private = stats.get('is_private', False)
        follower_ratio = stats.get('follower_ratio', stats['following'] / max(stats['followers'], 1))
        posts_per_day = stats.get('posts_per_day', stats['posts'] / max(stats['account_age_days'], 1))
        suspicious_keywords_count = len(stats.get('suspicious_keywords', []))

        for reason_id, reason_data in BanRecommendationEngine.BAN_REASONS.items():
            max_score += reason_data['weight']
            reason_score = 0.0
            thresholds = reason_data['thresholds']

            # Check each threshold
            if 'following_ratio' in thresholds and follower_ratio > thresholds['following_ratio']:
                reason_score += 0.3
                
            if 'daily_actions' in thresholds and stats['avg_daily_actions'] > thresholds['daily_actions']:
                reason_score += 0.3
                
            if 'engagement_rate' in thresholds and stats['engagement_rate'] < thresholds['engagement_rate']:
                reason_score += 0.2
                
            if 'reports_received' in thresholds and stats['reports_received'] >= thresholds['reports_received']:
                reason_score += min(0.4, stats['reports_received'] * 0.15)
                
            if 'account_age_days' in thresholds and stats['account_age_days'] < thresholds['account_age_days']:
                reason_score += 0.2
                
            if 'posts_per_day' in thresholds and posts_per_day > thresholds['posts_per_day']:
                reason_score += 0.2
                
            if 'suspicious_keywords_count' in thresholds and suspicious_keywords_count >= thresholds['suspicious_keywords_count']:
                reason_score += min(0.3, suspicious_keywords_count * 0.1)
                
            if 'follower_ratio' in thresholds and follower_ratio < thresholds['follower_ratio']:
                reason_score += 0.2
                
            if 'is_verified' in thresholds and stats.get('is_verified', True) == thresholds['is_verified']:
                reason_score += 0.1
                
            if 'external_url' in thresholds and stats.get('external_url') and thresholds['external_url']:
                reason_score += 0.1

            # Apply private account adjustment
            if is_private:
                reason_score = max(0, reason_score + reason_data['private_adjustment'])

            if reason_score > 0:
                final_score = reason_score * reason_data['weight']
                score += final_score
                reasons.append({
                    'reason': reason_data['name'],
                    'confidence': min(round(reason_score * 100), 95),
                    'weight': reason_data['weight'],
                    'emoji': reason_data['emoji'],
                    'color': reason_data['color'],
                    'score': round(final_score, 2)
                })

        # Calculate base probability
        ban_probability = min(round((score / max_score) * 100), 95) if max_score > 0 else 0
        
        # Adjust for account age (older accounts are less likely to be banned)
        if stats['account_age_days'] > 365:
            ban_probability = max(0, ban_probability - 10)
        elif stats['account_age_days'] > 730:
            ban_probability = max(0, ban_probability - 15)

        # Adjust for verified accounts
        if stats.get('is_verified', False):
            ban_probability = max(0, ban_probability - 20)

        return {
            'ban_probability': max(5, ban_probability),  # Minimum 5% probability
            'reasons': sorted(reasons, key=lambda x: x['confidence'], reverse=True),
            'risk_level': BanRecommendationEngine._get_risk_level(ban_probability),
            'score_breakdown': round(score, 2),
            'max_possible_score': round(max_score, 2)
        }

    @staticmethod
    def _get_risk_level(probability: int) -> str:
        """Get risk level with color coding"""
        if probability >= 80:
            return f"{Color.RED}{Color.BOLD}CRITICAL RISK{Color.END}"
        elif probability >= 60:
            return f"{Color.ORANGE}{Color.BOLD}HIGH RISK{Color.END}"
        elif probability >= 40:
            return f"{Color.YELLOW}{Color.BOLD}MEDIUM RISK{Color.END}"
        elif probability >= 20:
            return f"{Color.BLUE}{Color.BOLD}LOW RISK{Color.END}"
        else:
            return f"{Color.GREEN}{Color.BOLD}MINIMAL RISK{Color.END}"

    @staticmethod
    def generate_quick_reports(analysis: Dict, username: str) -> List[str]:
        """Generate quick report templates"""
        reports = []
        top_reasons = analysis['reasons'][:3]
        
        report_templates = [
            "Reporting @{username} for {reason} - detected multiple violations of community guidelines",
            "Flagging @{username} account for {reason} - engaging in suspicious activities",
            "Reporting @{username} for {reason} - this account appears to be violating platform rules",
            "Flagging @{username} for {reason} - potential spam/fake account behavior detected"
        ]
        
        for reason in top_reasons:
            template = random.choice(report_templates)
            reports.append(template.format(username=username, reason=reason['reason'].lower()))
            
        return reports[:3]

    @staticmethod
    def get_recommendations(analysis: Dict, stats: Dict) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        probability = analysis['ban_probability']
        
        if probability >= 80:
            recommendations.extend([
                "🚨 IMMEDIATE ACTION: Consider reporting this account to Instagram",
                "🔒 High likelihood of violations - monitor account activity closely",
                "📋 Document any suspicious content for evidence"
            ])
        elif probability >= 60:
            recommendations.extend([
                "⚠️ High risk account - exercise caution when interacting",
                "🔍 Monitor for further suspicious activity",
                "Consider limiting engagement with this account"
            ])
        elif probability >= 40:
            recommendations.extend([
                "📊 Moderate risk - account shows some suspicious patterns",
                "👀 Keep an eye on account activity",
                "Verify account authenticity before engaging"
            ])
        else:
            recommendations.append("✅ Account appears normal - continue monitoring as needed")

        # Add specific recommendations based on reasons
        for reason in analysis['reasons'][:2]:
            if 'Spam' in reason['reason']:
                recommendations.append(f"Address {reason['reason']} patterns (Confidence: {reason['confidence']}%)")
            elif 'Fake' in reason['reason']:
                recommendations.append(f"Verify authentic engagement (Confidence: {reason['confidence']}%)")

        return recommendations
