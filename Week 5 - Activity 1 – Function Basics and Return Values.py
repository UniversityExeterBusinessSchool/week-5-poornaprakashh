#######################################################################
# Week 5 – Activity 1: Function Basics & Return Values
#
# What you're expected to do
# 1) Define a function with a default value and call it using positional and
#    keyword arguments.
# 2) Write a function that returns a DICTIONARY with multiple calculated fields.
# 3) Make one argument optional (with a sensible default).
#
# Paste key outputs as comments using:  # OUTPUT: ...
#######################################################################

# 1) Define a function greet(name, title="") that returns a friendly string.
#    - If title is provided, include it before the name (e.g., "Dr Smith").
#    - Demonstrate calls: greet("Aisha"), greet(name="Ben", title="Mr").

def greet(name, title=""):
    """Return a polite greeting string. If title provided, include it."""
    if title:
        full = f"{title} {name}"
    else:
        full = name
    return f"Hello, {full}!"

print(greet("Aisha"))                 # OUTPUT:
print(greet(name="Ben", title="Mr"))  # OUTPUT:


# 2) Write compute_order_total(prices, tax_rate=0.2, discount_pct=0)
#    - prices: list of item prices (numbers)
#    - tax_rate: default 20%
#    - discount_pct: default 0
#    Return a dict with keys: subtotal, discount, tax, total (all rounded to 2dp)

def compute_order_total(prices, tax_rate=0.2, discount_pct=0):
    subtotal = sum(prices)
    discount = round(subtotal * (discount_pct/100), 2)
    taxable = subtotal - discount
    tax = round(taxable * tax_rate, 2)
    total = round(taxable + tax, 2)
    return {
        "subtotal": round(subtotal, 2),
        "discount": discount,
        "tax": tax,
        "total": total,
    }

basket = [12.99, 8.50, 4.00]
summary = compute_order_total(basket, discount_pct=10)  # keyword arg
print(summary)  # OUTPUT:


# 3) Optional argument example:
#    Define format_name(first, last, middle="")
#    - If middle is provided, include it between first and last.
#    - Return the formatted full name.

def format_name(first, last, middle=""):
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

print(format_name("Sam", "Patel"))             # OUTPUT:
print(format_name("Sam", "Patel", middle="R."))  # OUTPUT:
