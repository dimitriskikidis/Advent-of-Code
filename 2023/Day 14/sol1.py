with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [line.replace('\n', '') for line in lines]
width = len(grid[0])
height = len(grid)
columns = [''.join([grid[j][i] for j in range(height)]) for i in range(width)]

result = 0
for i in range(width):
    s = 0
    j = 0
    column = columns[i]
    lastInd = -1
    while j < height:
        if column[j] == 'O':
            s += 1
        elif column[j] == '#':
            result += sum([(height - ind) for ind in range(lastInd + 1, lastInd + 1 + s)])
            lastInd = j
            s = 0
        j += 1
    
    if s != 0:
        result += sum([(height - ind) for ind in range(lastInd + 1, lastInd + 1 + s)])

print(result)
        