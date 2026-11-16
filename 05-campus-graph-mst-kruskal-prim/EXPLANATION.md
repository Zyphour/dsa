# Practical 5: Campus Graph & MST (Kruskal & Prim) — Complete Reference & Code Guide (`campus_mst.py`)

> **Aim:** Represent the college campus as a weighted graph (departments as nodes, walking distances as edges) using an adjacency list and an adjacency matrix, then find the minimum spanning tree with Kruskal's and Prim's algorithms.
>
> **Language:** Python · **Program:** [`campus_mst.py`](campus_mst.py) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`campus_mst.py`](campus_mst.py) models a **5-building college campus** (`Gate`, `Admin`, `CSE`, `Library`, `Canteen`) connected by **7 two-way weighted roads**. With no user input needed, running the script automatically builds and prints four results:
1. **Adjacency List (`adj`):** Prints every building and its list of `(neighbor, distance)` pairs.
2. **Adjacency Matrix (`mat`):** Prints the `5 × 5` grid of edge weights (`0` where no direct road exists).
3. **Kruskal's MST:** Sorts all 7 roads by ascending distance and uses **Union-Find** to pick `4` cycle-free roads of minimum total distance (`55`).
4. **Prim's MST:** Starts at `"Gate"` and greedily grows one connected tree across `4` roads, also reaching the exact same minimum total distance (`55`).

