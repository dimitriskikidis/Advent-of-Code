from collections import deque

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [line.replace('\n', '') for line in lines]
width = len(grid[0])
height = len(grid)

S = 0
for i in range(0, height):
    for j in range(0, width):
        if grid[i][j] == 'S':
            S = [i, j]
            break

visited = [[False for i in range(0, width)] for j in range(0, height)]
distances = [[0 for i in range(0, width)] for j in range(0, height)]
visited[S[0]][S[1]] = True
q = deque()
q.append(S)

while len(q) > 0:
    u = q.popleft()
    i, j = u
    furthest = distances[i][j]

    neighbors = []
    northInd = i - 1
    southInd = i + 1
    westInd = j - 1
    eastInd = j + 1

    if northInd >= 0 and grid[i][j] in ['|', 'L', 'J', 'S'] and grid[northInd][j] in ['|', '7', 'F']:
        neighbors.append([northInd, j])
    
    if southInd < height and grid[i][j] in ['|', '7', 'F', 'S'] and grid[southInd][j] in ['|', 'L', 'J']:
        neighbors.append([southInd, j])
    
    if westInd >= 0 and grid[i][j] in ['-', 'J', '7', 'S'] and grid[i][westInd] in ['-', 'L', 'F']:
        neighbors.append([i, westInd])
    
    if eastInd < width and grid[i][j] in ['-', 'L', 'F', 'S'] and grid[i][eastInd] in ['-', 'J', '7']:
        neighbors.append([i, eastInd])
    
    for row, col in neighbors:
        if visited[row][col]:
            continue
        visited[row][col] = True
        distances[row][col] = distances[i][j] + 1
        q.append([row, col])

print(furthest)
