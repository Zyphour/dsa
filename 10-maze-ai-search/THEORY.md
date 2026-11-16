# Practical 10 — Maze Navigation using AI Search

**Aim:** Find the optimal path from `S` to `G` in a maze using AI search
algorithms, handle a maze that changes while the agent walks, and visualise the
process.

**Language:** Python · **Program:** [`maze_ai_search.py`](maze_ai_search.py)

---

## The maze as a search problem

| Part | In our maze |
|---|---|
| State | the cell the agent stands on |
| Actions | up / down / left / right, if the cell is not a wall |
| Start / Goal | `S` and `G` |
| Step cost | 1 per move, so shortest path = fewest moves |

Each free cell is a vertex and each legal move is an edge of weight 1 — the maze
is an unweighted graph hidden inside a grid.

## BFS — Breadth First Search

Uses a **queue**. Visit the start, then everything one move away, then two moves
away, and so on. A `parent` table records how each cell was reached, so when the
goal is found we can retrace the path.

Because all cells at distance `d` are finished before any cell at distance `d+1`,
the first time the goal is reached the path is a **shortest** one.

Time `O(V+E)`, space `O(V)` for the queue and the parent table.

## A\* — A-star

Like BFS but with a **priority queue** and a hint:

```
f = g + h
g = moves already made from the start
h = estimated moves still needed  (Manhattan distance: |Δrow| + |Δcol|)
```

A\* always expands the cell with the smallest `f`, so it heads towards the goal
instead of spreading out evenly.

If `h` never overestimates the real distance (it is **admissible** — Manhattan
distance on a 4-direction grid always is), A\* still returns a shortest path.
With `h = 0` it becomes plain BFS.

## Comparison in our 7 × 11 maze

| | BFS | A\* |
|---|---|---|
| Data structure | queue | min-heap |
| Uses the goal position? | no | yes (`h`) |
| Path length found | 7 moves | 7 moves |
| Cells explored | 21 | 8 |

Both are optimal; A\* looks at fewer cells because the heuristic points it the
right way.

## Dynamic maze (re-planning)

In a dynamic maze the map changes while the agent moves — a corridor is blocked,
a door closes. The agent cannot keep using the old plan.

Approach: walk along the current path; if a new wall appears ahead, **run the
search again from the current cell** and follow the new path. This is
*re-planning*, an online search problem.

In the demo a wall appears at `(3, 6)` after the first step, so the agent needs
**19 moves instead of 7** by re-planning around the upper corridor — reacting
costs extra distance, which is why robots prefer a known map. If no route is left,
BFS returns an empty path and the program prints `"No path"`.

## Exam points

- BFS is optimal only because every move costs the same; weighted maps need
  Dijkstra.
- Mark a cell visited when it is **added** to the queue, not when it leaves,
  otherwise cells are queued many times.
- The `parent` table is what makes drawing the path possible.
- A\* = BFS + priority queue + heuristic; an inadmissible heuristic makes it fast
  but no longer optimal.
- DFS would find *a* path, not the shortest one.
