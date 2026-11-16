# Practical 5 — Campus Graph and Minimum Spanning Tree

**Aim:** Represent the college campus as a weighted graph (departments as nodes,
walking distances as edges) using an adjacency list and an adjacency matrix, then
find the minimum spanning tree with Kruskal's and Prim's algorithms.

**Language:** Python · **Program:** [`campus_mst.py`](campus_mst.py)

---

## Concepts

- **Vertex (node)** – a building / department: 5 in our graph.
- **Edge (link)** – a road between two buildings, with a **weight** = distance: 7 roads.
- **Undirected** – the road can be walked both ways, so each edge is stored twice.
- **Sparse graph** – few edges compared to the maximum possible → adjacency list is better.

| Representation | Space | Best for |
|---|---|---|
| Adjacency matrix (V×V) | O(V²) | dense graphs, O(1) "is there an edge?" |
| Adjacency list | O(V+E) | sparse graphs, walking a neighbourhood |

**Spanning tree** – connects all vertices, contains no cycle, and has exactly
`V−1` edges (4 here). **Minimum spanning tree (MST)** – the spanning tree with the
smallest total weight: the cheapest way to connect every building.

## Kruskal — greedy on edges

1. Sort all edges by weight, cheapest first.
2. Take the cheapest edge and keep it **if it does not create a cycle**.
3. Stop after `V−1` edges are kept.

Cycle detection uses **Union-Find (DSU)**: `find(x)` gives the set (component) of
x, `union(a,b)` merges two sets. If `find(a) == find(b)`, both ends are already
connected, so the edge would form a cycle and is rejected.

Time: **O(E log E)** — the sorting dominates; DSU operations are almost O(1).

## Prim — greedy from a vertex

1. Start from any building; it is the tree so far.
2. From all edges leaving the tree, take the cheapest one that reaches a **new**
   building.
3. Repeat until every building is in the tree.

A min-heap gives the cheapest outgoing edge in `O(log V)`, so the total is
**O(E log V)**. The simple version without a heap scans all vertices and costs
`O(V²)`, which is fine for a small campus.

## Comparison

| | Kruskal | Prim |
|---|---|---|
| Greedy on | edges, in sorted order | one growing tree |
| Needs | sorting + Union-Find | heap (or a V×V scan) |
| Time | O(E log E) | O(E log V) |
| Good for | sparse graphs | dense graphs |
| Result | MST | MST |

Both are correct, and every MST of a graph has the **same total weight** — in our
campus both give **55**, which is a built-in self-check.

## Exam points

- The MST has `V−1` edges; an extra edge would always close a cycle.
- A cheaper edge can still be rejected (here `Admin–Canteen 16`) because it closes a cycle.
- Different MSTs can exist for one graph, but their total weights are equal.
- Applications: network cable, water pipes, power lines, road planning.
