from math import lcm

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

instructions = lines[0].replace('\n', '')
rows = [line.replace('\n', '') for line in lines[2:]]
nodes = []
dirs = {}
for row in rows:
    node, dirPair = row.split(' = ')
    left, right = dirPair[1 : -1].split(', ')
    nodes.append(node)
    dirs[node] = { 'L': left, 'R': right }

startingNodes = [node for node in nodes if node[2] == 'A']
steps = [0] * len(startingNodes)

for i, startingNode in enumerate(startingNodes):
    count = 0
    j = 0
    currNode = startingNode
    while True:
        count += 1
        turn = instructions[j]
        nextNode = dirs.get(currNode, '').get(turn, '')
        if nextNode[2] == 'Z':
            break
        currNode = nextNode
        j += 1
        if j == len(instructions):
            j = 0
    steps[i] = count

print(lcm(*steps))
