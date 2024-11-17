with open('input.txt', 'r') as infile:
    lines = infile.readlines()

steps = [step for step in lines[0].replace('\n', '').split(',')]
boxes = [[] for i in range(256)]

for step in steps:
    if step[-1] == '-':
        label = step[0 : -1]
        boxInd = 0
        for c in label:
            boxInd = ((boxInd + ord(c)) * 17) % 256
        idx = -1
        for i, pair in enumerate(boxes[boxInd]):
            currLabel, currFocalLength = pair
            if label == currLabel:
                idx = i
                break
        if idx != -1:
            boxes[boxInd].pop(idx)
    else:
        label, focalLength = step.split('=')
        boxInd = 0
        for c in label:
            boxInd = ((boxInd + ord(c)) * 17) % 256
        found = False
        for i, pair in enumerate(boxes[boxInd]):
            currLabel, currFocalLength = pair
            if label == currLabel:
                boxes[boxInd][i][1] = focalLength
                found = True
                break
        
        if not found:
            boxes[boxInd].append([label, focalLength])

result = 0
for i, box in enumerate(boxes):
    for j, pair in enumerate(box):
        result += (i + 1) * (j + 1) * int(pair[1])

print(result)
