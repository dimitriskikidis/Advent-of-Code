from heapq import heappush, heappop

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [list(map(int, line.replace('\n', ''))) for line in lines]
width, height = len(grid[0]), len(grid)
target = (height - 1, width - 1)
visited = {(0, 0, 0, 1, 0): 0, (0, 0, 1, 0, 0): 0}
q = []
heappush(q, (0, 0, 0, 0, 1, 0))
heappush(q, (0, 0, 0, 1, 0, 0))

while q:
    heat, row, col, dr, dc, steps = heappop(q)

    if (row, col) == target:
        print(heat)
        break
    
    if heat > visited[(row, col, dr, dc, steps)]:
        continue

    dirs = []

    if steps < 3:
        dirs.append((dr, dc))
    
    dirs.append((-dc, dr))
    dirs.append((dc, -dr))
    
    for ndr, ndc in dirs:
        nr = row + ndr
        nc = col + ndc
        if (0 <= nr < height) and (0 <= nc < width):
            s = steps + 1 if (ndr, ndc) == (dr, dc) else 1
            newHeat = heat + grid[nr][nc]
            key = (nr, nc, ndr, ndc, s)
            if key not in visited or newHeat < visited[key]:
                visited[key] = newHeat
                heappush(q, (newHeat, *key))
