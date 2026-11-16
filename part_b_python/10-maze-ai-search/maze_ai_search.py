import heapq

maze = [
    "###########",
    "#.........#",
    "#.#######.#",
    "#...S.....#",
    "#.#######.#",
    "#.......#G#",
    "###########",
]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_pos(grid, ch):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == ch:
                return (r, c)


def neighbors(grid, cell):
    r, c = cell
    res = []
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
            res.append((nr, nc))
    return res


def get_path(par, goal):
    if goal not in par:
        return []
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = par[cur]
    return path[::-1]


def bfs(grid, start, goal):
    q = [start]
    par = {start: None}
    seen = []
    while q:
        cur = q.pop(0)
        seen.append(cur)
        if cur == goal:
            return get_path(par, goal), seen
        for nxt in neighbors(grid, cur):
            if nxt not in par:
                par[nxt] = cur
                q.append(nxt)
    return [], seen


def astar(grid, start, goal):
    h = [(abs(start[0] - goal[0]) + abs(start[1] - goal[1]), 0, start)]
    par = {start: None}
    cost = {start: 0}
    seen = []
    closed = set()
    while h:
        f, g, cur = heapq.heappop(h)
        if cur in closed:
            continue
        closed.add(cur)
        seen.append(cur)
        if cur == goal:
            return get_path(par, goal), seen
        for nxt in neighbors(grid, cur):
            ng = g + 1
            if nxt not in cost or ng < cost[nxt]:
                cost[nxt] = ng
                par[nxt] = cur
                nf = ng + abs(nxt[0] - goal[0]) + abs(nxt[1] - goal[1])
                heapq.heappush(h, (nf, ng, nxt))
    return [], seen


def show(grid, path, seen):
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[0])):
            ch = grid[r][c]
            if ch in ("S", "G"):
                line += ch
            elif (r, c) in path:
                line += "*"
            elif (r, c) in seen:
                line += "."
            else:
                line += "#" if ch == "#" else " "
        print(line)


grid = [list(r) for r in maze]
start, goal = find_pos(grid, "S"), find_pos(grid, "G")

p1, s1 = bfs(grid, start, goal)
print("BFS (moves:", len(p1) - 1, "explored:", len(s1), ")")
show(grid, p1, s1)

p2, s2 = astar(grid, start, goal)
print("\nA* (moves:", len(p2) - 1, "explored:", len(s2), ")")
show(grid, p2, s2)

print("\nDynamic Maze Re-planning:")
pos = start
steps = 0
blocked = False
while pos != goal:
    path, _ = bfs(grid, pos, goal)
    if not path:
        print("No path")
        break
    if not blocked and len(path) > 2:
        wall = path[2]
        pos = path[1]
        steps += 1
        grid[wall[0]][wall[1]] = "#"
        blocked = True
        print("Wall appeared at", wall, "-> replanning from", pos)
    else:
        steps += len(path) - 1
        pos = goal
        show(grid, path, [])
print("Total moves:", steps)
