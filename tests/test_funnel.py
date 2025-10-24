import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from funnel import funnel_conversion, overall_conversion, biggest_drop_off, funnel_health

STEPS = [
    {'name': 'Visit',    'count': 10000},
    {'name': 'Sign up',  'count': 2000},
    {'name': 'Activate', 'count': 800},
    {'name': 'Purchase', 'count': 200},
]


def test_overall_conversion():
    assert overall_conversion(STEPS) == 2.0


def test_funnel_conversion_first_step():
    result = funnel_conversion(STEPS)
    assert result[0]['drop_off'] == 0.0


def test_funnel_conversion_second_step():
    result = funnel_conversion(STEPS)
    assert result[1]['conversion_from_prev'] == 20.0


def test_biggest_drop_off():
    step = biggest_drop_off(STEPS)
    assert step['name'] == 'Sign up'


def test_funnel_health_critical():
    assert funnel_health(1.0) == 'critical'


def test_funnel_health_healthy():
    assert funnel_health(6.0) == 'healthy'
