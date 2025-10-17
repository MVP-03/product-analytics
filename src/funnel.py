from typing import List, Dict


def funnel_conversion(steps: List[Dict]) -> List[Dict]:
    result = []
    for i, step in enumerate(steps):
        prev_count = steps[i - 1]['count'] if i > 0 else step['count']
        cvr = round(step['count'] / prev_count * 100, 1) if prev_count else 0.0
        result.append({
            **step,
            'conversion_from_prev': cvr,
            'drop_off':             round(100 - cvr, 1) if i > 0 else 0.0,
        })
    return result


def overall_conversion(steps: List[Dict]) -> float:
    if not steps or steps[0]['count'] == 0:
        return 0.0
    return round(steps[-1]['count'] / steps[0]['count'] * 100, 2)


def biggest_drop_off(steps: List[Dict]) -> Dict:
    annotated = funnel_conversion(steps)
    return max(annotated[1:], key=lambda s: s['drop_off'], default={})


def funnel_health(overall_cvr: float) -> str:
    if overall_cvr >= 5:
        return 'healthy'
    if overall_cvr >= 2:
        return 'needs_improvement'
    return 'critical'
