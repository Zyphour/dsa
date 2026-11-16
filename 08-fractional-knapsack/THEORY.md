# Practical 8 — Fractional Knapsack (Greedy)

**Aim:** Maximize total profit inside a capacity-constrained knapsack using the
greedy profit-to-weight ratio approach.

**Language:** Python · **Program:** [`fractional_knapsack.py`](fractional_knapsack.py)

---

## Concepts

- **Fractional Knapsack** – given `(profit, weight)` items and capacity `cap`,
  items **can be split** into fractions (unlike 0/1 Knapsack).
- **Greedy choice** – always take as much as possible of the item with the
  highest **profit per unit weight** (`profit / weight`).

## Algorithm

1. Sort `items` in descending order of `profit / weight`.
2. Set `profit = 0`.
3. For each `(p, w)` in sorted `items`:
   - `take = min(w, cap)`
   - `profit += take * (p / w)`
   - `cap -= take`
   - If `cap == 0`, stop.
4. Return `profit`.

## Comparison

| | Fractional Knapsack | 0/1 Knapsack |
|---|---|---|
| Can split items? | Yes | No (all or nothing) |
| Greedy optimal? | **Yes** | **No** (needs DP) |
| Time | O(n log n) | O(n · W) via DP |

## Exam points

- Sorting by `profit` alone or `weight` alone fails; sorting by `profit / weight`
  is always optimal for Fractional Knapsack.
- Time complexity is **O(n log n)** due to sorting; extra space is **O(1)**.
- Demo input `[(60,10), (100,20), (120,30)]` with `cap = 50` gives **240.0**.
