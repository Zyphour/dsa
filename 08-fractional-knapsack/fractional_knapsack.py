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
