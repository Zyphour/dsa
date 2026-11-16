# Practical 10: Maze Navigation using AI Search — Complete Reference & Code Guide (`maze_ai_search.py`)

> **Aim:** Find the optimal path from `S` to `G` in a maze using AI search algorithms, handle a maze that changes while the agent walks, and visualise the process.
>
> **Language:** Python · **Program:** [`maze_ai_search.py`](maze_ai_search.py) · **Theory Summary:** [`THEORY.md`](THEORY.md)

---

## 1. What This Code Is Supposed to Do

[`maze_ai_search.py`](maze_ai_search.py) solves a **7 × 11 grid maze** from Start `S = (3, 4)` to Goal `G = (5, 9)` (where `#` = wall, `.` = open corridor) across **three automated demonstrations** and prints ASCII maps (`*` = chosen path, `.` = explored cells):
1. **Static BFS (Breadth-First Search):** Finds the optimal **7-move** shortest path using a FIFO queue, exploring **21 cells** because it expands blindly in all directions.
2. **Static A\* (A-Star Search):** Finds the **exact same 7-move** shortest path using a Min-Heap (`heapq`) guided by **Manhattan distance (`f = g + h`)**, exploring **only 8 cells**.
3. **Dynamic Maze Re-Planning:** Walks 1 step from `(3, 4)` to `(3, 5)`, places a new dynamic wall `#` right ahead at `(3, 6)` blocking the shortcut, **re-runs BFS from `(3, 5)`** to route around the upper corridor, and reaches `G` in **19 total moves**.

### Exact Program Output
```text
BFS (moves: 7 explored: 21 )
###########
#...     .#
#.#######.#
#...S*****#
#.#######*#
#...    #G#
###########

A* (moves: 7 explored: 8 )
###########
#         #
# ####### #
#   S*****#
# #######*#
#       #G#
###########

Dynamic Maze Re-planning:
Wall appeared at (3, 6) -> replanning from (3, 5)
###########
#*********#
#*#######*#
#***S*#  *#
# #######*#
#       #G#
###########
Total moves: 19
```

---

## 2. Definitions, Full Forms & Key Terminology

