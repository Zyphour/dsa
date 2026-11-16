# Student Guide — `fractional_knapsack.py`

This guide explains how [`fractional_knapsack.py`](fractional_knapsack.py) works and prepares you for viva questions.

## How the Code Works

```python
def knapsack(items, cap):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    profit = 0
    for p, w in items:
        take = min(w, cap)
        profit += take * p/w
        cap -= take
        if cap == 0: break
    return profit
```
- `items` is a list of tuples `(profit, weight)`: `x[0]` is profit, `x[1]` is weight.
- `items.sort(key=lambda x: x[0]/x[1], reverse=True)` sorts items from highest `profit / weight` value-density to lowest.
- `take = min(w, cap)` handles both whole and fractional picks cleanly in one line:
  - When enough room is left (`w <= cap`), `take = w`, so `take * p/w` equals full profit `p`.
  - When less room is left (`cap < w`), `take = cap`, so `take * p/w` adds the exact fraction `(cap / w) * p` and reduces `cap` to `0`, triggering `break`.

## Dry Run — `items = [(60, 10), (100, 20), (120, 30)]`, `cap = 50`

1. Ratios:
   - `(60, 10)` → `60 / 10 = 6.0`
   - `(100, 20)` → `100 / 20 = 5.0`
   - `(120, 30)` → `120 / 30 = 4.0`
2. Greedy picks:
   - Take all `10` of `(60, 10)`: `profit = 60.0`, `cap = 40`
   - Take all `20` of `(100, 20)`: `profit = 160.0`, `cap = 20`
   - Take `20` out of `30` (`2/3`) of `(120, 30)`: `profit = 160.0 + 20 * 4.0 = 240.0`, `cap = 0` → stop.

Output: `240.0`

## Common Mistakes

- Sorting by raw profit (`x[0]`) or raw weight (`x[1]`) instead of the ratio `x[0] / x[1]`. (If you picked `(120, 30)` + `(100, 20)` first, you'd only get `220` instead of `240`!)
- Forgetting `reverse=True` (that picks the *worst* ratio items first!).

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| Why do we sort by `profit / weight` instead of just `profit`? | Capacity is limited by weight, so we want the highest profit per unit of weight. |
| Does the greedy method always give the optimal answer for Fractional Knapsack? | Yes! |
| Would this greedy method work for 0/1 Knapsack (items cannot be split)? | No — 0/1 Knapsack requires Dynamic Programming (or backtracking) because greedy can leave unused space or pick suboptimal combinations. |
| What is the time complexity? | `O(n log n)` due to sorting. |
