"""
EXPERIMENT 6 : Heap Sort
------------------------
Part B - Python

A heap is a COMPLETE binary tree stored inside a plain array (no pointers!):

    parent of index i      = (i - 1) // 2
    left child of index i  = 2 * i + 1
    right child of index i = 2 * i + 2

MAX-HEAP rule: every parent is >= its children,
so the biggest element always sits at index 0 (the root).

Heap Sort in two steps:
    1. BUILD a max-heap out of the array               -> O(n)
    2. REPEATEDLY swap the root (biggest) to the end
       and shrink the heap, repairing it                -> O(n log n)

    Total time  : O(n log n)  (best = average = worst)
    Extra space : O(1)        (it sorts inside the same array)

Run: python3 heap_sort.py
"""

import random


def heapify(arr, n, i, trace=False):
    """Push arr[i] down until the subtree with root i is a valid max-heap."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:                        # a child was bigger -> swap down
        arr[i], arr[largest] = arr[largest], arr[i]
        if trace:
            print(f"      swap arr[{i}] <-> arr[{largest}] -> {arr[:n]}")
        heapify(arr, n, largest, trace)     # keep fixing the lower subtree


def heap_sort(arr, trace=False):
    n = len(arr)

    # ---- step 1: build a max-heap, starting from the last parent ----
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, trace)
    if trace:
        print("  After building max-heap:", arr)

    # ---- step 2: move the maximum to the end, one by one ----
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]     # biggest goes to position end
        if trace:
            print(f"  placed {arr[end]} at index {end} -> {arr}")
        heapify(arr, end, 0, trace)             # repair the smaller heap

    return arr


# ----------------------------------------------------------------------
# tests
# ----------------------------------------------------------------------
def check():
    for size in range(0, 60):
        data = [random.randint(-100, 100) for _ in range(size)]
        if heap_sort(data.copy()) != sorted(data):
            print("FAILED for", data)
            return False
    print("\nSelf-check: 60 random arrays sorted correctly by Heap Sort.")
    return True


if __name__ == "__main__":
    print("=" * 55)
    print("HEAP SORT DEMO WITH STEP-BY-STEP TRACE")
    print("=" * 55)

    numbers = [4, 10, 3, 5, 1]
    print("\nOriginal array:", numbers)
    print("\nBuilding max-heap:")
    heap_sort(numbers, trace=True)

    print("\nSorted (ascending):", numbers)

    print("\n" + "=" * 55)
    print("WORKING ON A BIGGER ARRAY")
    print("=" * 55)
    big = [45, 12, 78, 3, 99, 23, 67, 8, 56, 41, 19, 90]
    print("Before:", big)
    heap_sort(big)
    print("After :", big)

    print("\n--- Complexity ---")
    print("Building the heap : O(n)")
    print("Sorting phase     : O(n log n)")
    print("Overall           : O(n log n) time, O(1) extra space")
    print("Not stable (equal values may change their relative order).")

    check()
