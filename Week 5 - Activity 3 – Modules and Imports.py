#######################################################################
# Week 5 – Activity 3: Modules & Imports
#
# What you're expected to do
# 1) Use the separate module 'week5_utils.py' provided alongside this file.
# 2) Import the module in THREE different ways and use its functions:
#    a) import week5_utils as u       -> u.mean([...])
#    b) from week5_utils import top_n -> top_n([...], n=3)
#    c) from week5_utils import format_currency as money
# 3) Show outputs and add short comments.
#######################################################################

# a) Import the whole module with an alias
import week5_utils as u

values = [12.5, 18.0, 15.75, 9.20, 22.10]
avg = u.mean(values)
print("Mean:", round(avg, 2))  # OUTPUT:

# b) Import a specific function
from week5_utils import top_n

top3 = top_n(values, n=3)
print("Top 3:", top3)  # OUTPUT:

# c) Import with alias
from week5_utils import format_currency as money

print("Formatted total:", money(sum(values)))  # OUTPUT:

# Bonus: slugify usage
from week5_utils import slugify
print("Slug: ", slugify("Business Analytics 101"))  # OUTPUT:
