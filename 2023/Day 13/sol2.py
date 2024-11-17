with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grids = ''.join(lines).split('\n\n')
grids = [grid.split('\n') for grid in grids]
grids[-1] = grids[-1][0 : -1]

result = 0
for grid in grids:
    width = len(grid[0])
    height = len(grid)
    rows = [row for row in grid]
    columns = [''.join([grid[j][i] for j in range(height)]) for i in range(width)]
    
    for i in range(0, width - 1):
        l = i
        r = i + 1
        diff = 0
        while l > -1 and r < width:
            diff += sum([1 for j in range(height) if columns[l][j] != columns[r][j]])
            l -= 1
            r += 1
        if diff == 1:
            result += i + 1
    
    for i in range(0, height - 1):
        l = i
        r = i + 1
        diff = 0
        while l > -1 and r < height:
            diff += sum([1 for j in range(width) if rows[l][j] != rows[r][j]])
            l -= 1
            r += 1
        if diff == 1:
            result += 100 * (i + 1)

print(result)
