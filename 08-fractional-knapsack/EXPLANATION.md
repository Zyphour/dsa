# Practical 8: Fractional Knapsack (Greedy) — Complete Reference & Code Guide (`fractional_knapsack.py`)

> **Aim:** Maximize total profit inside a capacity-constrained knapsack using the greedy profit-to-weight ratio approach.
>
> **Language:** Python · **Program:** [`fractional_knapsack.py`](fractional_knapsack.py) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`fractional_knapsack.py`](fractional_knapsack.py) solves the **Fractional Knapsack Problem** for 3 items `[(60, 10), (100, 20), (120, 30)]` (each tuple is `(profit, weight)`) and a knapsack weight limit `cap = 50`:
1. Sorts the items in **descending order of their profit-to-weight ratio (`profit / weight`)**.
2. Iterates through the sorted items, taking either the **entire item** (`w`) if it fits inside remaining capacity `cap`, or the **exact fraction** (`cap / w`) that fills the remaining space (`take = min(w, cap)`).
3. Accumulates and prints the **maximum achievable total profit** (`240.0`).

### Exact Program Output
```text
240.0
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Full Form & Definition |
|---|---|
| **Knapsack Problem** | A classic combinatorial optimization problem: given items with `(profit, weight)` and a maximum bag capacity `W`, select items to **maximize total profit** without exceeding total weight `W`. |
| **Fractional Knapsack** | Variant of the Knapsack Problem where **items are divisible** — any fraction `0 <= x <= 1` of an item can be taken, earning proportional profit `x * profit`. |
| **0/1 Knapsack** | Variant where items are **indivisible** (`x ∈ {0, 1}` — either take the whole item `1` or leave it `0`). |
| **Greedy Algorithm** | An algorithmic paradigm that builds a solution step by step by always selecting the **locally optimal choice** at each stage without backtracking. |
| **Profit-to-Weight Ratio (`p / w`)** | Profit earned **per 1 unit of weight** (value density) — the exact greedy selection criterion for Fractional Knapsack. |
| **Greedy-Choice Property** | Property stating that a globally optimal solution can always be reached by making locally greedy choices (`highest p / w` first). |
| **Optimal Substructure** | Property stating that after picking `take` units of an item, the remaining problem (capacity `cap - take` on remaining items) also requires an optimal solution. |
| **DP** | **Full Form:** *Dynamic Programming* — the tabular technique required to solve **0/1 Knapsack** (`O(n · W)`), since Greedy does NOT work on 0/1 Knapsack. |

---

## 3. Core Facts, Rules, Comparison & Uses

### Key Exam Facts
1. **Why Sort by `profit / weight` (NOT `profit` alone or `weight` alone):**
   - Sorting by raw `profit` (`(120,30)` + `(100,20)`) gives `220.0` instead of optimal **`240.0`**.
   - Sorting by **`profit / weight` descending** maximizes profit gained per unit of scarce capacity and is **100% optimal** for Fractional Knapsack.
2. **Why Greedy FAILS on 0/1 Knapsack (Same Input Counterexample!):**
   - On `[(60,10), (100,20), (120,30)]` with `cap = 50` in **0/1 Knapsack** (no splitting allowed), ratio greedy picks `(60,10)` + `(100,20)` = `160` (`30` weight used, `20` wasted because `(120,30)` doesn't fit whole!), whereas optimal 0/1 takes `(100,20)` + `(120,30)` = **`220`**!
3. **Number of Fractional Items:** An optimal Fractional Knapsack solution splits **at most 1 item** (the boundary item that reduces `cap` to `0`).

### Comparison: Fractional Knapsack vs. 0/1 Knapsack

| Parameter | Fractional Knapsack | 0/1 Knapsack |
|---|---|---|
| **Can items be divided into fractions?** | **Yes (`0 <= x <= 1`)** | **No (`x ∈ {0, 1}`)** |
| **Does Greedy (`p / w`) give optimal answer?** | **Yes — Always** | **No** |
| **Optimal Algorithm Used** | **Greedy Algorithm** | **Dynamic Programming (DP)** |
| **Time Complexity** | **`O(n log n)`** | **`O(n · W)`** |
| **Auxiliary Space** | **`O(1)`** | `O(n · W)` (or `O(W)`) |

### Real-World Uses / Applications of Fractional Knapsack
1. **Cargo / Freight loading** of divisible bulk commodities (grain, oil, chemicals, metals, powders) into trucks/ships with weight limits.
2. **Financial portfolio & budget allocation** — dividing capital across divisible investments ranked by return per unit of risk/cost.
3. **Cloud / CPU time-slice & bandwidth allocation** — assigning fractional bandwidth or compute time to tasks with highest value per unit resource.

---

## 4. Step-by-Step Algorithm

1. Compute ratio `p / w` for each item and sort `items` in **descending** order of `p / w`.
2. Initialize `profit = 0`.
3. Loop through each `(p, w)` in sorted `items`:
   - Set `take = min(w, cap)`.
   - Add `take * (p / w)` to `profit`.
   - Subtract `take` from `cap` (`cap -= take`).
   - If `cap == 0`, stop (`break`).
4. Return `profit`.

---

## 5. Line-by-Line Code Explanation

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

items = [(60,10), (100,20), (120,30)]
print(knapsack(items, 50))
```

