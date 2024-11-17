from copy import deepcopy
from collections import deque

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [line.strip() for line in lines]
width, height = len(grid[0]), len(grid)
source = (0, grid[0].find('.'))
target = (height - 1, grid[-1].find('.'))

def dfs(r, c, t, currDist):
    if (r, c) == t:
        return currDist

    maxDist = -float('inf')
    seen.add((r, c))
    for nr, nc, dist in slopeDist[(r, c)]:
        if (nr, nc) not in seen:
            maxDist = max(maxDist, dfs(nr, nc, t, currDist + dist))
    seen.remove((r, c))
    
    return maxDist

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

        adj = []
        for ndr, ndc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            adj.append((ndr, ndc))

        for ndr, ndc in adj:
            nr = r + ndr
            nc = c + ndc
            if 0 <= nr < height and 0 <= nc < width and (nr, nc) not in seen:
                cell = grid[nr][nc]
                if cell != '#':
                    count = 0
                    for ndr2, ndc2 in adj:
                        nr2 = nr + ndr2
                        nc2 = nc + ndc2
                        if 0 <= nr2 < height and 0 <= nc2 < width and grid[nr2][nc2] != '#':
                            count += 1
                    
                    if count > 2 or (nr, nc) == target:
                        slopesFound.append((nr, nc, dist + 1))
                        seen.add((nr, nc))
                        if (nr, nc) not in seenSlopes and (nr, nc) != target:
                            seenSlopes.add((nr, nc))
                            qs.append((nr, nc))
                    else:
                        seen.add((nr, nc))
                        q.append((nr, nc, dist + 1))
    
    slopeDist[s] = deepcopy(slopesFound)

seen = set()
result = dfs(*source, target, 0)
print(result)
