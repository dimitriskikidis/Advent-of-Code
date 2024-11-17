from collections import deque

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [line.replace('\n', '') for line in lines]
width = len(grid[0])
height = len(grid)
initTiles = [[0, i, 'down'] for i in range(width)] + [[height - 1, i, 'up'] for i in range(width)] + [[i, 0, 'right'] for i in range(height)] + [[i, width - 1, 'left'] for i in range(height)]
result = 0

for initTile in initTiles:
    energized = [[False for _ in range(width)] for _ in range(height)]
    moves = {}
    q = deque()
    q.append(initTile)

    while len(q) > 0:
        u = q.popleft()
        row, col, dir = u
        if not (-1 < row < height) or not (-1 < col < width):
            continue
        energized[row][col] = True

        if dir == 'right':
            for i in range(col, width):
                energized[row][i] = True
                key = (row, col, row, i)
                if grid[row][i] == '\\':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([row + 1, i, 'down'])
                    break
                elif grid[row][i] == '/':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([row - 1, i, 'up'])
                    break
                elif grid[row][i] == '|':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([row + 1, i, 'down'])
                        q.append([row - 1, i, 'up'])
                    break
        elif dir == 'down':
            for i in range(row, height):
                energized[i][col] = True
                key = (row, col, i, col)
                if grid[i][col] == '\\':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([i, col + 1, 'right'])
                    break
                elif grid[i][col] == '/':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([i, col - 1, 'left'])
                    break
                elif grid[i][col] == '-':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([i, col + 1, 'right'])
                        q.append([i, col - 1, 'left'])
                    break
        elif dir == 'left':
            for i in range(col, -1, -1):
                energized[row][i] = True
                key = (row, col, row, i)
                if grid[row][i] == '\\':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([row - 1, i, 'up'])
                    break
                elif grid[row][i] == '/':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([row + 1, i, 'down'])
                    break
                elif grid[row][i] == '|':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([row + 1, i, 'down'])
                        q.append([row - 1, i, 'up'])
                    break
        elif dir == 'up':
            for i in range(row, -1, -1):
                energized[i][col] = True
                key = (row, col, i, col)
                if grid[i][col] == '\\':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([i, col - 1, 'left'])
                    break
                elif grid[i][col] == '/':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([i, col + 1, 'right'])
                    break
                elif grid[i][col] == '-':
                    if not moves.get(key, False):
                        moves[key] = True
                        q.append([i, col + 1, 'right'])
                        q.append([i, col - 1, 'left'])
                    break

    count = 0
    for i in range(height):
        for j in range(width):
            if energized[i][j]:
                count += 1
    
    result = max(result, count)

print(result)
