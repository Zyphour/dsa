"""
EXPERIMENT 7 : Divide and Conquer - Merge Sort on Online Orders
---------------------------------------------------------------
Part B - Python

Problem: an online store has many orders, each with an estimated delivery
time in minutes. Sort the orders so that the quickest deliveries are
handled first.

Why Merge Sort?
    It is the classic DIVIDE AND CONQUER algorithm:
        DIVIDE   : split the list into two halves
        CONQUER  : sort each half recursively (same function, smaller input)
        COMBINE  : merge the two sorted halves into one sorted list

    Time  : O(n log n) always (best, average and worst case)
    Space : O(n) extra, because merging needs a temporary list
    Stable: yes -> orders with the same delivery time keep their
            original order, which is fair for customers.

Run: python3 merge_sort_orders.py
"""

import random

# ----------------------------------------------------------------------
# sample data: (order_id, item, delivery time in minutes)
# ----------------------------------------------------------------------
ORDERS = [
    {"id": "ORD-101", "item": "Laptop Bag",     "minutes": 45},
    {"id": "ORD-102", "item": "Notebook",       "minutes": 20},
    {"id": "ORD-103", "item": "Headphones",     "minutes": 90},
    {"id": "ORD-104", "item": "Water Bottle",   "minutes": 15},
    {"id": "ORD-105", "item": "Phone Charger",  "minutes": 30},
    {"id": "ORD-106", "item": "Shoes",          "minutes": 120},
    {"id": "ORD-107", "item": "T-Shirt",        "minutes": 25},
    {"id": "ORD-108", "item": "Rice 5kg",       "minutes": 60},
    {"id": "ORD-109", "item": "Dumbbells",      "minutes": 150},
    {"id": "ORD-110", "item": "Coffee Mug",     "minutes": 10},
    {"id": "ORD-111", "item": "Desk Lamp",      "minutes": 35},
    {"id": "ORD-112", "item": "Backpack",       "minutes": 75},
]

comparisons = 0          # simple counter so we can "measure" the work done


# ----------------------------------------------------------------------
# MERGE SORT
# ----------------------------------------------------------------------
def merge_sort(orders):
    """
    Returns a new sorted list (ascending delivery time).
    Splitting a list this way keeps the code short and easy to read.
    """
    global comparisons

    if len(orders) <= 1:                  # base case: 0 or 1 item is sorted
        return orders

    middle = len(orders) // 2             # DIVIDE
    left = merge_sort(orders[:middle])
    right = merge_sort(orders[middle:])

    return merge(left, right)             # COMBINE


def merge(left, right):
    """Join two sorted lists into one sorted list."""
    global comparisons

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i]["minutes"] <= right[j]["minutes"]:
            result.append(left[i])        # '<=' keeps equal items in order
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])               # whatever is left over is already sorted
    result.extend(right[j:])
    return result


# ----------------------------------------------------------------------
# helpers for printing
# ----------------------------------------------------------------------
def show(orders, title):
    print(f"\n{title}")
    print(f"{'ORDER ID':<10}{'ITEM':<18}{'DELIVERY':>10}")
    print("-" * 38)
    for o in orders:
        print(f"{o['id']:<10}{o['item']:<18}{o['minutes']:>8} min")


if __name__ == "__main__":
    show(ORDERS, "1) ORDERS AS THEY ARRIVED (unsorted)")

    comparisons = 0
    sorted_orders = merge_sort(ORDERS)
    show(sorted_orders, "2) AFTER MERGE SORT (quickest first)")

    print(f"\nComparisons made while sorting: {comparisons}")
    print("For n = 12, n log2 n is about 12 x 3.6 = 43, and O(n log n) tells us")
    print("the real number stays close to that even when n becomes very large.")

    # the original list must not be destroyed
    print("\nOriginal list still unsorted (merge sort worked on copies):",
          [o["minutes"] for o in ORDERS])

    # ---- quick proof that it really sorts ----
    print("\n--- Self-check on random data ---")
    ok = True
    for size in range(0, 80):
        data = [{"id": str(i), "item": "x", "minutes": random.randint(0, 500)}
                for i in range(size)]
        got = [o["minutes"] for o in merge_sort(data)]
        if got != sorted(got):
            ok = False
            print("FAILED at size", size)
            break
    if ok:
        print("80 random order lists sorted correctly.")

    print("\n--- Why divide and conquer is fast ---")
    print("n = 16 -> 16 + 16 + ... work at each of log2(16) = 4 levels")
    print("So work = n x log2(n) instead of n x n for bubble sort.")
