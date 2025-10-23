import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from retention import cohort_retention, day_n_retention, retention_curve_area, classify_retention

COHORT = ['u1', 'u2', 'u3', 'u4']
EVENTS = [
    {'user_id': 'u1', 'period': 0}, {'user_id': 'u2', 'period': 0},
    {'user_id': 'u3', 'period': 0}, {'user_id': 'u4', 'period': 0},
    {'user_id': 'u1', 'period': 1}, {'user_id': 'u2', 'period': 1},
    {'user_id': 'u1', 'period': 2},
]


def test_cohort_retention_period0():
    curve = cohort_retention(COHORT, EVENTS, periods=3)
    assert curve[0] == 100.0


def test_cohort_retention_period1():
    curve = cohort_retention(COHORT, EVENTS, periods=3)
    assert curve[1] == 50.0


def test_cohort_retention_period2():
    curve = cohort_retention(COHORT, EVENTS, periods=3)
    assert curve[2] == 25.0


def test_day_n_retention():
    assert day_n_retention(COHORT, EVENTS, day=1) == 50.0


def test_curve_area():
    series = [100.0, 50.0, 25.0]
    assert retention_curve_area(series) == pytest.approx(37.5)


def test_classify_retention():
    assert classify_retention(45.0) == 'excellent'
    assert classify_retention(15.0) == 'average'
    assert classify_retention(5.0) == 'poor'


try:
    import pytest
except ImportError:
    pass
