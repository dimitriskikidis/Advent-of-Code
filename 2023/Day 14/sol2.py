with open('input.txt', 'r') as infile:
    lines = infile.readlines()

grid = [list(line.replace('\n', '')) for line in lines]
width = len(grid[0])
height = len(grid)
count = 0
loads = []
entries = {}

while True:
    columns = [[grid[j][i] for j in range(height)] for i in range(width)]
    for i in range(width):
        s = 0
        j = 0
        column = columns[i]
        lastInd = -1
        while j < height:
            if column[j] == 'O':
                s += 1
            elif column[j] == '#':
                for k in range(lastInd + 1, lastInd + 1 + s):
                    grid[k][i] = 'O'
                for k in range(lastInd + 1 + s, j):
                    grid[k][i] = '.'
                lastInd = j
                s = 0
            j += 1
        
        if s != 0:
            for k in range(lastInd + 1, lastInd + 1 + s):
                grid[k][i] = 'O'
            for k in range(lastInd + 1 + s, j):
                grid[k][i] = '.'
    
    rows = [grid[i] for i in range(height)]
    for i in range(height):
        s = 0
        j = 0
        row = rows[i]
        lastInd = -1
        while j < width:
            if row[j] == 'O':
                s += 1
            elif row[j] == '#':
                for k in range(lastInd + 1, lastInd + 1 + s):
                    grid[i][k] = 'O'
                for k in range(lastInd + 1 + s, j):
                    grid[i][k] = '.'
                lastInd = j
                s = 0
            j += 1
        
        if s != 0:
            for k in range(lastInd + 1, lastInd + 1 + s):
                grid[i][k] = 'O'
            for k in range(lastInd + 1 + s, j):
                grid[i][k] = '.'
    
    columns = [[grid[j][i] for j in range(height)] for i in range(width)]
    for i in range(width):
        s = 0
        j = height - 1
        column = columns[i]
        lastInd = height
        while j > -1:
            if column[j] == 'O':
                s += 1
            elif column[j] == '#':
                for k in range(lastInd - s, lastInd):
                    grid[k][i] = 'O'
                for k in range(j + 1, lastInd - s):
                    grid[k][i] = '.'
                lastInd = j
                s = 0
            j -= 1
        
        if s != 0:
            for k in range(lastInd - s, lastInd):
                grid[k][i] = 'O'
            for k in range(j + 1, lastInd - s):
                grid[k][i] = '.'
    
    rows = [grid[i] for i in range(height)]
    for i in range(height):
        s = 0
        j = width - 1
        row = rows[i]
        lastInd = width
        while j > -1:
            if row[j] == 'O':
                s += 1
            elif row[j] == '#':
                for k in range(lastInd - s, lastInd):
                    grid[i][k] = 'O'
                for k in range(j + 1, lastInd - s):
                    grid[i][k] = '.'
                lastInd = j
                s = 0
            j -= 1
        
        if s != 0:
            for k in range(lastInd - s, lastInd):
                grid[i][k] = 'O'
            for k in range(j + 1, lastInd - s):
                grid[i][k] = '.'

    load = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'O':
                load += height - i
    
    loads.append(load)
    count += 1
    ind = entries.get(str(grid), 0)
    if ind != 0:
        diff = count - ind
        result = loads[ind - 1 + (1000000000 - ind) % diff]
        break
    entries[str(grid)] = count

print(result)
