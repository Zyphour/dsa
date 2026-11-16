# Code explanation — `naive_string_matching.py`

17-line brute-force pattern matcher returning all starting indices where `pat`
occurs in `text`.

## Function

```python
def naive_search(text, pat):
    n, m = len(text), len(pat)
    pos = []
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pat[j]:
            j += 1
        if j == m:
            pos.append(i)
    return pos
```

- `i` tries every valid alignment from `0` to `n - m`.
- `j` compares characters `text[i + j]` and `pat[j]` left to right.
- If `j` reaches `m`, all characters matched and `i` is appended to `pos`
  (including overlapping matches, since `i` increments by `1`).

## Dry run — `text = "ABABABABC"`, `pat = "ABAB"`

- `i = 0`: `j` reaches `4` → match (`0`)
- `i = 1`: `text[1] = 'B' != 'A'` → stops at `j = 0`
- `i = 2`: `j` reaches `4` → match (`2`)
- `i = 3`: mismatch at `j = 0`
- `i = 4`: `j` reaches `4` → match (`4`)
- `i = 5`: mismatch at `j = 0`
- Result: `[0, 2, 4]`.

## Viva — short answers

| Question | Answer |
|---|---|
| Best and worst time complexity? | Best O(n), worst O(n·m) (e.g. `aaaa...` and `aaab`). |
| Space complexity? | O(1) extra space (excluding output list). |
| Why `n - m + 1`? | Beyond index `n - m`, fewer than `m` characters remain in `text`. |
