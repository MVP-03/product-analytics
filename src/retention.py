from typing import List, Dict


def cohort_retention(cohort: List[str], events: List[Dict], periods: int = 8) -> List[float]:
    cohort_set  = set(cohort)
    period_seen = [set() for _ in range(periods)]

    for event in events:
        uid = event.get('user_id')
        p   = event.get('period', 0)
        if uid in cohort_set and 0 <= p < periods:
            period_seen[p].add(uid)

    n = len(cohort_set)
    if n == 0:
        return [0.0] * periods

    return [round(len(period_seen[p]) / n * 100, 1) for p in range(periods)]


def day_n_retention(cohort: List[str], events: List[Dict], day: int) -> float:
    series = cohort_retention(cohort, events, periods=day + 1)
    return series[day] if len(series) > day else 0.0


def retention_curve_area(series: List[float]) -> float:
    if len(series) < 2:
        return 0.0
    return round(sum(series[1:]) / (len(series) - 1), 2)


def classify_retention(day30: float) -> str:
    if day30 >= 40:
        return 'excellent'
    if day30 >= 20:
        return 'good'
    if day30 >= 10:
        return 'average'
    return 'poor'
