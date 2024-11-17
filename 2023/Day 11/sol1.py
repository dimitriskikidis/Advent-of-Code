with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [line.replace('\n', '') for line in lines]
width = len(grid[0])
height = len(grid)

gRows = []
gCols = []
galaxies = []

for i in range(0, height):
    hasGalaxy = False

    for j in range(0, width):
        if grid[i][j] == '#':
            galaxies.append([i, j])
            hasGalaxy = True
    
    if not hasGalaxy:
        gRows.append(i)

for i in range(0, width):
    hasGalaxy = False

    for j in range(0, height):
        if grid[j][i] == '#':
            hasGalaxy = True
            break
    
    if not hasGalaxy:
        gCols.append(i)

result = 0

for i in range(0, len(galaxies)):
    g1 = galaxies[i]
    for j in range(i + 1, len(galaxies)):
        g2 = galaxies[j]
        
        minRow = min(g1[0], g2[0])
        maxRow = max(g1[0], g2[0])
        minCol = min(g1[1], g2[1])
        maxCol = max(g1[1], g2[1])

        result += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        result += sum([1 for row in gRows if minRow < row < maxRow])
        result += sum([1 for col in gCols if minCol < col < maxCol])

print(result)
