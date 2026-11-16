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


text = "ABABABABC"
pat = "ABAB"
print("Text:", text)
print("Pattern:", pat)
print("Found at:", naive_search(text, pat))
