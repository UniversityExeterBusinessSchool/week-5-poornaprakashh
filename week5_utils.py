"""week5_utils.py - Utility functions for Week 5 Activity 3.

Functions
---------
- mean(values): float average of numeric list (raises ValueError if empty)
- top_n(values, n=3): returns a NEW list of the top n values (descending)
- format_currency(amount, symbol="£"): return e.g. "£12.34"
- slugify(text): lowercase, replace spaces with '-', strip surrounding spaces
"""

def mean(values):
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)

def top_n(values, n=3):
    return sorted(values, reverse=True)[:n]

def format_currency(amount, symbol="£"):
    return f"{symbol}{amount:.2f}"

def slugify(text):
    return "-".join(text.strip().lower().split())
