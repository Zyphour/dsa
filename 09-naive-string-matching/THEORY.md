# Practical 9 — Naïve String Matching

**Aim:** Find all starting indices (including overlapping occurrences) of a
pattern inside a text string using Naïve String Matching.

**Language:** Python · **Program:** [`naive_string_matching.py`](naive_string_matching.py)

---

## Concepts

- **String matching** – locate every index `i` in `text` (length `n`) where
  `text[i : i + m] == pattern` (length `m`).
- **Sliding window** – test every possible shift `i` from `0` to `n - m`,
  advancing by `1` each time so overlapping matches are also found.

## Algorithm

1. Set `n = len(text)`, `m = len(pattern)`, `positions = []`.
2. For `i = 0` to `n - m`:
   - Set `j = 0`.
   - While `j < m` and `text[i + j] == pattern[j]`: `j += 1`.
   - If `j == m`, append `i` to `positions`.
3. Return `positions`.

## Comparison

| Algorithm | Preprocessing | Search Time (Worst) | Extra Space |
|---|---|---|---|
| Naïve | None | O(n · m) | O(1) |
| KMP | O(m) LPS table | O(n + m) | O(m) |

## Exam points

- Outer loop runs `n - m + 1` times (`0 .. n - m`).
- Worst case `O(n · m)` occurs when `text` and `pattern` share long prefixes
  (e.g., `"AAAB"` inside `"AAAAAAAAAAAA"`).
- Best case is `O(n)` when the first character mismatches immediately at every
  shift.
- In `"ABABABCABAB"`, `"ABAB"` matches at `[0, 2, 7]` (`0` and `2` overlap).
