# Code explanation — `naive_string_matching.py`

| Function | Job |
|---|---|
| `naive_search(text, pattern, show_steps)` | returns `(positions, comparisons)`; prints the alignments when asked |
| `brute_force_check(text, pattern)` | independent answer using Python slicing, used to verify the result |
| `run_demo()` | three demos: normal, overlapping, worst case |
| `run_custom()` | takes a text and pattern from the user |

## The main function

```python
n, m = len(text), len(pattern)

if m == 0:                 # empty pattern matches everywhere
    return list(range(n + 1)), 0
if m > n:                  # can never fit
    return [], 0

for i in range(n - m + 1):         # every possible start
    j = 0
    while j < m:
        comparisons += 1
        if text[i + j] != pattern[j]:
            break                  # mismatch -> slide the pattern
        j += 1
    if j == m:                     # all m characters matched
        positions.append(i)
```

`j == m` is the test for a match, because the inner loop either broke early or
completed. `i + j` reads the text under the pattern.

`show_steps=True` prints the text and the shifted pattern with `<== MATCH`
markers, which is the fastest way to explain the algorithm on a board.

## Dry run — `text = ABABABABC`, `pattern = ABAB`

| Shift | Compare | Result | Comparisons used |
|---|---|---|---|
| 0 | A B A B | match at 0 | 4 |
| 1 | B A B A | fail on 1st character | 1 |
| 2 | A B A B | match at 2 | 4 |
| 3 | B A B A | fail on 1st character | 1 |
| 4 | A B A B | match at 4 | 4 |
| 5 | B A B A | fail on 1st character | 1 |

Total 15 comparisons, positions `[0, 2, 4]` — exactly what the program prints.

## Worst-case demo

```
text    = 'a' × 20000
pattern = 'a' × 500 + 'b'
comparisons = 9,769,500      (n × m = 10,020,000)
```

Every start position compares 500 matching characters before failing on the last
one. That is the `O(n·m)` behaviour in numbers.

## Common mistakes

- Looping `i` up to `n` instead of `n − m`, which reads outside the string.
- Reporting only the first match.
- Jumping `i += m` after a match and losing overlapping matches.
- Ignoring the empty-pattern case (a `range(m)` loop matches nothing and gives
  wrong indices).
- Not resetting the comparison counter between calls.

## Viva — short answers

| Question | Answer |
|---|---|
| Worst case and an example? | O(n·m); text `aaaa…`, pattern `aaa…b`. |
| Best case? | O(n) — first-character mismatches everywhere. |
| Why is KMP better? | A failure table avoids restarting the match, giving O(n+m). |
| Does it find overlapping matches? | Yes, it shifts by exactly one position. |
| Where is pattern matching used? | Editors, DNA sequences, plagiarism checks, log analysis. |
