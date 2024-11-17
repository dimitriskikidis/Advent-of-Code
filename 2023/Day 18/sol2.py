from collections import deque
import math

def isInside(i, j, c):
    _cols = [col for col in c if j < col[0][1] and (col[0][0] <= i < col[1][0])]
    return len(_cols) % 2 == 1

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

plan = [line.replace('\n', '').split(' ')[-1][2 : -1] for line in lines]
plan = [(int(color[0 : -1], 16), int(color[-1])) for color in plan]

i, j = 0, 0
maxI, maxJ, minI, minJ = -math.inf, -math.inf, math.inf, math.inf
rows = []
cols = []
result = 0

for steps, d in plan:
    result += steps

    if d == 0:
        rows.append(((i, j), (i, j + steps)))
        j += steps
        maxJ = max(maxJ, j)
        minJ = min(minJ, j)
    elif d == 1:
        cols.append(((i, j), (i + steps, j)))
        i += steps
        maxI = max(maxI, i)
        minI = min(minI, i)
    elif d == 2:
        rows.append(((i, j - steps), (i, j)))
        j -= steps
        maxJ = max(maxJ, j)
        minJ = min(minJ, j)
    else:
        cols.append(((i - steps, j), (i, j)))
        i -= steps
        maxI = max(maxI, i)
        minI = min(minI, i)

rows = [((row - minI, col - minJ), (row2 - minI, col2 - minJ)) for ((row, col), (row2, col2)) in rows]
rows = sorted(rows, key=lambda row: row[0])

cols = [((row - minI, col - minJ), (row2 - minI, col2 - minJ)) for ((row, col), (row2, col2)) in cols]
cols = sorted(cols, key=lambda col: col[0])

for leftCol in cols:
    i, j = leftCol[0][0], leftCol[0][1]

    if not isInside(i + 1, j + 1, cols):
        continue
    
    hasTopRightRow = len([1 for row in rows if row[0] == leftCol[0]]) != 0
    hasBottomRightRow = len([1 for row in rows if row[0] == leftCol[1]]) != 0

    if hasTopRightRow:
        p1 = i + 1
    else:
        p1 = i
    if hasBottomRightRow:
        p2 = leftCol[1][0] - 1
    else:
        p2 = leftCol[1][0]
    intervals = deque([(p1, p2)])
    
    while len(intervals) != 0:
        currInterval = intervals.popleft()
        start, end = currInterval
        rightCols = [col for col in cols if (col[0][1] > j) and
            ((start <= col[0][0] <= end) or (start <= col[1][0] <= end) or (col[0][0] < start < end < col[1][0]))]
        rightCol = sorted(rightCols, key=lambda col: col[0][1])[0]

        if start <= rightCol[0][0] <= rightCol[1][0] <= end:
            finalStart = rightCol[0][0]
            finalEnd = rightCol[1][0]
        elif rightCol[0][0] < start < end < rightCol[1][0]:
            finalStart = start
            finalEnd = end
        elif start <= rightCol[0][0] <= end < rightCol[1][0]:
            finalStart = rightCol[0][0]
            finalEnd = end
        elif rightCol[0][0] < start <= rightCol[1][0] <= end:
            finalStart = start
            finalEnd = rightCol[1][0]
        height = (finalEnd - finalStart) + 1
        width = rightCol[0][1] - j - 1
        result += width * height

        if finalStart != start and finalEnd != end:
            intervals.append((start, finalStart - 1))
            intervals.append((finalEnd + 1, end))
        elif finalStart != start:
            intervals.append((start, finalStart - 1))
        elif finalEnd != end:
            intervals.append((finalEnd + 1, end))

print(result)
