with open('input.txt', 'r') as infile:
    lines = infile.readlines()

histories = [[int(num) for num in line.replace('\n', '').split()] for line in lines]
result = 0

for history in histories:
    oldDiff = [-num for num in history[::-1]]
    lastDiff = [oldDiff[-1]]
    while(any(d != 0 for d in oldDiff)):
        newDiff = [(oldDiff[i] - oldDiff[i - 1]) for i in range(1, len(oldDiff))]
        oldDiff = newDiff
        lastDiff.append(oldDiff[-1])
    
    lastDiff.pop()
    lastDiff.reverse()
    for i in range(0, len(lastDiff) - 1):
        lastDiff[i + 1] += lastDiff[i]
    result -= lastDiff[-1]

print(result)
