"""
EXPERIMENT 8 : Greedy Algorithm - Fractional Knapsack
-----------------------------------------------------
Part B - Python

Story: you run a shipping company. A truck can carry at most W kg.
Each parcel has a weight and a profit, and you are allowed to ship a
FRACTION of a parcel (cut it open, send half of it). Choose the parcels
that give the maximum total profit.

Greedy idea:
    "Take the parcel that gives the most profit per kg first."
    profit/weight = value density. Sort by this ratio (biggest first),
    then fill the truck until it is full. The last parcel may be split.

Why is greedy correct here? Because if parcel A gives more profit per kg
than parcel B, every kg of space is better used by A. Any piece of B could
always be replaced by the same weight of A for at least as much profit.

    Time  : O(n log n) for the sort (everything else is one pass)
    Space : O(n) for the sorted copy of the item list

Note: this "take fractions" rule does NOT work for 0/1 knapsack, where a
parcel must be taken whole (that problem needs dynamic programming).

Run: python3 fractional_knapsack.py
"""

# ----------------------------------------------------------------------
# sample data: (parcel name, weight in kg, profit in Rs)
# ----------------------------------------------------------------------
PARCELS = [
    ("Parcel A - Books",        10, 60),
    ("Parcel B - Electronics",  20, 100),
    ("Parcel C - Clothes",      30, 120),
    ("Parcel D - Medicine",      5, 90),
    ("Parcel E - Furniture",    25, 150),
]

CAPACITY = 50


# ----------------------------------------------------------------------
# GREEDY FRACTIONAL KNAPSACK
# ----------------------------------------------------------------------
def fractional_knapsack(parcels, capacity, show_steps=True):
    # make a copy and sort by profit per kg, biggest first
    items = []
    for name, weight, profit in parcels:
        items.append({
            "name": name,
            "weight": weight,
            "profit": profit,
            "ratio": profit / weight,
        })
    items.sort(key=lambda item: item["ratio"], reverse=True)

    if show_steps:
        print("Parcels sorted by profit per kg (best first):")
        print(f"{'PARCEL':<26}{'WEIGHT':>8}{'PROFIT':>8}{'PROFIT/KG':>11}")
        for it in items:
            print(f"{it['name']:<26}{it['weight']:>8.1f}{it['profit']:>8.1f}"
                  f"{it['ratio']:>11.2f}")
        print()

    total_profit = 0.0
    used_weight = 0.0
    taken = []

    for it in items:
        if capacity == 0:
            break                                    # truck full, stop

        if it["weight"] <= capacity:                 # take the whole parcel
            fraction = 1.0
            capacity -= it["weight"]
            total_profit += it["profit"]
            used_weight += it["weight"]
        else:                                        # take only a part of it
            fraction = capacity / it["weight"]
            total_profit += it["profit"] * fraction
            used_weight += it["weight"] * fraction
            capacity = 0

        taken.append({
            "name": it["name"],
            "fraction": fraction,
            "weight": it["weight"] * fraction,
            "profit": it["profit"] * fraction,
        })

        if show_steps:
            if fraction == 1.0:
                print(f"  take ALL of {it['name']:<26} (+ Rs {it['profit']:.2f})")
            else:
                print(f"  take {fraction * 100:.1f}% of {it['name']:<26} "
                      f"(+ Rs {it['profit'] * fraction:.2f})")

    return taken, total_profit, used_weight


# ----------------------------------------------------------------------
def main():
    print("=" * 62)
    print("FRACTIONAL KNAPSACK - maximise shipping profit")
    print("=" * 62)
    print(f"Truck capacity: {CAPACITY} kg")
    print(f"Parcels available: {len(PARCELS)}\n")

    print(f"{'PARCEL':<26}{'WEIGHT(kg)':>11}{'PROFIT(Rs)':>11}")
    print("-" * 48)
    for name, w, p in PARCELS:
        print(f"{name:<26}{w:>11}{p:>11}")
    print()

    taken, total_profit, used_weight = fractional_knapsack(PARCELS, CAPACITY)

    print("\n--- FINAL LOADING PLAN ---")
    print(f"{'PARCEL':<26}{'TAKEN':>8}{'WEIGHT':>9}{'PROFIT':>10}")
    print("-" * 53)
    for t in taken:
        print(f"{t['name']:<26}{t['fraction'] * 100:>7.1f}%"
              f"{t['weight']:>9.1f}{t['profit']:>10.2f}")
    print("-" * 53)
    print(f"{'TOTAL':<26}{'':>8}{used_weight:>9.1f}{total_profit:>10.2f}")

    print(f"\nTruck used     : {used_weight:.1f} / {CAPACITY} kg")
    print(f"Maximum profit : Rs {total_profit:.2f}")
    print("\nGreedy choices are locally best (best profit per kg) and that")
    print("happens to give the globally best answer for this problem.")


if __name__ == "__main__":
    main()
