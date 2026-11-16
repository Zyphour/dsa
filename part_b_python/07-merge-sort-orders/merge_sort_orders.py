orders = [
    {"id": "ORD-1", "item": "Bag", "minutes": 45},
    {"id": "ORD-2", "item": "Book", "minutes": 20},
    {"id": "ORD-3", "item": "Bottle", "minutes": 15},
    {"id": "ORD-4", "item": "Charger", "minutes": 30},
    {"id": "ORD-5", "item": "Mug", "minutes": 10},
]


def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["minutes"] <= right[j]["minutes"]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


print("Before:")
for o in orders:
    print(o["id"], o["item"], o["minutes"], "min")

sorted_orders = merge_sort(orders)

print("\nAfter:")
for o in sorted_orders:
    print(o["id"], o["item"], o["minutes"], "min")
