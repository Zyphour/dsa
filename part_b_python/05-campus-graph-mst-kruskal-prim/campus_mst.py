buildings = ["Gate", "Admin", "CSE", "Library", "Canteen"]

edges = [
    ("Gate", "Admin", 10),
    ("Gate", "CSE", 25),
    ("Admin", "CSE", 15),
    ("Admin", "Canteen", 16),
    ("Admin", "Library", 20),
    ("CSE", "Canteen", 12),
    ("Library", "Canteen", 18),
]

n = len(buildings)
idx = {buildings[i]: i for i in range(n)}

adj = {b: [] for b in buildings}
mat = [[0] * n for _ in range(n)]

for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))
    mat[idx[u]][idx[v]] = w
    mat[idx[v]][idx[u]] = w


def find(p, i):
    while p[i] != i:
        i = p[i]
    return i


def kruskal():
    p = list(range(n))
    mst = []
    total = 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        ru, rv = find(p, idx[u]), find(p, idx[v])
        if ru != rv:
            p[rv] = ru
            mst.append((u, v, w))
            total += w
    return mst, total


def prim(start):
    vis = [start]
    mst = []
    total = 0
    while len(vis) < n:
        best = None
        for u, v, w in edges:
            if u in vis and v not in vis and (best is None or w < best[2]):
                best = (u, v, w)
            elif v in vis and u not in vis and (best is None or w < best[2]):
                best = (v, u, w)
        vis.append(best[1])
        mst.append(best)
        total += best[2]
    return mst, total


print("Adjacency List:")
for b in buildings:
    print(b, ":", adj[b])

print("\nAdjacency Matrix:")
for row in mat:
    print(row)

k_mst, k_wt = kruskal()
print("\nKruskal MST:", k_mst)
print("Total Weight:", k_wt)

p_mst, p_wt = prim("Gate")
print("\nPrim MST:", p_mst)
print("Total Weight:", p_wt)
