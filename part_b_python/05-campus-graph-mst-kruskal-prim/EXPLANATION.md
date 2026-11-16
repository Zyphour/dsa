# Code explanation — `campus_mst.py`

5 campus buildings and 7 undirected weighted roads (no external imports needed):

```python
buildings = ["Gate", "Admin", "CSE", "Library", "Canteen"]
edges = [("Gate", "Admin", 10), ...]
```

Both graph representations (`adj` dictionary and 5×5 `mat` matrix) are populated
in one loop over `edges`.

## What each function does

| Function | Job |
|---|---|
| `find(p, i)` | finds set representative of `i` in Union-Find parent array `p` |
| `kruskal()` | sorts `edges` by weight, merges disjoint sets `ru != rv`, accumulates MST |
| `prim(start)` | starts `vis = [start]`, repeatedly picks cheapest edge crossing out of `vis` |

## Kruskal

```python
p = list(range(n))
for u, v, w in sorted(edges, key=lambda e: e[2]):
    ru, rv = find(p, idx[u]), find(p, idx[v])
    if ru != rv:
        p[rv] = ru
        mst.append((u, v, w))
        total += w
```

## Prim

```python
vis = [start]
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
```

## Dry run — Kruskal in sorted order

| Edge | Weight | Action | Total |
|---|---|---|---|
| Gate–Admin | 10 | keep | 10 |
| CSE–Canteen | 12 | keep | 22 |
| Admin–CSE | 15 | keep | 37 |
| Admin–Canteen | 16 | **skip** (cycle Admin–CSE–Canteen) | 37 |
| Library–Canteen | 18 | keep → 4th edge (`V−1`) | **55** |
| Admin–Library | 20 | skip | 55 |
| Gate–CSE | 25 | skip | 55 |

Prim starting from `"Gate"` also reaches total weight **55** with `4` edges.

## Viva — short answers

| Question | Answer |
|---|---|
| Spanning tree vs MST? | Connects all V vertices with V−1 edges and no cycles; MST has minimum total weight. |
| Why Union-Find in Kruskal? | Detects whether an edge connects two already-connected vertices (cycle). |
| Kruskal vs Prim? | Kruskal sorts edges (good for sparse graphs); Prim grows a single connected tree. |
| Number of edges in MST for 5 buildings? | `V − 1 = 4`. |
