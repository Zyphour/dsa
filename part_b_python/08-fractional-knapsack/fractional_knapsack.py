parcels = [
    ("Books", 10, 60),
    ("Electronics", 20, 100),
    ("Clothes", 30, 120),
    ("Medicine", 5, 90),
    ("Furniture", 25, 150),
]

cap = 50
parcels.sort(key=lambda x: x[2] / x[1], reverse=True)

profit = 0.0
for name, w, p in parcels:
    if cap == 0:
        break
    if w <= cap:
        cap -= w
        profit += p
        print(name, ": 100% | Profit:", p)
    else:
        frac = cap / w
        profit += p * frac
        cap = 0
        print(name, ":", round(frac * 100, 1), "% | Profit:", round(p * frac, 2))

print("Maximum Profit:", profit)