### Exact Program Output
```text
Adjacency List:
Gate : [('Admin', 10), ('CSE', 25)]
Admin : [('Gate', 10), ('CSE', 15), ('Canteen', 16), ('Library', 20)]
CSE : [('Gate', 25), ('Admin', 15), ('Canteen', 12)]
Library : [('Admin', 20), ('Canteen', 18)]
Canteen : [('Admin', 16), ('CSE', 12), ('Library', 18)]

Adjacency Matrix:
[0, 10, 25, 0, 0]
[10, 0, 15, 20, 16]
[25, 15, 0, 0, 12]
[0, 20, 0, 0, 18]
[0, 16, 12, 18, 0]

Kruskal MST: [('Gate', 'Admin', 10), ('CSE', 'Canteen', 12), ('Admin', 'CSE', 15), ('Library', 'Canteen', 18)]
Total Weight: 55

Prim MST: [('Gate', 'Admin', 10), ('Admin', 'CSE', 15), ('CSE', 'Canteen', 12), ('Canteen', 'Library', 18)]
Total Weight: 55
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Full Form & Definition |
|---|---|
| **Graph `G = (V, E)`** | A non-linear data structure consisting of a finite set of **vertices (nodes) `V`** and a set of **edges (links) `E`** connecting pairs of vertices. |
| **Weighted Graph** | A graph in which every edge is assigned a numerical **weight / cost** (here, walking distance between campus buildings). |
| **Undirected Graph** | A graph whose edges have **no direction** (`(u, v)` is identical to `(v, u)` — two-way roads). Its adjacency matrix is always symmetric (`mat[i][j] == mat[j][i]`). |
| **Cycle** | A closed path that starts and ends at the same vertex without repeating edges. |
| **Sparse vs. Dense Graph** | **Sparse:** few edges (`E ≈ V`). **Dense:** edge count close to maximum possible (`E ≈ V²`, max = `V(V - 1) / 2`). |
| **Adjacency List** | Graph representation mapping each vertex to a list of its directly connected neighbors. Space: **`O(V + E)`**. |
| **Adjacency Matrix** | A `V × V` 2D array where `mat[i][j] = w` if an edge of weight `w` exists between `i` and `j`, else `0`. Space: **`O(V²)`**. |
| **Spanning Tree** | A connected, acyclic (cycle-free) subgraph that includes **all `V` vertices** of `G` and contains **exact edge count `V - 1`**. |
| **MST** | **Full Form:** *Minimum Spanning Tree* — a spanning tree of a weighted connected undirected graph having the **minimum possible sum of edge weights**. |
| **DSU (Union-Find)** | **Full Form:** *Disjoint Set Union* — a data structure tracking non-overlapping sets via `find` (locate set root) and `union` (merge two sets), used by Kruskal's algorithm to detect cycles. |
| **Greedy Algorithm** | An algorithm that makes the locally cheapest valid choice at every step; both Kruskal's and Prim's are **greedy** algorithms guaranteed to find the global MST. |

---

## 3. Core Rules, Comparisons & Real-World Uses

### Fundamental MST Facts (High-Probability Exam Questions)
1. **Number of vertices in MST:** `V` (`5` buildings).
2. **Number of edges in MST:** Always **`V - 1`** (`5 - 1 = 4` edges). Adding any `V`-th edge **always** creates a cycle.
3. **Uniqueness:** A graph can have multiple different MSTs if edge weights tie, **but every MST of a graph has the exact same minimum total weight** (`55` here).
4. **Negative weights:** Both Kruskal and Prim work **correctly** even if a graph contains negative edge weights.

### Comparison 1: Adjacency Matrix vs. Adjacency List

| Parameter | Adjacency Matrix (`V × V`) | Adjacency List |
|---|---|---|
| **Space Complexity** | **`O(V²)`** | **`O(V + E)`** |
| **Check if edge `(u, v)` exists** | **`O(1)`** | `O(degree(u))` |
| **Find all neighbors of `u`** | `O(V)` | **`O(degree(u))`** |
| **Best For** | **Dense graphs** | **Sparse graphs** |

### Comparison 2: Kruskal's Algorithm vs. Prim's Algorithm

| Parameter | Kruskal's Algorithm | Prim's Algorithm |
|---|---|---|
| **Greedy Approach** | **Edge-based:** sorts all edges by weight; merges components (forest → tree) | **Vertex-based:** grows **one single connected tree** outward from `start` |
| **Cycle Detection** | **Union-Find (DSU)** (`find(u) != find(v)`) | **`vis` set** (picks edge with 1 endpoint inside `vis` and 1 outside) |
| **Standard Time Complexity** | **`O(E log E)`** (or `O(E log V)`) | **`O(E log V)`** (with Min-Heap) / **`O(V²)`** (with Matrix) |
| **Time in `campus_mst.py`** | `O(E log E + E · V)` | `O(V · E)` (simple edge scan without heap) |
| **Best Suited For** | **Sparse graphs** | **Dense graphs** |

### Real-World Uses / Applications of MST
1. **Network cabling** — laying minimum campus fiber-optic, LAN, telephone, or TV cables connecting all buildings.
2. **Civil & utility infrastructure** — designing minimum-cost electrical power grids, water pipelines, gas lines, and road networks.
3. **Cluster analysis** in data mining / machine learning (removing heaviest MST edges separates clusters).
4. **Approximation algorithms** for NP-hard routing problems like the Metric Travelling Salesperson Problem (TSP).

---

## 4. Step-by-Step Algorithms

### Kruskal's Algorithm
1. Initialize `V` disjoint sets `p = [0, 1, ..., V - 1]` (each vertex is its own parent).
2. Sort all `E` edges in ascending order of weight `w`.
3. For each `(u, v, w)` in sorted edges:
   - Find roots `ru = find(p, u)` and `rv = find(p, v)`.
   - If `ru != rv` (different sets → **no cycle**): merge sets (`p[rv] = ru`), add `(u, v, w)` to `mst`, and add `w` to `total`.
   - Else (`ru == rv` → **cycle**): reject edge.
4. Return `mst` (contains `V - 1` edges) and `total`.

### Prim's Algorithm
1. Initialize `vis = [start]`, `mst = []`, `total = 0`.
2. Repeat while `len(vis) < V`:
   - Scan edges to find the minimum-weight edge `best = (u_in, v_out, w)` having **one endpoint inside `vis`** and **one endpoint outside `vis`**.
   - Append `v_out` to `vis`, append `best` to `mst`, and add `w` to `total`.
3. Return `mst` and `total`.

---

## 5. Line-by-Line Code Explanation

| Code Section | Exact Role in `campus_mst.py` |
|---|---|
| `buildings = [...]` & `edges = [...]` | Defines the `5` vertex names (`n = 5`) and `7` `(u, v, weight)` undirected road tuples. |
| `idx = {buildings[i]: i for i in range(n)}` | Dictionary mapping building names to matrix indices `0..4` (`Gate:0, Admin:1, CSE:2, Library:3, Canteen:4`). |
| `adj = {b: [] ...}` & `mat = [[0] * n for _ in range(n)]` | Initializes empty Adjacency List dict and `5 × 5` zeroed Adjacency Matrix. |
| `for u, v, w in edges:` | Adds both `(v, w)` to `adj[u]` and `(u, w)` to `adj[v]`, and sets `mat[u][v] = mat[v][u] = w` (undirected symmetry). |
| `def find(p, i): while p[i] != i: i = p[i]` | Walks parent pointers up to the root representative of vertex `i`'s component in Union-Find. |
| `sorted(edges, key=lambda e: e[2])` | Sorts edges by weight `e[2]` ascending (`10, 12, 15, 16, 18, 20, 25`). |
| `if ru != rv: p[rv] = ru ...` | Keeps edge only if endpoints belong to different components, then unions the two components. |
| `if u in vis and v not in vis ... elif v in vis and u not in vis` | In `prim(start)`, checks edges crossing the boundary of `vis` in either direction and picks the smallest `w`. |

---

## 6. Step-by-Step Dry Run (Kruskal's Cycle Rejection)

| Sorted Edge | Weight `w` | Check `ru != rv` | Action & Reason | Running Total |
|---|---|---|---|---|
| `Gate – Admin` | `10` | `0 != 1` (True) | **Keep** (`{Gate, Admin}`) | `10` |
| `CSE – Canteen` | `12` | `2 != 4` (True) | **Keep** (`{CSE, Canteen}`) | `22` |
| `Admin – CSE` | `15` | `0 != 2` (True) | **Keep** (`{Gate, Admin, CSE, Canteen}`) | `37` |
| **`Admin – Canteen`** | **`16`** | **`0 == 0` (False)** | **SKIP — forms cycle `Admin–CSE–Canteen`!** | `37` |
| `Library – Canteen` | `18` | `3 != 0` (True) | **Keep** — 4th edge (`V - 1 = 4`), all 5 connected! | **`55`** |
| `Admin – Library` | `20` | `3 == 3` (False) | Skip (cycle) | `55` |
| `Gate – CSE` | `25` | `3 == 3` (False) | Skip (cycle) | `55` |

---

## 7. Important Exam Points & Common Mistakes

- **Exam Fact:** A cheaper edge (`Admin–Canteen`, weight `16`) can still be **rejected** if its endpoints are already connected, because adding it closes a cycle.
- **Mistake 1:** Storing an undirected edge in only one direction (`mat[u][v] = w` without `mat[v][u] = w`).
- **Mistake 2:** Writing `mat = [[0] * n] * n` in Python (shares the same row list 5 times!). Always write `[[0] * n for _ in range(n)]`.

---

## 8. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | What are the full forms of MST and DSU? | **MST:** Minimum Spanning Tree. **DSU:** Disjoint Set Union (also called Union-Find). |
| 2 | Define a Spanning Tree and a Minimum Spanning Tree (MST). | A **Spanning Tree** connects all `V` vertices of a graph with `V - 1` edges and no cycles. An **MST** is a spanning tree with the minimum total edge weight. |
| 3 | How many edges are in an MST of `V` vertices (and for 5 buildings)? | Always **`V - 1` edges** (`4` edges for `5` buildings). |
| 4 | State the space complexity of Adjacency Matrix vs. Adjacency List. | Adjacency Matrix: **`O(V²)`**. Adjacency List: **`O(V + E)`**. |
| 5 | Which graph representation is better for sparse graphs, and which for dense graphs? | **Adjacency List** is better for sparse graphs; **Adjacency Matrix** is better for dense graphs (and `O(1)` edge existence checks). |
| 6 | State the standard time complexities of Kruskal's and Prim's algorithms. | Kruskal's: **`O(E log E)`** (or `O(E log V)`). Prim's: **`O(E log V)`** using a Min-Heap (or `O(V²)` with an adjacency matrix scan). |
| 7 | Which algorithmic paradigm do both Kruskal's and Prim's follow? | **Greedy Algorithm**. |
| 8 | How does Kruskal's algorithm detect cycles? | Using **Union-Find (DSU)**: if `find(u) == find(v)`, both vertices are already in the same connected component, so adding edge `(u, v)` creates a cycle. |
| 9 | State the key difference between Kruskal's and Prim's algorithms. | Kruskal sorts edges globally and merges disconnected components (good for **sparse** graphs); Prim grows **one connected tree** from a starting vertex (good for **dense** graphs). |
| 10 | Does changing the starting vertex in Prim's algorithm change the MST's total weight? | **No** — every starting vertex in a connected undirected graph yields the exact same minimum total weight (`55`). |
| 11 | Can an MST exist for a disconnected graph? | No single spanning tree exists for a disconnected graph (Kruskal instead finds a Minimum Spanning **Forest**, one MST per connected component). |
| 12 | Give three real-world applications/uses of MST. | (1) Laying campus/city internet & telephone cables, (2) designing electrical power grids and water pipe networks, and (3) data clustering. |
