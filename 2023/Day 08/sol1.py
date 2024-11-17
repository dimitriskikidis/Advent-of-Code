with open('input.txt', 'r') as infile:
    lines = infile.readlines()

instructions = lines[0][0 : -1]
rows = [line[0 : -1] for line in lines[2:]]
dirs = {}
for row in rows:
    node, dirPair = row.split(' = ')
    left, right = dirPair[1 : -1].split(', ')
    dirs[node] = { 'L': left, 'R': right }

steps = 0
i = 0
currNode = 'AAA'
while True:
    steps += 1
    turn = instructions[i]
    nextNode = dirs.get(currNode, '').get(turn, '')
    if nextNode == 'ZZZ':
        break
    currNode = nextNode
    i += 1
    if i == len(instructions):
        i = 0

print(steps)
