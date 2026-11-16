# Code explanation — `campus_mst.py`

Data first, algorithms after:

```python
BUILDINGS = ["Main Gate", "Admin", "CSE", "IT", "ENTC",
             "Library", "Canteen", "Hostel", "Sports"]      # 9 vertices

EDGES = [("Main Gate", "Admin", 120), ...]                  # 18 (a, b, distance)
```

## What each function does

| Function | Job |
|---|---|
| `build_adjacency_list()` | `building -> [(neighbour, distance), ...]`, both directions |
| `build_adjacency_matrix()` | 9×9 table, `0` = no direct road, diagonal 0 |
| `print_graph()` | prints both representations |
| `find(x)` | representative of x's set, with path compression |
| `union(a, b)` | merge two sets; returns `False` if they were already one |
| `kruskal()` | sort edges, keep the ones `union` accepts, collect rejects |
| `prim(start)` | min-heap of edges leaving the tree |
| `show_mst(name, mst, total)` | table of edges and the total distance |

## Kruskal — the core loop

```python
for a, b, w in sorted(EDGES, key=lambda e: e[2]):    # cheapest first
    if union(INDEX[a], INDEX[b]):                    # no cycle?
        mst.append((a, b, w)); total += w
    else:
        rejected.append((a, b, w))
    if len(mst) == len(BUILDINGS) - 1:               # V-1 edges -> done
        break
```

Union-Find with path compression keeps the cycle test almost free:

```python
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]      # flatten the path
        x = parent[x]
    return x
```

The arrays `parent` and `rank` are reset at the start of `kruskal()`, because
they are module-level state.

## Prim — the core loop

```python
visited = {start}
heap = [(w, start, b) for b, w in adj_list[start]]
heapq.heapify(heap)

while heap and len(visited) < len(BUILDINGS):
    w, a, b = heapq.heappop(heap)
    if b in visited: continue              # would create a cycle
    visited.add(b); mst.append((a, b, w)); total += w
    for nxt, weight in adj_list[b]:
        if nxt not in visited:
            heapq.heappush(heap, (weight, b, nxt))
```

## Dry run — Kruskal in sorted order

| Edge | Weight | Action | Total |
|---|---|---|---|
| CSE–IT | 90 | keep | 90 |
| Main Gate–Admin | 120 | keep | 210 |
| IT–ENTC | 140 | keep | 350 |
| Canteen–Sports | 150 | keep | 500 |
| CSE–ENTC | 160 | **reject** (cycle CSE–IT–ENTC) | 500 |
| Library–Canteen | 170 | keep | 670 |
| Admin–CSE | 180 | keep | 850 |
| Admin–Library | 200 | keep | 1050 |
| Library–Sports | 210 | **reject** (already connected) | 1050 |
| IT–Library | 220 | **reject** (already connected) | 1050 |
| Canteen–Hostel | 230 | keep → 8th edge, stop | **1280** |

Prim picks the same edges in a different order and also totals 1280 m.

## Common mistakes

- Keeping `V` edges instead of `V−1` (the extra one always makes a cycle).
- Adding each edge only one way, which silently turns the graph into a directed one.
- Forgetting to reset the DSU before a second Kruskal run.
- In Prim, not skipping heap entries that point to a visited node.
- Saying "the MST is unique" — the total weight is unique, the edge set may not be.

## Viva — short answers

| Question | Answer |
|---|---|
| Spanning tree vs MST? | A spanning tree connects all vertices with V−1 edges; the MST has minimum total weight. |
| Why Union-Find in Kruskal? | To detect cycles in almost O(1) per edge. |
| Kruskal vs Prim? | Kruskal sorts edges and works well on sparse graphs; Prim grows one tree and suits dense graphs. |
| Edges in an MST of 9 vertices? | 8. |
| Why can a cheap edge be rejected? | It would close a cycle, so it adds cost without connecting anything new. |
