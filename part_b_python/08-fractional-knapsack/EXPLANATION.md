# Code explanation — `fractional_knapsack.py`

26-line greedy implementation on 5 `(name, weight, profit)` tuples with `cap = 50`.

## Key logic

```python
parcels.sort(key=lambda x: x[2] / x[1], reverse=True)

profit = 0.0
for name, w, p in parcels:
    if cap == 0:
        break
    if w <= cap:
        cap -= w
        profit += p
    else:
        frac = cap / w
        profit += p * frac
        cap = 0
```

`x[2] / x[1]` is `profit / weight` (profit per kg). Sorting with `reverse=True`
processes highest value-density parcels first, taking each whole if `w <= cap`
or splitting the last parcel with `frac = cap / w`.

## Dry run (`cap = 50`)

| Parcel | Weight | Profit | Ratio | Taken | Profit added | `cap` left |
|---|---|---|---|---|---|---|
| Medicine | 5 | 90 | 18.0 | 100% | 90 | 45 |
| Books | 10 | 60 | 6.0 | 100% | 60 | 35 |
| Furniture | 25 | 150 | 6.0 | 100% | 150 | 10 |
| Electronics | 20 | 100 | 5.0 | 50% | 50 | 0 |
| Clothes | 30 | 120 | 4.0 | 0% | 0 | 0 |

**Maximum Profit: `350.0`.**

## Viva — short answers

| Question | Answer |
|---|---|
| Why sort by `profit / weight`? | Maximises profit earned for every kilogram of truck capacity. |
| Time complexity? | O(n log n) for sorting + O(n) single pass = O(n log n). |
| Does this greedy choice work for 0/1 Knapsack? | No — 0/1 Knapsack requires Dynamic Programming. |
