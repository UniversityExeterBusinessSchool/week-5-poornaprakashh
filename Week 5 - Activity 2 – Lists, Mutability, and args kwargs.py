#######################################################################
# Week 5 – Activity 2: Lists, Mutability, and *args/**kwargs
#
# What you're expected to do
# 1) Write two functions that add a surcharge to a list of prices:
#    - add_surcharge_inplace(prices, pct): modifies the original list.
#    - add_surcharge_copy(prices, pct): returns a NEW list; original unchanged.
# 2) Demonstrate that one modifies the original, the other doesn't.
# 3) Write a function that accepts *args and **kwargs and returns a summary dict.
#######################################################################

# 1) In-place vs copy

def add_surcharge_inplace(prices, pct):
    """Increase each price by pct% IN PLACE (modifies the list)."""
    for i in range(len(prices)):
        prices[i] = round(prices[i] * (1 + pct/100), 2)

def add_surcharge_copy(prices, pct):
    """Return a NEW list with pct% added; original list is not changed."""
    return [round(p * (1 + pct/100), 2) for p in prices]


original = [10.0, 12.5, 8.0]
copy_before = original[:]  # safeguard snapshot
add_surcharge_inplace(original, 10)
print("After inplace:", original, "(was:", copy_before, ")")  # OUTPUT:

original2 = [10.0, 12.5, 8.0]
result_copy = add_surcharge_copy(original2, 10)
print("Copy result:", result_copy, "Original remains:", original2)  # OUTPUT:


# 2) *args and **kwargs summary function
#    Define register_products(*skus, **metadata) -> dict
#    - skus: any number of product IDs
#    - metadata: arbitrary keyword pairs (e.g., category="peripherals")

def register_products(*skus, **metadata):
    return {
        "count": len(skus),
        "skus": list(skus),
        "meta": dict(metadata)
    }

summary = register_products("SKU-1", "SKU-2", warehouse="A", priority=True)
print(summary)  # OUTPUT:
