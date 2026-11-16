"""
EXPERIMENT 10 : AI Search - Maze Navigation (BFS, A*, Dynamic Re-planning)
-------------------------------------------------------------------------
Part B - Python

An agent (a robot, or a student walking to the exam hall) must get from
S (start) to G (goal) inside a maze. Walls are '#', open cells are '.'.

Two AI search algorithms are used:

  BFS (Breadth First Search)
      Explore the maze in "rings": everything 1 step away, then everything
      2 steps away, and so on. Uses a QUEUE (FIFO).
      -> always finds the SHORTEST path (fewest moves) in an unweighted maze.

  A* (A-star)
      Like BFS but it uses a PRIORITY QUEUE ordered by
          f = g + h
          g = moves already made from the start
          h = Manhattan distance still left to the goal (the heuristic)
      -> also finds the shortest path, but usually looks at far fewer cells.

DYNAMIC maze: while the agent is walking, a new wall suddenly appears on
the planned path. The agent cannot continue, so it runs the search again
from where it is standing and follows the new path. This is called
re-planning and is how real delivery robots handle surprises.

Run: python3 maze_ai_search.py
"""

import heapq
from collections import deque

# ----------------------------------------------------------------------
# THE STATIC MAZE
# ----------------------------------------------------------------------
MAZE = [
    "#####################",
    "#S..........#.......#",   # a loop between the two top corridors
    "#.###.#.###.#.#####.#",
    "#...#.#...#.#.....#.#",
    "###.#.###.#.#####.#.#",
    "#...#.....#.......#.#",
    "#.#####.###.#####.#.#",
    "#.....#...#.....#...#",
    "#.###.#.#.#####.###.#",
    "#.#...#.#.....#...#.#",
    "#.#.###.#####.###.#.#",
    "#.#.....#.....#...#.#",
    "#.#####.#.###.#.###.#",
    "#.......#...#.....#G#",
    "#####################",
]

WALL = "#"
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]      # up, down, left, right


# ----------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------
def find_char(grid, target):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == target:
                return (r, c)
    return None


