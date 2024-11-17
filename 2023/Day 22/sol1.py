with open('input.txt', 'r') as infile:
    lines = infile.readlines()

bricks = []
over = {}
under = {}
maxX = -1
maxY = -1

for line in lines:
    start, end = line.strip().split('~')
    start = list(map(int, start.split(',')))
    end = list(map(int, end.split(',')))
    maxX = max(maxX, end[0])
    maxY = max(maxY, end[1])
    bricks.append([start, end])

bricks.sort(key=lambda x: x[0][2])

width = maxX + 1
height = maxY + 1
heights = [[[0, -1] for _ in range(width)] for _ in range(height)]

for c, b in enumerate(bricks):
    start, end = b
    maxHeight = -1
    underList = []

    for i in range(start[1], end[1] + 1):
        for j in range(start[0], end[0] + 1):
            maxHeight = max(maxHeight, heights[i][j][0])
    
    for i in range(start[1], end[1] + 1):
        for j in range(start[0], end[0] + 1):
            brick = heights[i][j][1]
            if heights[i][j][0] == maxHeight and brick != -1 and brick not in underList:
                underList.append(brick)
    
    h = end[-1] - start[-1]
    newHeight = maxHeight + 1
    start[-1] = newHeight
    end[-1] = newHeight + h
    bricks[c] = (tuple(start), tuple(end))
    
    for i in range(start[1], end[1] + 1):
        for j in range(start[0], end[0] + 1):
            heights[i][j] = [end[-1], c]
    
    under[c] = underList

    for u in underList:
        overList = over.get(u, [])
        if c not in overList:
            overList.append(c)
        over[u] = overList
    

result = 0
for i, brick in enumerate(bricks):
    overList = over.get(i, [])
    isValid = True
    for o in overList:
        if len([u for u in under.get(o, []) if u != i]) == 0:
            isValid = False
            break
    
    if isValid:
        result += 1

print(result)
