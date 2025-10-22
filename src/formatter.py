from typing import List, Dict


def format_retention_curve(series: List[float], label: str = 'Retention') -> str:
    lines = [f'{label} Curve', '-' * 36]
    for i, rate in enumerate(series):
        bar = '█' * int(rate / 5)
        lines.append(f'Period {i:>2}: {rate:>5.1f}%  {bar}')
    return '\n'.join(lines)


def format_funnel(steps: List[Dict]) -> str:
    lines = [f"{'Step':<24} {'Count':>8}  {'CVR':>7}  {'Drop':>7}", '-' * 52]
    for step in steps:
        cvr  = step.get('conversion_from_prev', 0)
        drop = step.get('drop_off', 0)
        lines.append(
            f"{step.get('name', 'Step'):<24} {step['count']:>8}  "
            f"{cvr:>6.1f}%  {drop:>6.1f}%"
        )
    return '\n'.join(lines)


def format_cohort_table(sizes: Dict[str, int]) -> str:
    lines = [f"{'Cohort':<15}  {'Users':>6}", '-' * 24]
    for period, count in sorted(sizes.items()):
        lines.append(f'{period:<15}  {count:>6}')
    return '\n'.join(lines)
