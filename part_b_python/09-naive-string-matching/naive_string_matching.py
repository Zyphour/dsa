"""
EXPERIMENT 9 : String Processing - Naive (Brute Force) String Matching
----------------------------------------------------------------------
Part B - Python

Given a text of length n and a pattern of length m, find EVERY starting
index i where text[i : i+m] is exactly equal to the pattern.

Naive idea (the simplest possible way):
    Place the pattern under the text at position 0, compare characters.
    If all m characters match -> record i.
    Slide the pattern one place to the right and try again.
    Stop when the pattern would stick out past the end of the text
    (i.e. i > n - m).

Time  : O(n * m) worst case  (e.g. text = "aaaaaa", pattern = "aaab")
Space : O(1) extra

We also count comparisons so the O(n*m) behaviour can be seen on real data.

Run: python3 naive_string_matching.py
"""


def naive_search(text, pattern, show_steps=False):
    """
    Returns (positions, comparisons).

    positions    : list of every starting index where the pattern is found
                   (overlapping matches ARE reported, e.g. "aa" in "aaaa"
                   is found at 0, 1 and 2)
    comparisons  : how many character comparisons were made
    """
    n = len(text)
    m = len(pattern)
    positions = []
    comparisons = 0

    # m == 0 : the empty pattern matches at every position, including the end
    if m == 0:
        return list(range(n + 1)), 0

    # pattern can never fit
    if m > n:
        return [], 0

    # try every possible starting index
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break                  # mismatch -> slide the pattern
            j += 1

        found = (j == m)               # the whole pattern matched

        if show_steps:
            marker = "  <== MATCH" if found else ""
            print(f"  shift {i:>2}: {text}")
            print(f"            {' ' * i}{pattern}{marker}")

        if found:
            positions.append(i)

    return positions, comparisons


def brute_force_check(text, pattern):
    """A second, independent way of getting the answer (simple slicing)."""
    if pattern == "":
        return list(range(len(text) + 1))
    return [i for i in range(len(text) - len(pattern) + 1)
            if text[i:i + len(pattern)] == pattern]


# ----------------------------------------------------------------------
def run_demo():
    print("=" * 60)
    print("DEMO 1 : simple text")
    print("=" * 60)
    text = "ABABABABC"
    pattern = "ABAB"
    print(f"text    = {text}   (length {len(text)})")
    print(f"pattern = {pattern}   (length {len(pattern)})\n")

    positions, comparisons = naive_search(text, pattern, show_steps=True)
    print(f"\nPattern found at indices: {positions}")
    print(f"Comparisons used        : {comparisons}")

    print("\n" + "=" * 60)
    print("DEMO 2 : overlapping matches")
    print("=" * 60)
    text = "aaaaa"
    pattern = "aa"
    positions, comparisons = naive_search(text, pattern)
    print(f"text = {text}, pattern = {pattern}")
    print(f"Found at: {positions}  (overlapping matches are also reported)")

    print("\n" + "=" * 60)
    print("DEMO 3 : worst case for the naive algorithm")
    print("=" * 60)
    text = "a" * 20000
    pattern = "a" * 500 + "b"
    positions, comparisons = naive_search(text, pattern)
    print(f"text = 'a' x 20000, pattern = 'a' x 500 + 'b'")
    print(f"Matches           : {len(positions)} (none, as expected)")
    print(f"Comparisons       : {comparisons}")
    print(f"n * m             : {len(text) * len(pattern)}")
    print("Almost n*m comparisons were needed -> that is the worst case, O(n*m).")


def run_custom():
    text = input("\nEnter the text    : ")
    pattern = input("Enter the pattern : ")

    positions, comparisons = naive_search(text, pattern)
    if not positions:
        print("Pattern not found.")
    else:
        print(f"Pattern found at indices: {positions}")
    print(f"Comparisons used: {comparisons}")

    # safety check with an independent method
    if positions == brute_force_check(text, pattern):
        print("(verified with Python slicing)")


if __name__ == "__main__":
    run_demo()
    while True:
        choice = input("\nTry your own text? (y/n): ").strip().lower()
        if choice == "y":
            run_custom()
        else:
            print("Bye!")
            break
