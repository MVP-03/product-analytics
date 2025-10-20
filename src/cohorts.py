from typing import List, Dict
from collections import defaultdict


def build_cohorts(users: List[Dict], period_key: str = 'signup_month') -> Dict[str, List[str]]:
    cohorts: Dict[str, List[str]] = defaultdict(list)
    for user in users:
        period = user.get(period_key, 'unknown')
        uid    = user.get('user_id')
        if uid:
            cohorts[period].append(uid)
    return dict(cohorts)


def cohort_sizes(cohorts: Dict[str, List[str]]) -> Dict[str, int]:
    return {period: len(users) for period, users in cohorts.items()}


def avg_cohort_size(cohorts: Dict[str, List[str]]) -> float:
    sizes = list(cohort_sizes(cohorts).values())
    if not sizes:
        return 0.0
    return round(sum(sizes) / len(sizes), 1)


def largest_cohort(cohorts: Dict[str, List[str]]) -> str:
    if not cohorts:
        return ''
    return max(cohorts.items(), key=lambda x: len(x[1]))[0]
