import math

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

plan = [line.replace('\n', '').split(' ') for line in lines]
plan = [(d, int(steps), color[1 : -1]) for d, steps, color in plan]

i, j = 0, 0
maxI, maxJ, minI, minJ = -math.inf, -math.inf, math.inf, math.inf
result = 0
for d, steps, _ in plan:
    result += steps

    if d == 'U':
        i -= steps
        maxI = max(maxI, i)
        minI = min(minI, i)
    elif d == 'R':
        j += steps
        maxJ = max(maxJ, j)
        minJ = min(minJ, j)
    elif d == 'D':
        i += steps
        maxI = max(maxI, i)
        minI = min(minI, i)
    else:
        j -= steps
        maxJ = max(maxJ, j)
        minJ = min(minJ, j)

height, width = (maxI - minI + 1), (maxJ - minJ + 1)
grid = [[0 for _ in range(width)] for _ in range(height)]

i, j = -minI, -minJ
for d, steps, _ in plan:
    if d == 'U':
        for k in range(i, i - steps, - 1):
            grid[k][j] = 1
        i -= steps
    elif d == 'R':
        for k in range(j, j + steps):
            grid[i][k] = 1
        j += steps
    elif d == 'D':
        for k in range(i, i + steps):
            grid[k][j] = 1
        i += steps
    else:
        for k in range(j, j - steps, -1):
            grid[i][k] = 1
        j -= steps

for i in range(height):
    for j in range(width):
        if grid[i][j] == 1:
            continue
        
        isOutside = True

        for k in range(j + 1, width):
            if grid[i][k] == 1 and (i + 1 < height) and grid[i + 1][k] == 1:
                isOutside = not isOutside

        if not isOutside:
            result += 1

print(result)
