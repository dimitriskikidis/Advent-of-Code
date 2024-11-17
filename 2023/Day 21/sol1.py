from collections import deque

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [line.strip() for line in lines]
width, height = len(grid[0]), len(grid)

for i, row in enumerate(grid):
    j = row.find('S')
    if j != -1:
        S = (i, j)
        break

seen = set()
q = deque()
q.append((*S, 0))
seen.add(S)
result = 1

while q:
    r, c, n = q.popleft()

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if (0 <= nr < height) and (0 <= nc < width) and grid[nr][nc] != '#' and n < 64:
            key = (nr, nc)
            if key not in seen:
                if n % 2 == 1:
                    result += 1
                seen.add(key)
                q.append((*key, n + 1))

print(result)
