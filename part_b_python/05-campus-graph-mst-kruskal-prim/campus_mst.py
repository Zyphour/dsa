"""
EXPERIMENT 5 : Minimum Spanning Tree of a College Campus Graph
--------------------------------------------------------------
Part B - Python

The campus is modelled as a weighted undirected graph:
    NODES (vertices) : departments / buildings
    LINKS (edges)    : walking distance in metres between two buildings

Goal: connect every building with the least total cable/walkway length and
no cycles -> that cheapest connection set is the MINIMUM SPANNING TREE (MST).

Two classic greedy algorithms are implemented and compared:
    a) KRUSKAL'S : sort all edges by weight, keep an edge if it does not
                   form a cycle (checked with Union-Find / DSU)
    b) PRIM'S    : start from one node, always grow the tree with the
                   cheapest edge that connects a new node

Both must give the same total distance (a graph can have many different
MSTs, but they all have the same total weight).

Run: python3 campus_mst.py
"""

import heapq

# ----------------------------------------------------------------------
# 1. THE CAMPUS GRAPH
#    (building1, building2, distance in metres)
# ----------------------------------------------------------------------
BUILDINGS = [
    "Main Gate", "Admin", "CSE", "IT", "ENTC",
    "Library", "Canteen", "Hostel", "Sports"
]

EDGES = [
    ("Main Gate", "Admin", 120),
    ("Main Gate", "CSE", 300),
    ("Main Gate", "Hostel", 450),
    ("Admin", "CSE", 180),
    ("Admin", "Library", 200),
    ("Admin", "Hostel", 420),
    ("CSE", "IT", 90),
    ("CSE", "ENTC", 160),
    ("CSE", "Library", 250),
    ("IT", "ENTC", 140),
    ("IT", "Library", 220),
    ("ENTC", "Library", 260),
    ("ENTC", "Sports", 300),
    ("Library", "Canteen", 170),
    ("Library", "Sports", 210),
    ("Canteen", "Hostel", 230),
    ("Canteen", "Sports", 150),
    ("Hostel", "Sports", 280),
]

INDEX = {name: i for i, name in enumerate(BUILDINGS)}


# ----------------------------------------------------------------------
# 2. GRAPH REPRESENTATIONS
# ----------------------------------------------------------------------
def build_adjacency_list():
    """node -> list of (neighbour, distance)"""
    graph = {name: [] for name in BUILDINGS}
    for a, b, w in EDGES:
        graph[a].append((b, w))
        graph[b].append((a, w))            # undirected: both ways
    return graph


def build_adjacency_matrix():
    """a V x V table; 0 means 'no direct road', diagonal is 0 too"""
    n = len(BUILDINGS)
    matrix = [[0] * n for _ in range(n)]
    for a, b, w in EDGES:
        i, j = INDEX[a], INDEX[b]
        matrix[i][j] = w
        matrix[j][i] = w
    return matrix


def print_graph():
    print("\n--- Adjacency list ---")
    for name in BUILDINGS:
        neighbours = ", ".join(f"{n}({w}m)" for n, w in adj_list[name])
        print(f"  {name:<10}: {neighbours}")

    print("\n--- Adjacency matrix (0 = no direct road) ---")
    short = ["MG", "AD", "CS", "IT", "EC", "LB", "CT", "HS", "SP"]
    print(" " * 12 + "".join(f"{s:>6}" for s in short))
    for i, name in enumerate(BUILDINGS):
        row = "".join(f"{matrix[i][j]:>6}" for j in range(len(BUILDINGS)))
        print(f"  {name:<10}{row}")


# ----------------------------------------------------------------------
# 3. UNION-FIND (DSU) - used by Kruskal to detect cycles
# ----------------------------------------------------------------------
parent = list(range(len(BUILDINGS)))
rank = [0] * len(BUILDINGS)


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]       # path compression
        x = parent[x]
    return x


def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False                        # already in the same set -> cycle
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1
    return True


# ----------------------------------------------------------------------
# 4. KRUSKAL'S ALGORITHM  - O(E log E)
# ----------------------------------------------------------------------
def kruskal():
    global parent, rank
    parent = list(range(len(BUILDINGS)))    # reset DSU
    rank = [0] * len(BUILDINGS)

    mst = []
    total = 0
    rejected = []

    for a, b, w in sorted(EDGES, key=lambda e: e[2]):   # cheapest first
        if union(INDEX[a], INDEX[b]):
            mst.append((a, b, w))
            total += w
        else:
            rejected.append((a, b, w))
        if len(mst) == len(BUILDINGS) - 1:              # V-1 edges = done
            break

    return mst, total, rejected


# ----------------------------------------------------------------------
# 5. PRIM'S ALGORITHM  - O(E log V) with a min-heap
# ----------------------------------------------------------------------
def prim(start="Main Gate"):
    visited = set([start])
    heap = [(w, start, b) for b, w in adj_list[start]]
    heapq.heapify(heap)

    mst = []
    total = 0

    while heap and len(visited) < len(BUILDINGS):
        w, a, b = heapq.heappop(heap)        # cheapest edge leaving the tree
        if b in visited:
            continue                        # would create a cycle
        visited.add(b)
        mst.append((a, b, w))
        total += w
        for nxt, weight in adj_list[b]:
            if nxt not in visited:
                heapq.heappush(heap, (weight, b, nxt))

    return mst, total


# ----------------------------------------------------------------------
# 6. OUTPUT
# ----------------------------------------------------------------------
def show_mst(title, mst, total):
    print(f"\n--- {title} ---")
    print(f"{'FROM':<12}{'TO':<12}{'DISTANCE':>10}")
    for a, b, w in mst:
        print(f"{a:<12}{b:<12}{w:>8} m")
    print(f"{'TOTAL':<24}{total:>8} m")
    print(f"Edges in MST: {len(mst)}  (should be V-1 = {len(BUILDINGS) - 1})")


adj_list = build_adjacency_list()
matrix = build_adjacency_matrix()

if __name__ == "__main__":
    print("COLLEGE CAMPUS GRAPH")
    print(f"Buildings = {len(BUILDINGS)},  Roads = {len(EDGES)}")
    print_graph()

    k_mst, k_total, rejected = kruskal()
    show_mst("KRUSKAL'S MST", k_mst, k_total)
    print("\nEdges rejected by Kruskal (they would create a cycle):")
    for a, b, w in rejected:
        print(f"  {a} - {b} ({w} m)")

    p_mst, p_total = prim()
    show_mst("PRIM'S MST (started at Main Gate)", p_mst, p_total)

    print("\n--- COMPARISON ---")
    print(f"Kruskal total = {k_total} m")
    print(f"Prim    total = {p_total} m")
    if k_total == p_total:
        print("Both algorithms found an MST with the SAME total distance.")
    print("\nKruskal: global edge sorting + union-find -> good for sparse graphs.")
    print("Prim   : grows one tree from a start node -> good for dense graphs.")
