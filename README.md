# product-analytics

A Python library for core product analytics primitives: **cohort retention**, **funnel analysis**, and **cohort segmentation**. Designed to work with raw event data — no analytics platform required.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-pytest-orange)

---

## Features

- **Cohort retention curves** — D1 / D7 / D30 retention for any user cohort
- **Funnel analysis** — step-by-step conversion rates and drop-off detection
- **Cohort builder** — segment users by signup month, plan, or any attribute
- **Retention classification** — excellent / good / average / poor benchmarks
- **Funnel health scoring** — surface critical drop-off points automatically
- **Text formatters** — retention curves, funnel tables, cohort size charts

---

## Installation

```bash
git clone https://github.com/MVP-03/product-analytics.git
cd product-analytics
python -m venv .venv && source .venv/bin/activate
pip install pytest
```

---

## Quick Start

### Cohort Retention

```python
from src.retention import cohort_retention, day_n_retention, classify_retention

# Define your cohort (e.g. users who signed up in Jan 2026)
cohort = ["u001", "u002", "u003", "u004", "u005"]

# Events: {user_id, period} where period=0 is signup day
events = [
    {"user_id": "u001", "period": 0}, {"user_id": "u002", "period": 0},
    {"user_id": "u003", "period": 0}, {"user_id": "u004", "period": 0},
    {"user_id": "u005", "period": 0},
    {"user_id": "u001", "period": 7}, {"user_id": "u002", "period": 7},
    {"user_id": "u001", "period": 30},
]

curve = cohort_retention(cohort, events, periods=31)
print(f"D1  retention: {curve[1]:.1f}%")
print(f"D7  retention: {curve[7]:.1f}%")
print(f"D30 retention: {curve[30]:.1f}%")
print(f"Health: {classify_retention(curve[30])}")
```

**Output**
```
D1  retention: 0.0%
D7  retention: 40.0%
D30 retention: 20.0%
Health: good
```

### Funnel Analysis

```python
from src.funnel import funnel_conversion, overall_conversion, biggest_drop_off
from src.formatter import format_funnel

steps = [
    {"name": "Visit",    "count": 10000},
    {"name": "Sign up",  "count": 1800},
    {"name": "Activate", "count": 720},
    {"name": "Purchase", "count": 180},
]

annotated = funnel_conversion(steps)
print(format_funnel(annotated))

drop = biggest_drop_off(steps)
print(f"\nBiggest drop-off: {drop['name']} ({drop['drop_off']:.1f}% lost)")
print(f"Overall conversion: {overall_conversion(steps):.2f}%")
```

**Output**
```
Step                     Count    CVR      Drop
----------------------------------------------------
Visit                    10000    0.0%    0.0%
Sign up                   1800   18.0%   82.0%
Activate                   720   40.0%   60.0%
Purchase                   180   25.0%   75.0%

Biggest drop-off: Sign up (82.0% lost)
Overall conversion: 1.80%
```

---

## Retention Benchmarks

| D30 Retention | Classification |
|---|---|
| >= 40% | Excellent |
| >= 20% | Good |
| >= 10% | Average |
| < 10% | Poor |

---

## Project Structure

```
product-analytics/
├── src/
│   ├── retention.py   # cohort retention curves and classification
│   ├── funnel.py      # step-by-step conversion and drop-off analysis
│   ├── cohorts.py     # cohort builder and size aggregation
│   └── formatter.py   # retention curves, funnel tables, cohort charts
├── tests/
│   ├── test_retention.py
│   └── test_funnel.py
└── data/
    └── events.json
```

---

## API Reference

### `retention.py`
| Function | Description |
|---|---|
| `cohort_retention(cohort, events, periods)` | Returns retention % for each period |
| `day_n_retention(cohort, events, day)` | Retention at a specific day |
| `retention_curve_area(series)` | AUC of the retention curve (quality signal) |
| `classify_retention(day30)` | Returns `excellent` / `good` / `average` / `poor` |

### `funnel.py`
| Function | Description |
|---|---|
| `funnel_conversion(steps)` | Annotates each step with CVR and drop-off |
| `overall_conversion(steps)` | Top-to-bottom conversion % |
| `biggest_drop_off(steps)` | Returns the step with the highest drop-off |
| `funnel_health(overall_cvr)` | Returns `healthy` / `needs_improvement` / `critical` |

---

## Running Tests

```bash
python -m pytest tests/ -v
```

---

## License

MIT
