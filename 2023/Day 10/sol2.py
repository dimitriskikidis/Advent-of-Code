from collections import deque

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [line.replace('\n', '') for line in lines]
width = len(grid[0])
height = len(grid)

S = 0
for i in range(0, height):
    j = grid[i].find('S')
    if j != -1:
        S = [i, j]
        break

visited = [[False for i in range(0, width)] for j in range(0, height)]
neighbors = {}

visited[S[0]][S[1]] = True
q = deque()
q.append(S)

while len(q) > 0:
    u = q.popleft()
    i, j = u

    currNeighbors = []
    northInd = i - 1
    southInd = i + 1
    westInd = j - 1
    eastInd = j + 1

    if northInd >= 0 and grid[i][j] in ['|', 'L', 'J', 'S'] and grid[northInd][j] in ['|', '7', 'F', 'S']:
        currNeighbors.append([northInd, j])
    
    if southInd < height and grid[i][j] in ['|', '7', 'F', 'S'] and grid[southInd][j] in ['|', 'L', 'J', 'S']:
        currNeighbors.append([southInd, j])
    
    if westInd >= 0 and grid[i][j] in ['-', 'J', '7', 'S'] and grid[i][westInd] in ['-', 'L', 'F', 'S']:
        currNeighbors.append([i, westInd])
    
    if eastInd < width and grid[i][j] in ['-', 'L', 'F', 'S'] and grid[i][eastInd] in ['-', 'J', '7', 'S']:
        currNeighbors.append([i, eastInd])
    
    ind = i * width + j
    neighbors[ind] = currNeighbors
    
    for row, col in currNeighbors:
        if visited[row][col]:
            continue
        visited[row][col] = True
        q.append([row, col])

result = 0
for i in range(0, height):
    for j in range(0, width):
        if visited[i][j]:
            continue

        isOutside = True
        
        for k in range(j + 1, width):
            curr = i * width + k

            n = neighbors.get(curr, [])
            if [i + 1, k] in n:
                isOutside = not isOutside

        if not isOutside:
            result += 1

print(result)