def inside(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def open_cell(grid, r, c):
    return inside(grid, r, c) and grid[r][c] != WALL


def neighbours(grid, cell):
    r, c = cell
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if open_cell(grid, nr, nc):
            yield (nr, nc)


def rebuild_path(parent, start, goal):
    """Walk backwards from the goal to the start using the parent links."""
    if goal not in parent:
        return []
    path = [goal]
    cell = goal
    while cell != start:
        cell = parent[cell]
        path.append(cell)
    path.reverse()
    return path


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# ----------------------------------------------------------------------
# SEARCH 1 : BFS  -  O(V + E)
# ----------------------------------------------------------------------
def bfs(grid, start, goal):
    queue = deque([start])          # FIFO queue
    parent = {start: None}
    explored = []                   # order in which cells were visited

    while queue:
        cell = queue.popleft()
        explored.append(cell)

        if cell == goal:
            return rebuild_path(parent, start, goal), explored

        for nxt in neighbours(grid, cell):
            if nxt not in parent:             # not visited yet
                parent[nxt] = cell            # remember how we reached it
                queue.append(nxt)

    return [], explored                       # goal is unreachable


# ----------------------------------------------------------------------
# SEARCH 2 : A*  -  O(E log V) with a binary heap
# ----------------------------------------------------------------------
def astar(grid, start, goal):
    open_heap = [(manhattan(start, goal), 0, start)]   # (f, g, cell)
    parent = {start: None}
    cost = {start: 0}                                  # g values
    explored = []
    closed = set()

    while open_heap:
        f, g, cell = heapq.heappop(open_heap)
        if cell in closed:
            continue
        closed.add(cell)
        explored.append(cell)

        if cell == goal:
            return rebuild_path(parent, start, goal), explored

        for nxt in neighbours(grid, cell):
            new_cost = g + 1
            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                parent[nxt] = cell
                priority = new_cost + manhattan(nxt, goal)
                heapq.heappush(open_heap, (priority, new_cost, nxt))

    return [], explored


# ----------------------------------------------------------------------
# VISUALISATION
# ----------------------------------------------------------------------
def draw(grid, path=(), explored=(), title=""):
    if title:
        print("\n" + title)

    path = set(path)
    explored = set(explored)

    for r in range(len(grid)):
        line = []
        for c in range(len(grid[0])):
            ch = grid[r][c]
            cell = (r, c)
            if ch == "S" or ch == "G":
                line.append(ch)
            elif cell in path:
                line.append("*")          # the final path
            elif cell in explored:
                line.append(".")          # looked at by the algorithm
            elif ch == WALL:
                line.append("#")
            else:
                line.append(" ")
        print("  " + "".join(line))

    print("  S = start   G = goal   # = wall   . = explored   * = path")


# ----------------------------------------------------------------------
# DEMO 1 : solve the static maze
# ----------------------------------------------------------------------
def demo_static():
    grid = [list(row) for row in MAZE]
    start = find_char(grid, "S")
    goal = find_char(grid, "G")

    draw(grid, title="THE MAZE")
    print(f"\nStart = {start}, Goal = {goal}")

    print("\n" + "=" * 62)
    print("BFS  (queue, explores in rings)")
    print("=" * 62)
    bfs_path, bfs_seen = bfs(grid, start, goal)
    draw(grid, bfs_path, bfs_seen, "BFS result")
    print(f"  Path length  : {len(bfs_path) - 1} moves")
    print(f"  Cells visited: {len(bfs_seen)}")

    print("\n" + "=" * 62)
    print("A*  (priority queue, heuristic = Manhattan distance)")
    print("=" * 62)
    astar_path, astar_seen = astar(grid, start, goal)
    draw(grid, astar_path, astar_seen, "A* result")
    print(f"  Path length  : {len(astar_path) - 1} moves")
    print(f"  Cells visited: {len(astar_seen)}")

    print("\n--- COMPARISON ---")
    print(f"  BFS visited {len(bfs_seen)} cells, A* visited {len(astar_seen)} cells.")
    print(f"  Both paths have {len(bfs_path) - 1} moves, so both are OPTIMAL.")
    if len(astar_seen) < len(bfs_seen):
        print("  A* was smarter: the heuristic guided it towards the goal faster.")
    print("  BFS ignores direction, so it must look at almost the whole maze.")


# ----------------------------------------------------------------------
# DEMO 2 : dynamic maze (a wall appears while the agent walks)
# ----------------------------------------------------------------------
def pick_wall_cell(grid, path, goal):
    """
    Choose ONE cell of the current path that we are allowed to close.
    A cell is only chosen if another route still exists and that detour is
    short (at most 15 extra moves), so the demo stays easy to follow.
    """
    n = len(path)
    options = []

    for i in range(4, n - 3):                 # not too close to pos or goal
        cell = path[i]
        trial = [row[:] for row in grid]
        trial[cell[0]][cell[1]] = WALL
        detour = bfs(trial, path[0], goal)[0]
        if detour:                            # another route still exists
            options.append((len(detour) - n, cell))

    if not options:
        return None                           # every cell is a dead end

    options.sort()                            # pick the shortest detour
    return options[0][1]


def demo_dynamic(animate=False, pause=0.15):
    """
    The agent plans a path, starts walking, and from time to time a wall
    appears on the path ahead. It then runs BFS again from where it stands
    and follows the new path. This is 're-planning', the same idea real
    delivery robots use when a road is closed.
    """
    import time

    grid = [list(row) for row in MAZE]
    start = find_char(grid, "S")
    goal = find_char(grid, "G")

    pos = start
    moves_done = 0
    plans = 0
    walls_dropped = 0

    first_path = bfs(grid, start, goal)[0]
    original_length = len(first_path) - 1

    draw(grid, first_path,
         title="\nDYNAMIC MAZE - the agent follows the BFS path")
    print("  Somewhere ahead a wall will appear. The agent cannot walk")
    print("  through it, so it searches again from where it stands.\n")

    while pos != goal:
        path = bfs(grid, pos, goal)[0]
        if not path:
            print("  No path left! The agent is trapped.")
            return

        plans += 1
        if animate:
            draw(grid, path, title=f"Plan {plans}: path from {pos} to {goal}")
            time.sleep(pause)

        # pick a cell of THIS plan that may be closed later on
        wall_cell = None
        if walls_dropped < 2:
            wall_cell = pick_wall_cell(grid, path, goal)

        k = 1
        while k < len(path) and pos != goal:
            pos = path[k]
            moves_done += 1

            ahead = path[k + 1] if k + 1 < len(path) else None
            if ahead is not None and ahead == wall_cell and ahead != goal:
                grid[ahead[0]][ahead[1]] = WALL       # the maze changes
                walls_dropped += 1
                print(f"  step {moves_done:>2}: a wall appeared at {ahead}! "
                      f"Re-planning from {pos} ...")
                if animate:
                    draw(grid, [pos], title="The maze just changed")
                    time.sleep(pause)
                break                                  # go plan again

            if animate:
                draw(grid, [pos], title=f"Agent at {pos} (step {moves_done})")
                time.sleep(pause)
            k += 1

    draw(grid, [goal], title="\nFINAL MAZE - the agent reached the goal")
    print(f"  Total moves         : {moves_done}")
    print(f"  Search runs (plans) : {plans}")
    if walls_dropped:
        print(f"  The first plan needed only {original_length} moves, but walls")
        print("  appeared, so the agent had to search again and walk further.")
        print("  It always re-planned before taking another step, which is")
        print("  why it never walked into a new wall.")
    else:
        print("  No wall appeared this time, so the first plan was enough.")


# ----------------------------------------------------------------------
# MENU
# ----------------------------------------------------------------------
def main():
    while True:
        print("\n========== MAZE AI SEARCH ==========")
        print("1. Solve the static maze with BFS and A*")
        print("2. Solve the dynamic maze (walls appear while walking)")
        print("3. Solve the dynamic maze with animation")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            demo_static()
        elif choice == "2":
            demo_dynamic(animate=False)
        elif choice == "3":
            demo_dynamic(animate=True)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
