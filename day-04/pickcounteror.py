#Pick ONE: Counter, json, or defaultdict
#Write your first-principles version first
#Write the library version and print True if they agree
from collections import Counter


# 1. First-principles version
def manual_counter(items):
  counts = {}
  for item in items:
    if item in counts:
      counts[item] += 1
    else:
      counts[item] = 1
  return counts


# Sample data
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Run both versions
first_principles_result = manual_counter(words)
library_result = Counter(words)

# 2. Print results and verify they agree
print("First-principles:", first_principles_result)
print("Library version: ", dict(library_result))
print("Do they agree?   ", first_principles_result == library_result)
