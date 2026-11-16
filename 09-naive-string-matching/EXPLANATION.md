# Student Guide — `naive_string_matching.py`

This guide explains how [`naive_string_matching.py`](naive_string_matching.py) works and prepares you for viva questions.

## How the Code Works

```python
def naive_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i+j] == pattern[j]: j += 1
        if j == m: positions.append(i)
    return positions
```
- **Why `range(n - m + 1)`?** With `n = 11` and `m = 4`, the last starting index where a 4-letter pattern can still fit inside an 11-letter text is index `7` (`7, 8, 9, 10`). `range(11 - 4 + 1)` gives `0, 1, ..., 7`.
- **Inner `while` loop:** Compares `text[i + j]` against `pattern[j]`. It stops as soon as `j == m` (full match) or a mismatch happens.
- **`if j == m:`** Only true if the `while` loop didn't hit any mismatch across all `m` characters — so `i` is saved in `positions`.

## Dry Run — `text = "ABABABCABAB"`, `pattern = "ABAB"`

| `i` | Substring `text[i:i+4]` | Match? |
|---|---|---|
| `0` | `"ABAB"` | **Yes** → append `0` |
| `1` | `"BABA"` | No (`'B' != 'A'`) |
| `2` | `"ABAB"` | **Yes** → append `2` (overlapping!) |
| `3` | `"BABC"` | No |
| `4` | `"ABCA"` | No (`j=2`: `'C' != 'A'`) |
| `5` | `"BCAB"` | No |
| `6` | `"CABA"` | No |
| `7` | `"ABAB"` | **Yes** → append `7` |

Output: `[0, 2, 7]`

## Common Mistakes

- Using `range(n - m)` instead of `range(n - m + 1)` — misses a match sitting right at the end of `text` (like index `7` here!).
- Jumping `i` forward by `m` after a match instead of `1` — misses overlapping matches (like index `2`!).

## Questions You Might Be Asked (Viva Prep)

| Question | Answer |
|---|---|
| Why does the outer loop stop at `n - m`? | Beyond `n - m`, fewer than `m` characters remain in `text`, so `pattern` cannot fit. |
| What is the worst-case time complexity and an example input? | `O(n · m)`, for instance searching `"AAAB"` in `"AAAAAAAAAAAA"`. |
| Does this algorithm handle overlapping matches? | Yes, because `i` shifts by only `1` even after a full match is found. |
| Name faster string matching algorithms that avoid re-checking characters. | KMP (Knuth-Morris-Pratt), Rabin-Karp, and Boyer-Moore. |