| Term / Abbreviation | Full Form & Definition |
|---|---|
| **AI** | **Full Form:** *Artificial Intelligence*. |
| **BFS** | **Full Form:** *Breadth-First Search* — an **uninformed (blind)** graph search algorithm using a **FIFO Queue** that explores vertices level by level in order of distance from the start. Guarantees shortest path when all edge costs are equal (`1`). |
| **DFS** | **Full Form:** *Depth-First Search* — an uninformed search using a **LIFO Stack** (or recursion) that explores deep along one branch before backtracking. Does **NOT** guarantee shortest path. |
| **UCS** | **Full Form:** *Uniform-Cost Search* (equivalent to **Dijkstra's Algorithm**) — expands the node with lowest cumulative path cost `g(n)`; optimal on weighted graphs with non-negative weights. |
| **A\* (A-Star Search)** | An **informed (heuristic) best-first search** algorithm using a **Priority Queue (Min-Heap)** ordered by **`f(n) = g(n) + h(n)`**. Guarantees an optimal shortest path whenever `h(n)` is **admissible**. |
| **`g(n)` (Path Cost)** | Exact cost (number of moves) already incurred from `start` to current cell `n`. |
| **`h(n)` (Heuristic Function)** | Problem-specific estimate of the remaining cost from cell `n` to `goal`. |
| **`f(n) = g(n) + h(n)`** | Evaluation function in A\*: estimated total cost of the cheapest path from `start` to `goal` passing through `n`. |
| **Manhattan Distance** | Heuristic for 4-directional grids (Up/Down/Left/Right only): **`|r1 - r2| + |c1 - c2|`** (sum of absolute row and column differences). |
| **Admissible Heuristic** | A heuristic `h(n)` that **never overestimates** the true shortest remaining cost (`0 <= h(n) <= h*(n)` for every state `n`). Required for A\* optimality! |
| **Uninformed vs. Informed Search** | **Uninformed (Blind):** uses no goal-distance estimate (`BFS`, `DFS`, `UCS`). **Informed (Heuristic):** uses `h(n)` to guide search toward the goal (`A*`, Greedy Best-First). |
| **Online Re-Planning** | Re-running search from the agent's **current position** whenever the environment/map changes dynamically mid-execution (e.g., new obstacle appears). |
| **GPS** | **Full Form:** *Global Positioning System* (uses A\* / Dijkstra + dynamic traffic re-planning in map navigation apps). |

---

## 3. Core Facts, Rules, Comparisons & Uses

### Essential Search Facts for Exams
1. **Maze as a State-Space Graph:**
   - **State / Vertex (`V`):** Open grid cell `(r, c)`.
   - **Action / Edge (`E`):** Up, Down, Left, Right move into a non-wall cell (each free cell has `<= 4` edges, so `E = O(V)`).
   - **Step Cost:** `1` per move → unweighted graph → **fewest moves = shortest path**.
2. **Why BFS Marks Visited on Enqueue (NOT on Pop):**
   - Recording `nxt` in `par` **when appending to `q`** prevents surrounding neighbors from adding the same cell to `q` multiple times.
3. **Why A\* Beat BFS (`8` explored vs. `21` explored):**
   - Both find the optimal **7-move** path, *but* BFS expands blindly leftward and upward, whereas Manhattan `h` directs A\* straight toward `G`.
   - Note: Setting **`h(n) = 0`** turns A\* into plain **Dijkstra / BFS**!
4. **Parent Table (`par`):** Maps `child → parent` (`par[start] = None`) so `get_path` retraces `goal → start` and reverses to recover the shortest path.

### Comparison: BFS vs. DFS vs. Dijkstra vs. A\*

| Parameter | BFS | DFS | Dijkstra (UCS) | A\* Search |
|---|---|---|---|---|
| **Category** | Uninformed | Uninformed | Uninformed | **Informed (Heuristic)** |
| **Data Structure** | **FIFO Queue** | LIFO Stack | Min-Heap (`g`) | **Min-Heap (`f = g + h`)** |
| **Uses Goal Position?** | No | No | No | **Yes (`h` = Manhattan)** |
| **Optimal Shortest Path?** | **Yes** (unit step cost) | **No** | **Yes** (`w >= 0`) | **Yes** (admissible `h`) |
| **Time Complexity** | **`O(V + E)`** | `O(V + E)` | `O(E log V)` | **`O(E log V)`** |
| **Space Complexity** | **`O(V)`** | `O(V)` | `O(V)` | **`O(V)`** |
| **Demo Path / Cells Explored** | `7` moves / **`21` cells** | Not optimal | `7` moves / `21` cells | `7` moves / **`8` cells** |

### Real-World Uses / Applications of BFS, A\* & Re-Planning
1. **GPS & Map Navigation** (Google Maps / Apple Maps route planning + live traffic/roadblock re-routing).
2. **Robotics & Autonomous Vehicles / Warehouse Robots** navigating around moving obstacles.
3. **Video Game AI Pathfinding** (NPC characters finding shortest paths around terrain using A\*).
4. **Network routing** (shortest hop count via BFS / OSPF) and **puzzle solvers** (8-puzzle, Rubik's cube).

---

## 4. Step-by-Step Algorithms

### 1. `bfs(grid, start, goal)`
1. Initialize FIFO queue `q = [start]`, parent dict `par = {start: None}`, and `seen = []`.
2. While `q` is non-empty:
   - Pop front cell `cur = q.pop(0)` and append to `seen`.
   - If `cur == goal`, reconstruct path from `par` and return `(path, seen)`.
   - For each valid open 4-neighbor `nxt` of `cur`:
     - If `nxt not in par`, set `par[nxt] = cur` and `q.append(nxt)`.
3. If `q` empties without reaching `goal`, return `([], seen)`.

### 2. `astar(grid, start, goal)`
1. Push `(h(start), 0, start)` onto Min-Heap `h`; set `par = {start: None}`, `cost = {start: 0}`, `closed = set()`.
2. While `h` is non-empty:
   - Pop smallest-`f` entry `(f, g, cur) = heapq.heappop(h)`.
   - If `cur in closed`, skip (`continue`); else add `cur` to `closed` and `seen`.
   - If `cur == goal`, return `(get_path(par, goal), seen)`.
   - For each valid neighbor `nxt`: let `ng = g + 1`; if `nxt not in cost` or `ng < cost[nxt]`, update `cost[nxt] = ng`, `par[nxt] = cur`, compute `nf = ng + Manhattan(nxt, goal)`, and push `(nf, ng, nxt)` onto `h`.
3. Return `([], seen)` if unreachable.

### 3. Dynamic Re-Planning Loop
1. Start at `pos = start`. While `pos != goal`:
   - Run `bfs(grid, pos, goal)` from **current `pos`**. If `path` is empty, print `"No path"` and stop.
   - Step along `path`; if a dynamic obstacle `#` appears ahead on `grid`, repeat loop from current `pos` to compute a new detour!

---

## 5. Function-by-Function Code Explanation

| Function / Block in `maze_ai_search.py` | Exact Role |
|---|---|
| `import heapq` | Python standard-library **Min-Heap** priority queue module used by `astar`. |
| `moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]` | Row/column offsets `(dr, dc)` for Up, Down, Left, and Right. |
| `find_pos(grid, ch)` | Scans `grid` to return `(row, col)` coordinates of `'S'` (`(3, 4)`) and `'G'` (`(5, 9)`). |
| `neighbors(grid, cell)` | Returns list of adjacent `(nr, nc)` cells that are inside grid bounds and not `'#'` walls. |
| `get_path(par, goal)` | Follows `cur = par[cur]` from `goal` back to `start` (`None`) and reverses with `path[::-1]`. Move count = `len(path) - 1`. |
| `bfs(grid, start, goal)` | FIFO queue search returning `(shortest_path, explored_cells)`. |
| `astar(grid, start, goal)` | Min-Heap search ordering states by `(f, g, cell)` where `f = g + |r - goal_r| + |c - goal_c|`. |
| `show(grid, path, seen)` | Prints ASCII grid: `S`/`G` endpoints, `*` for path cells, `.` for explored non-path cells, `#` for walls. |
| `grid = [list(r) for r in maze]` | Converts immutable strings into mutable character lists so dynamic walls (`grid[r][c] = "#"`) can be written. |
| `while pos != goal:` *(bottom)* | Simulates stepping from `(3, 4)` to `(3, 5)`, spawning a `#` wall at `(3, 6)`, and re-planning from `(3, 5)` (`19` total moves). |

---

## 6. Time & Space Complexity Fact Sheet

For a maze with `V` open cells and `E` legal transitions (`E <= 4V`, so `E = O(V)`):

| Algorithm | Time Complexity | Space Complexity | Optimal? |
|---|---|---|---|
| **BFS** | **`O(V + E)`** (`O(rows × cols)`) | **`O(V)`** (`q` + `par`) | **Yes** (equal step cost `1`) |
| **A\* (with Binary Min-Heap `heapq`)** | **`O(E log V)`** *(explores far fewer states in practice!)* | **`O(V)`** (`h` + `par` + `cost` + `closed`) | **Yes** (admissible Manhattan `h`) |
| **Dynamic Re-Planning (`k` map changes)** | `O(k · (V + E))` (re-runs BFS on obstacle event) | **`O(V)`** | Locally optimal per known map |

---

## 7. Important Exam Points & Common Mistakes

- **Exam Fact 1:** BFS finds shortest paths **only on unweighted (or equal-step-cost) graphs**; weighted graphs require Dijkstra or A\*.
- **Exam Fact 2:** If heuristic `h` **overestimates** true cost (inadmissible), A\* becomes fast like Greedy Search **but is no longer guaranteed to return the shortest path**.
- **Mistake 1:** Marking visited when popping instead of when pushing onto the BFS queue (causes duplicate states in `q`).
- **Mistake 2:** Reporting `len(path)` instead of `len(path) - 1` as the number of moves (`path` contains `start` + every step).

---

## 8. Straightforward Viva & Exam Q&A

| # | Question | Direct Answer |
|---|---|---|
| 1 | What are the full forms of AI, BFS, DFS, and UCS? | **AI:** Artificial Intelligence. **BFS:** Breadth-First Search. **DFS:** Depth-First Search. **UCS:** Uniform-Cost Search. |
| 2 | Which data structure is used by BFS, DFS, and A\* respectively? | **BFS:** FIFO Queue. **DFS:** LIFO Stack. **A\*:** Priority Queue (Min-Heap). |
| 3 | Differentiate between Uninformed Search and Informed Search with examples. | **Uninformed (Blind) Search** has no estimate of distance to the goal (e.g., BFS, DFS). **Informed (Heuristic) Search** uses a heuristic `h(n)` estimating distance to the goal (e.g., A\*). |
| 4 | Write the A\* evaluation formula and define `f(n)`, `g(n)`, and `h(n)`. | **`f(n) = g(n) + h(n)`**, where `g(n)` = actual cost from start to `n`, `h(n)` = estimated heuristic cost from `n` to goal, and `f(n)` = estimated total path cost through `n`. |
| 5 | What is the formula for Manhattan Distance between `(r1, c1)` and `(r2, c2)`? | **`|r1 - r2| + |c1 - c2|`**. |
| 6 | Define an **Admissible Heuristic** and state why it is important in A\*. | A heuristic is **admissible** if it **never overestimates** the true minimum distance to the goal (`h(n) <= h*(n)`). It guarantees that A\* finds an **optimal shortest path**. |
| 7 | State the time and space complexities of BFS and A\*. | **BFS:** `O(V + E)` time, `O(V)` space. **A\*:** `O(E log V)` time, `O(V)` space. |
| 8 | Why does BFS guarantee the shortest path in this maze? | Because every move has uniform cost `1` and BFS visits all cells at distance `d` before any cell at distance `d + 1`. |
| 9 | Why wouldn't DFS guarantee the shortest path in a maze? | DFS explores deep along one arbitrary path first and may reach the goal via a long detour (e.g., `19` moves) instead of the `7`-move shortcut. |
| 10 | What happens to A\* when `h(n) = 0`? | `f(n) = g(n)`, so A\* behaves identically to **Dijkstra's Algorithm / BFS**. |
| 11 | In our 7 × 11 maze demo, compare path length and explored cells for BFS vs. A\*. | Both found the optimal **7-move** path, but BFS explored **21 cells** whereas A\* explored only **8 cells**. |
| 12 | What is Dynamic Re-planning, and what does the program output if all paths to `G` are blocked? | Dynamic re-planning re-runs search from the agent's current cell whenever an obstacle changes the map; if `G` becomes unreachable, BFS returns `[]` and prints **`"No path"`**. |
| 13 | Give three real-world applications/uses of A\* and BFS. | (1) GPS map navigation & live traffic rerouting, (2) autonomous robot obstacle navigation, and (3) video game character pathfinding. |
