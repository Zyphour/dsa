# Code explanation — `maze_ai_search.py`

The maze is a list of strings, 15 rows × 21 columns:

```python
MAZE = [
    "#####################",
    "#S..........#.......#",   # note the gap: a loop between the top corridors
    ...
]
```

## What each function does

| Function | Job |
|---|---|
| `find_char(grid, ch)` | locate `S` or `G` → `(row, col)` |
| `inside` / `open_cell` | bounds check and "is it not a wall" |
| `neighbours(grid, cell)` | the up/down/left/right cells that can be entered |
| `rebuild_path(parent, start, goal)` | walk parent links backwards, then reverse |
| `manhattan(a, b)` | the heuristic `abs(Δrow) + abs(Δcol)` |
| `bfs(grid, start, goal)` | returns `(path, explored_order)` |
| `astar(grid, start, goal)` | same, but ordered by `f = g + h` |
| `draw(grid, path, explored, title)` | ASCII picture: `#` wall, `.` explored, `*` path |
| `pick_wall_cell(grid, path, goal)` | chooses a path cell to close that still has a detour |
| `demo_static()` | BFS vs A\* on the fixed maze |
| `demo_dynamic(animate)` | walk, drop walls, re-plan |

## BFS — the whole algorithm

```python
queue = deque([start])
parent = {start: None}          # also acts as the "visited" set

while queue:
    cell = queue.popleft()
    explored.append(cell)
    if cell == goal:
        return rebuild_path(parent, start, goal), explored
    for nxt in neighbours(grid, cell):
        if nxt not in parent:
            parent[nxt] = cell          # remember how we got here
            queue.append(nxt)
return [], explored                     # unreachable
```

`parent[nxt] = cell` is what later allows `rebuild_path` to retrace the route.

## A\* — the whole algorithm

```python
open_heap = [(manhattan(start, goal), 0, start)]     # (f, g, cell)
cost = {start: 0}
closed = set()

while open_heap:
    f, g, cell = heapq.heappop(open_heap)
    if cell in closed: continue
    closed.add(cell)
    if cell == goal: return rebuild_path(parent, start, goal), explored

    for nxt in neighbours(grid, cell):
        new_cost = g + 1
        if nxt not in cost or new_cost < cost[nxt]:
            cost[nxt] = new_cost
            parent[nxt] = cell
            heapq.heappush(open_heap,
                           (new_cost + manhattan(nxt, goal), new_cost, nxt))
```

The tuple puts `f` first so the heap orders cells by estimated total cost. `closed`
prevents expanding the same cell twice.

## Dynamic demo

```python
wall_cell = pick_wall_cell(grid, path, goal)     # a cell with a possible detour

# while walking, once the agent reaches the cell before it:
grid[ahead[0]][ahead[1]] = WALL
break                                           # go back and plan again
```

`pick_wall_cell` tries each path cell, closes it temporarily, and keeps the one
whose detour is shortest. That guarantees a wall only appears where the agent can
still get around it.

## Dry run — a 3 × 5 maze

```
S . # . .
. . # . G
```

BFS: queue `[(0,0)]` → pop, push `(0,1)`, `(1,0)` → pop `(0,1)`, push `(1,1)` →
pop `(1,0)` (nothing new) → pop `(1,1)`, push `(1,2)` → … The goal is reached at
distance 5 along `(0,0) (1,0) (1,1) (1,2) (1,3) (1,4)`.

The wall at `(0,2)` blocks the direct top route, and BFS still finds the shortest
detour because it finishes every 4-move cell before touching a 5-move cell.

## Common mistakes

- Marking cells visited when popped instead of when pushed → duplicate work.
- Omitting the `parent` table → the goal is reachable but no path can be drawn.
- Using a stack (DFS) and calling the result "shortest".
- Forgetting `if cell in closed: continue` in A\*, which expands the same cell many times.
- An inadmissible heuristic (say Manhattan × 5) — faster but no longer optimal.
- Dropping a wall without checking for a detour → the agent gets trapped.

## Viva — short answers

| Question | Answer |
|---|---|
| BFS vs DFS? | BFS uses a queue and finds shortest paths; DFS uses a stack and finds any path. |
| What is `f = g + h`? | Estimated total cost = cost so far + estimated cost remaining. |
| What is an admissible heuristic? | One that never overestimates the remaining cost. |
| Is A\* always better than BFS? | It expands fewer cells, but pays `log V` per heap operation. |
| What is re-planning? | Searching again from the current state when the environment changes. |
| Why is BFS optimal here? | Every move costs 1, so fewest moves = lowest cost. |