| Line(s) | Exact Role in the Program |
|---|---|
| `def knapsack(items, cap):` | Takes list of `(profit, weight)` tuples and knapsack capacity `cap`. |
| `items.sort(key=lambda x: x[0]/x[1], reverse=True)` | Sorts `items` in place from highest `profit / weight` (`x[0] / x[1]`) to lowest (`reverse=True`). |
| `profit = 0` | Accumulator for total profit earned. |
| `for p, w in items:` | Unpacks each tuple into `p` (profit) and `w` (weight) in greedy order. |
| `take = min(w, cap)` | Takes full weight `w` if `w <= cap`, or remaining capacity `cap` (fractional pick) if `cap < w`. |
| `profit += take * p/w` | Adds full profit `p` (when `take == w`) or fractional profit `(cap / w) * p` (when `take == cap`). |
| `cap -= take; if cap == 0: break` | Deducts used capacity and exits loop immediately once knapsack is full. |
| `items = [(60,10), (100,20), (120,30)]` | Demo dataset with capacity `50`, printing `240.0`. |

---

## 6. Step-by-Step Dry Run

**Input:** `items = [(60, 10), (100, 20), (120, 30)]`, `cap = 50`

1. **Ratios & Sorted Order:**
   - `(60, 10)` → `60 / 10 = 6.0` (1st)
   - `(100, 20)` → `100 / 20 = 5.0` (2nd)
   - `(120, 30)` → `120 / 30 = 4.0` (3rd)

2. **Selection Trace:**

| Step | Item `(p, w)` | Ratio | `cap` Before | `take = min(w, cap)` | Fraction | Profit Added | Total `profit` | `cap` After |
|---|---|---|---|---|---|---|---|---|
| 1 | `(60, 10)` | `6.0` | `50` | `10` | `1` (`100%`) | `10 × 6.0 = 60.0` | `60.0` | `40` |
| 2 | `(100, 20)` | `5.0` | `40` | `20` | `1` (`100%`) | `20 × 5.0 = 100.0` | `160.0` | `20` |
| 3 | `(120, 30)` | `4.0` | `20` | `20` | **`20/30 = 2/3`** | `20 × 4.0 = 80.0` | **`240.0`** | `0` (`break`) |

---

## 7. Time & Space Complexity Fact Sheet

| Stage / Metric | Complexity | Explanation |
|---|---|---|
| **Sorting `n` items by ratio** | **O(n log n)** | Dominates overall runtime. |
| **Greedy filling loop** | **O(n)** | Scans each item at most once (`O(1)` per item). |
| **Overall Time Complexity (Best / Avg / Worst)** | **O(n log n)** | `O(n log n) + O(n) = O(n log n)`. |
| **Auxiliary Space Complexity** | **O(1)** | Sorts `items` in place and uses scalar variables (`profit`, `take`, `cap`). |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Sorting by `profit` or `weight` alone:** Suboptimal; always sort by **`profit / weight`**.
- **Mistake 2 — Omitting `reverse=True`:** Sorts ascending instead of descending and picks the *lowest-value* items first!
- **Mistake 3 — Using integer division `//` instead of float division `/`:** Truncates decimal ratios (e.g., `1.8` and `1.2` both become `1`).

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define the Fractional Knapsack Problem. | Given `n` divisible items with `(profit, weight)` and capacity `cap`, choose item fractions (`0 <= x <= 1`) to maximize total profit without exceeding `cap`. |
| 2 | Differentiate between Fractional Knapsack and 0/1 Knapsack. | **Fractional Knapsack** allows taking fractions of items and is solved optimally by **Greedy (`O(n log n)`)**; **0/1 Knapsack** forbids splitting items (`0` or `1` only) and requires **Dynamic Programming (`O(n · W)`)**. |
| 3 | Which algorithmic technique is used to solve Fractional Knapsack? | **Greedy Algorithm**. |
| 4 | What is the greedy selection criterion in Fractional Knapsack? | Highest **profit-to-weight ratio (`profit / weight`)** first. |
| 5 | Does the Greedy approach ALWAYS yield the optimal solution for Fractional Knapsack? | **Yes**, always. |
| 6 | Does the Greedy approach yield the optimal solution for 0/1 Knapsack? | **No**, because indivisible items can leave unused capacity wasted. |
| 7 | State the time complexity and auxiliary space complexity of Fractional Knapsack. | Time complexity: **O(n log n)** (due to sorting). Auxiliary space complexity: **O(1)**. |
| 8 | What is the full form of DP? | **Dynamic Programming**. |
| 9 | Why do we pass `reverse=True` in `items.sort(...)`? | Python's `.sort()` sorts ascending by default; `reverse=True` sorts ratios in **descending** order (highest ratio first). |
| 10 | On `[(60,10), (100,20), (120,30)]` with `cap = 50`, what is the Fractional optimal profit vs. 0/1 optimal profit? | Fractional optimal = **`240.0`**; 0/1 optimal = **`220`** (`100 + 120`). |
| 11 | At most how many items are taken fractionally in an optimal Fractional Knapsack solution? | **At most 1 item** (the last item that tops off remaining capacity to `0`). |
| 12 | Give three real-world applications of Fractional Knapsack. | (1) Bulk cargo loading (grain, fuel, metals), (2) investment budget allocation, and (3) network bandwidth / CPU resource allocation. |
