# Code explanation — `maze_ai_search.py`

7 × 11 grid maze solved directly with BFS, A\*, and dynamic wall re-planning:

```python
maze = [
    "###########",
    "#.........#",
    "#.#######.#",
    "#...S.....#",
    "#.#######.#",
    "#.......#G#",
    "###########",
]
```

## Functions

| Function | Job |
|---|---|
| `find_pos(grid, ch)` | finds `(r, c)` of `"S"` or `"G"` |
| `neighbors(grid, cell)` | returns open 4-directional neighbours (`!= "#"`) |
| `get_path(par, goal)` | traces `par` links backwards from `goal` to `start` and reverses |
| `bfs(grid, start, goal)` | FIFO queue search returning `(path, seen)` |
| `astar(grid, start, goal)` | min-heap search ordered by `f = g + Manhattan(cell, goal)` |
| `show(grid, path, seen)` | prints maze with `*` for path and `.` for explored cells |

## Static comparison (`S = (3, 4)`, `G = (5, 9)`)

- **BFS**: finds optimal 7-move path along the right corridor, exploring `21` cells (spreading left as well).
- **A\***: finds the same 7-move path while exploring only `8` cells, guided directly toward `G` by Manhattan distance.

## Dynamic re-planning

```python
while pos != goal:
    path, _ = bfs(grid, pos, goal)
    if not blocked and len(path) > 2:
        wall = path[2]
        pos = path[1]
        steps += 1
        grid[wall[0]][wall[1]] = "#"
        blocked = True
    else:
        steps += len(path) - 1
        pos = goal
```

After 1 step to `(3, 5)`, a `#` wall appears ahead at `(3, 6)`. On the next
iteration BFS re-plans from `(3, 5)` around the upper corridor and reaches `G`
in `19` total moves.

## Viva — short answers

| Question | Answer |
|---|---|
| Why does BFS guarantee shortest path here? | Every move has unit cost 1 and BFS explores in increasing distance order. |
| What is `f = g + h` in A\*? | `g` = steps from start, `h` = Manhattan distance heuristic to goal. |
| When is A\* optimal? | Whenever `h` is admissible (never overestimates true remaining steps). |
| What is re-planning? | Running search again from the agent's current cell when the map changes. |
