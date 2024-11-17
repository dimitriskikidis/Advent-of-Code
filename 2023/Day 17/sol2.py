import heapq

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [list(map(int, line.replace('\n', ''))) for line in lines]
width, height = len(grid[0]), len(grid)

visited = set()
q = [(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)]
heapq.heapify(q)

while q:
    heat, row, col, dr, dc, steps = heapq.heappop(q)

    if row == height - 1 and col == width - 1 and steps >= 4:
        print(heat)
        break

    if (row, col, dr, dc, steps) in visited:
        continue

    visited.add((row, col, dr, dc, steps))

    if steps < 10:
        nr = row + dr
        nc = col + dc
        if (0 <= nr < height) and (0 <= nc < width):
            heapq.heappush(q, (heat + grid[nr][nc], nr, nc, dr, dc, steps + 1))
    
    if 4 <= steps:
        for ndr, ndc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if (ndr, ndc) not in [(dr, dc), (-dr, -dc)]:
                nr = row + ndr
                nc = col + ndc
                if (0 <= nr < height) and (0 <= nc < width):
                    heapq.heappush(q, (heat + grid[nr][nc], nr, nc, ndr, ndc, 1))
