# Practical 9: Naïve String Matching — Complete Reference & Code Guide (`naive_string_matching.py`)

> **Aim:** Find all starting indices (including overlapping occurrences) of a pattern inside a text string using Naïve String Matching.
>
> **Language:** Python · **Program:** [`naive_string_matching.py`](naive_string_matching.py) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`naive_string_matching.py`](naive_string_matching.py) defines `naive_match(text, pattern)` and runs it on `text = "ABABABCABAB"` (`length n = 11`) and `pattern = "ABAB"` (`length m = 4`). It slides `pattern` one index at a time across every valid starting index `i` (`0` through `n - m = 7`), checks character-by-character whether `text[i .. i + m - 1]` equals `pattern`, collects **every matching 0-based start index (including overlapping matches)** into `positions`, and prints `[0, 2, 7]`.

### Exact Program Output
```text
[0, 2, 7]
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Full Form & Definition |
|---|---|
| **String Matching (Pattern Searching)** | The problem of finding one or **all** 0-based starting indices `i` (called **valid shifts**) in a string `text` (length `n`) where a substring matches `pattern` (length `m`). |
| **Naïve (Brute-Force) String Matching** | Pattern-matching algorithm with **zero preprocessing** that tests every possible shift `i` from `0` to `n - m` by comparing characters `text[i + j]` and `pattern[j]` left to right. |
| **Shift (`i`)** | Starting index in `text` where `pattern[0]` is currently aligned (`0 <= i <= n - m`). Total valid shifts tested = **`n - m + 1`**. |
| **Substring** | A contiguous sequence of characters inside a string (`text[i : i + m]`). |
| **Overlapping Match** | Two occurrences of `pattern` that share one or more characters in `text` (e.g., `"ABAB"` at `i = 0` (`0..3`) and `i = 2` (`2..5`) share indices `2` and `3`). |
| **KMP** | **Full Form:** *Knuth-Morris-Pratt Algorithm* — an optimized `O(n + m)` string-matching algorithm that avoids re-checking already matched characters. |
| **LPS** | **Full Form:** *Longest Proper Prefix which is also a Suffix* — the `O(m)` preprocessing array used inside KMP. |
| **DNA** | **Full Form:** *Deoxyribonucleic Acid* — biological nucleotide sequences (`A, C, G, T`) where exact/overlapping pattern matching is widely applied. |

---

## 3. Core Facts, Rules, Comparison & Uses

### Key Exam Facts
1. **Number of Window Shifts (`n - m + 1`):**
   - For `pattern` of length `m` to fit inside `text` of length `n`, the last valid starting index is **`n - m`** (covering `n - m .. n - 1`).
   - From `0` to `n - m` inclusive is **`n - m + 1` shifts** (`range(n - m + 1)` in Python).
2. **Overlapping Occurrences:**
   - Because `i` advances by **`1`** after every check (even after a match), **all overlapping occurrences** are found automatically (`0` and `2` in `"ABABABCABAB"`).
3. **Zero Preprocessing & `O(1)` Extra Memory:**
   - Unlike KMP or Boyer-Moore, Naïve String Matching needs no auxiliary lookup tables.

### Advantages & Disadvantages
- **Advantages:**
  1. Extremely simple to implement (`8` lines of code).
  2. Requires **zero preprocessing** and **O(1)** extra working space.
  3. Fast (`~O(n)`) in practice on ordinary natural-language text where mismatches occur on the 1st character most of the time.
- **Disadvantages:**
  1. Degrades to **O(n · m)** in the worst case when `text` and `pattern` have repeated characters (re-checks characters over and over).

### Comparison: Naïve vs. KMP vs. Rabin-Karp

| Algorithm | Preprocessing Time | Best-Case Search Time | Worst-Case Search Time | Extra Space |
|---|---|---|---|---|
| **Naïve String Matching** | **None (`O(1)`)** | **O(n)** | **O((n - m + 1) · m) = O(n · m)** | **O(1)** |
| **KMP** (*Knuth-Morris-Pratt*) | `O(m)` (LPS array) | O(n + m) | **O(n + m)** | `O(m)` |
| **Rabin-Karp** (Rolling Hash) | `O(m)` | O(n + m) | O(n · m) (hash collisions) | `O(1)` |

### Real-World Uses / Applications of String Matching
1. **`Ctrl + F` Find / Search & Replace** in text editors, IDEs, PDF viewers, and web browsers.
2. **Plagiarism detection, spam filters, and intrusion detection** (matching malware signatures in network packets).
3. **Bioinformatics / DNA sequence analysis** — locating gene motifs like `"ATGCG"` inside genome strings.
4. Standard library functions (`str.find()`, `in` operator, `strstr()` in C) on short strings.

---

## 4. Step-by-Step Algorithm

1. Set `n = len(text)`, `m = len(pattern)`, and `positions = []`.
2. Loop shift `i` from `0` to `n - m` (`range(n - m + 1)`):
   - Set `j = 0`.
   - While `j < m` **and** `text[i + j] == pattern[j]`:
     - Increment `j += 1`.
   - If `j == m`, append `i` to `positions`.
3. Return `positions`.

---

## 5. Line-by-Line Code Explanation

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

print(naive_match("ABABABCABAB", "ABAB"))
```

