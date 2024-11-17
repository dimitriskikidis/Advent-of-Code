from copy import deepcopy
from collections import deque
from heapq import heappush, heappop

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [line.strip() for line in lines]
width, height = len(grid[0]), len(grid)
source = (0, grid[0].find('.'))
target = (height - 1, grid[-1].find('.'))
dirs = {
    '^': [(-1, 0)],
    '>': [(0, 1)],
    'v': [(1, 0)],
    '<': [(0, -1)],
    '.': [(-1, 0), (0, 1), (1, 0), (0, -1)]
}

qs = deque()
qs.append(source)
slopeDist = {}
seenSlopes = set()
seenSlopes.add(source)

while qs:
    r, c = qs.popleft()
    s = (r, c)
    seen = set()
    seen.add(s)
    slopesFound = []
    q = deque()
    q.append((r, c, 0))
    
    while q:
        r, c, dist = q.popleft()

        adj = dirs[grid[r][c]]
        
        for ndr, ndc in adj:
            nr = r + ndr
            nc = c + ndc
            if 0 <= nr < height and 0 <= nc < width and (nr, nc) not in seen:
                cell = grid[nr][nc]
                if (cell not in '.#') or (nr, nc) == target:
                    if (cell == '^' and (ndr, ndc) != (1, 0)) or (cell == '>' and (ndr, ndc) != (0,- 1)) or \
                            (cell == 'v' and (ndr, ndc) != (-1, 0)) or (cell == '<' and (ndr, ndc) != (0, 1)) or (nr, nc) == target:
                        slopesFound.append((nr, nc, dist + 1))
                        seen.add((nr, nc))
                        if (nr, nc) not in seenSlopes and (nr, nc) != target:
                            seenSlopes.add((nr, nc))
                            qs.append((nr, nc))
                elif cell == '.':
                    seen.add((nr, nc))
                    q.append((nr, nc, dist + 1))
    
    slopeDist[s] = deepcopy(slopesFound)

pq = []
heappush(pq, (*source, 0))
seen = {}
seen[source] = 0

while pq:
    r, c, dist = heappop(pq)

    if (r, c) == target:
        result = -dist
        break

    key = (r, c)
    if dist > seen[key]:
        continue
    
    for nr, nc, d in slopeDist[key]:
        if (nr, nc) not in seen or dist - d < seen[(nr, nc)]:
            seen[(nr, nc)] = dist - d
            heappush(pq, (nr, nc, dist - d))

print(result)
