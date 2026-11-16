# Practical 8 — Fractional Knapsack (Greedy)

**Aim:** Maximise the profit of a truck with a weight limit, where parcels may be
loaded partially, using the greedy Fractional Knapsack strategy.

**Language:** Python · **Program:** [`fractional_knapsack.py`](fractional_knapsack.py)

---

## Concepts

A **greedy algorithm** builds the answer step by step, always taking the choice
that looks best right now, and never undoing a choice. It is fast and simple, but
it is only correct when the problem has the right structure.

**Problem.** A truck carries at most `W` kg. Each parcel has a weight and a
profit. Any **fraction** of a parcel may be shipped. Maximise the total profit.

**The greedy choice:** profit per kg.

```
ratio = profit / weight
```

Sort parcels by ratio, biggest first, then fill the truck. The last parcel may be
cut in half.

| Parcel | Weight | Profit | Profit per kg | Order |
|---|---|---|---|---|
| D – Medicine | 5 | 90 | 18.0 | 1st |
| A – Books | 10 | 60 | 6.0 | 2nd |
| E – Furniture | 25 | 150 | 6.0 | 3rd |
| B – Electronics | 20 | 100 | 5.0 | 4th |
| C – Clothes | 30 | 120 | 4.0 | 5th |

**Why the ratio is the right key.** If parcel A pays more per kg than parcel B,
then every kg given to B could be given to A instead for at least as much money.
So in an optimal answer the space is filled in decreasing ratio order. This
argument is called an *exchange argument*.

## Fractional vs 0/1 knapsack

| | Fractional | 0/1 |
|---|---|---|
| Split a parcel? | yes | no — take it whole or leave it |
| Method | greedy by ratio | dynamic programming |
| Greedy correct? | yes | no |

Counter-example for 0/1: capacity 10, items `(6 kg, Rs 6)`, `(5 kg, Rs 5)`,
`(5 kg, Rs 5)`. Greedy by ratio takes the 6 kg item and earns 6, but the best
answer is 10.

## Complexity

Sorting the `n` parcels takes `O(n log n)`; the filling loop is one pass,
`O(n)`. Total **O(n log n)** time, **O(n)** space for the sorted list.

## Exam points

- Sort by profit/weight — not by profit, not by weight.
- Greedy is locally best; here it also happens to be globally best.
- Greedy fails for 0/1 knapsack — that is why dynamic programming exists.
- Used in resource allocation: bandwidth, fuel, cargo, budget planning.