| Line(s) | Exact Role in the Program |
|---|---|
| `n = len(text); m = len(pattern)` | Stores text length (`11`) and pattern length (`4`). |
| `positions = []` | Stores all 0-based indices where `pattern` matches `text`. |
| `for i in range(n - m + 1):` | Iterates `i` over every valid starting index `0, 1, ..., n - m` (`0..7`). |
| `j = 0` | Resets character offset inside `pattern` to `0` at the start of each shift. |
| `while j < m and text[i+j] == pattern[j]: j += 1` | Compares `pattern[0..m-1]` against `text[i..i+m-1]`; stops immediately on the first mismatch or when `j == m`. |
| `if j == m: positions.append(i)` | `j == m` holds if and only if all `m` characters matched — records index `i`. |

---

## 6. Step-by-Step Dry Run — `text = "ABABABCABAB"`, `pattern = "ABAB"`

`n = 11`, `m = 4`, valid shifts `i = 0 .. 7`:

| Shift `i` | Window `text[i : i+4]` | Inner `while` Stops At | `j == 4`? | `positions` |
|---|---|---|---|---|
| `0` | `"ABAB"` | `j = 4` (all 4 chars matched) | **Yes** | `[0]` |
| `1` | `"BABA"` | `j = 0` (`'B' != 'A'`) | No | `[0]` |
| `2` | `"ABAB"` | `j = 4` (all 4 chars matched — **overlaps** with `0`!) | **Yes** | `[0, 2]` |
| `3` | `"BABC"` | `j = 0` (`'B' != 'A'`) | No | `[0, 2]` |
| `4` | `"ABCA"` | `j = 2` (`'C' != 'A'`) | No | `[0, 2]` |
| `5` | `"BCAB"` | `j = 0` (`'B' != 'A'`) | No | `[0, 2]` |
| `6` | `"CABA"` | `j = 0` (`'C' != 'A'`) | No | `[0, 2]` |
| `7` | `"ABAB"` | `j = 4` (all 4 chars matched) | **Yes** | **`[0, 2, 7]`** |

---

## 7. Time & Space Complexity Fact Sheet

| Case / Metric | Complexity | Condition / Example |
|---|---|---|
| **Best-Case Time Complexity** | **O(n)** (`n - m + 1` checks) | First character `pattern[0]` mismatches at every shift (e.g., `"BBBBBBBB"` & `"ABAB"`). |
| **Average-Case Time Complexity** | **O(n)** (on random text) | Mismatches happen within 1–2 characters on large alphabets. |
| **Worst-Case Time Complexity** | **O((n - m + 1) · m) = O(n · m)** | Every shift matches `m - 1` characters before failing on the last char (e.g., `text = "AAAAAAAAAAAA"`, `pattern = "AAAB"`, or all `'A'`s). |
| **Preprocessing Time** | **O(1)** (None) | No lookup table constructed. |
| **Auxiliary Space Complexity** | **O(1)** | Only scalar variables `n`, `m`, `i`, `j` (excluding output list `positions`). |

---

## 8. Important Exam Points & Common Mistakes

- **Mistake 1 — Writing `range(n - m)` instead of `range(n - m + 1)`:** Misses any match occurring at the very end of `text` (would miss index `7`!).
- **Mistake 2 — Jumping `i += m` after a match:** Misses overlapping matches (would miss index `2`!).
- **Mistake 3 — Writing `range(n)`:** Causes `IndexError` when `i > n - m` because `i + j` goes past `n - 1`.

---

## 9. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | Define String Matching (Pattern Searching). | Finding all starting indices `i` in a text string of length `n` where a given pattern string of length `m` occurs as a contiguous substring. |
| 2 | Why is this algorithm called "Naïve" String Matching? | Because it performs no preprocessing on the pattern and checks every valid shift independently from scratch. |
| 3 | State the best-case and worst-case time complexities of Naïve String Matching. | Best case: **O(n)**. Worst case: **O((n - m + 1) · m) = O(n · m)**. |
| 4 | Give an example input that causes the worst-case `O(n · m)` time. | Searching `pattern = "AAAB"` inside `text = "AAAAAAAAAAAA"` (every shift checks all `m` characters). |
| 5 | State the auxiliary space complexity of Naïve String Matching. | **O(1)** constant extra space. |
| 6 | How many shifts does the outer loop test for text length `n` and pattern length `m`? | **`n - m + 1` shifts** (`i = 0` to `n - m`). |
| 7 | Why does the outer loop stop at `n - m` instead of `n - 1`? | After index `n - m`, fewer than `m` characters remain in `text`, so a pattern of length `m` cannot fit. |
| 8 | Does Naïve String Matching detect overlapping occurrences? Why? | **Yes**, because the window shifts forward by `1` index (`i + 1`) even after finding a complete match. |
| 9 | What are the full forms of KMP and LPS? | **KMP:** Knuth-Morris-Pratt. **LPS:** Longest Proper Prefix which is also a Suffix. |
| 10 | Name three string-matching algorithms faster than Naïve Search in the worst/average case. | **KMP (`O(n + m)`)**, **Rabin-Karp**, and **Boyer-Moore**. |
| 11 | Give three real-world applications/uses of String Matching. | (1) `Ctrl + F` search in text editors/browsers, (2) DNA gene sequence matching, and (3) plagiarism / antivirus signature detection. |
| 12 | What does `naive_match` return if `len(pattern) > len(text)`? | An empty list `[]` (`n - m + 1 <= 0`, so `range(...)` executes 0 iterations). |
