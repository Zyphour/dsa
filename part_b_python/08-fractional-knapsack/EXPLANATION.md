# Code explanation — `fractional_knapsack.py`

Data and capacity at the top:

```python
PARCELS = [("Parcel D - Medicine", 5, 90), ...]   # (name, weight, profit)
CAPACITY = 50
```

## What each function does

| Function | Job |
|---|---|
| `fractional_knapsack(parcels, capacity, show_steps)` | build items with ratios, sort, fill, return the plan, profit and weight used |
| `main()` | prints the parcel table, the sorted ratio table, the take-steps and the final plan |

## The core loop

```python
items.sort(key=lambda item: item["ratio"], reverse=True)

for it in items:
    if capacity == 0:
        break

    if it["weight"] <= capacity:            # whole parcel fits
        fraction = 1.0
        capacity -= it["weight"]
        total_profit += it["profit"]

    else:                                   # only part of it fits
        fraction = capacity / it["weight"]
        total_profit += it["profit"] * fraction
        capacity = 0
```

Three things happen for every parcel: decide the fraction, add
`profit × fraction`, and reduce the remaining capacity.

## Dry run (capacity 50 kg)

| Parcel | Weight | Profit | Ratio | Decision | Profit so far | Capacity left |
|---|---|---|---|---|---|---|
| D – Medicine | 5 | 90 | 18.0 | take all 5 kg | 90 | 45 |
| A – Books | 10 | 60 | 6.0 | take all 10 kg | 150 | 35 |
| E – Furniture | 25 | 150 | 6.0 | take all 25 kg | 300 | 10 |
| B – Electronics | 20 | 100 | 5.0 | take **50 %** = 10 kg | 350 | 0 |
| C – Clothes | 30 | 120 | 4.0 | skip (truck full) | 350 | 0 |

**Result: 50/50 kg used, maximum profit Rs 350.**

## Common mistakes

- Sorting by profit only (medicine wins, but ratio is what matters here).
- Sorting by weight only (light parcels are not automatically the most profitable).
- Forgetting `capacity -= weight`, so the truck seems never to fill.
- Adding the full profit instead of `profit * fraction` for the split parcel.
- Using this greedy method for 0/1 knapsack, where it is simply wrong.

## Viva — short answers

| Question | Answer |
|---|---|
| What is a greedy algorithm? | Take the best local choice at each step and never undo it. |
| Why profit/weight? | Each kg of capacity should earn as much as possible. |
| Is greedy always optimal? | No — works here, for MST, Huffman, activity selection; fails for 0/1 knapsack. |
| Complexity? | O(n log n) for the sort + O(n) scan = O(n log n). |
| Which parcel is split and why? | Electronics — all 10 remaining kg are filled from it. |
