# Practical 9 — Naïve String Matching

**Aim:** Find every starting index `i` where `text[i : i+m]` equals `pattern`,
using the Naïve (brute force) String Matching algorithm.

**Language:** Python · **Program:** [`naive_string_matching.py`](naive_string_matching.py)

---

## The idea

Put the pattern under the text at position 0 and compare character by character.
If all `m` characters match, record the index. Then slide the pattern **one place
to the right** and try again, until it would stick out past the end of the text
(`i = n − m` is the last valid start).

```
text    : A B A B A B A B C
pattern : A B A B            shift 0 -> match at 0
            A B A B          shift 1 -> no ('B' vs 'A')
              A B A B        shift 2 -> match
```

## Edge cases

| Case | Behaviour |
|---|---|
| `m == 0` (empty pattern) | matches at every position `0 … n` |
| `m > n` | no match possible |
| Overlapping matches | reported, because the pattern shifts by 1 (`"aa"` in `"aaaaa"` → 0, 1, 2, 3) |
| Any characters | compare exactly, so digits, spaces and punctuation are fine |

## Complexity

| Case | Comparisons |
|---|---|
| Best | `O(n)` — the first character usually mismatches |
| Worst | `O(n·m)` — e.g. `text = aaaa…a` with `pattern = aaa…b` |
| Space | `O(1)` |

The worst case happens because after a long partial match we restart the
comparison from the next text position and forget everything we just matched.

**Improvement:** Knuth–Morris–Pratt pre-processes the pattern into a failure
table, so after a mismatch it can skip positions safely and finish in `O(n + m)`.
Rabin–Karp uses hashing for `O(n)` on average. Both are the naive idea plus a way
to avoid re-reading characters.

## Exam points

- The experiment asks for **all** indices, not just the first one.
- Sliding by `m` after a match would miss overlapping occurrences.
- Loop bound is `n − m + 1`, otherwise the window runs off the end.
- Uses: Ctrl+F, `strstr()`, DNA matching, log/plagiarism search, spam filters.
