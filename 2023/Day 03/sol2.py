import re

gears = {}

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

result = 0

width = len(lines[0]) - 1
height = len(lines)

for i, line in enumerate(lines):
    for j, number in enumerate(re.finditer('[0-9]+', line)):
        startVertical = max(0, i - 1)
        endVertical = min(height - 1, i + 1)
        startHorizontal = max(0, number.start() - 1)
        endHorizontal = min(width - 1, number.end())

        for h in range(startVertical, endVertical + 1):
            for w in range(startHorizontal, endHorizontal + 1):
                char = lines[h][w]
                if char == '*':
                    idx = h * width + w
                    gearList = gears.get(idx, [])
                    gearList.append(int(number.group()))
                    gears[idx] = gearList

for gear, numbers in gears.items():
    if len(numbers) == 2:
        result += numbers[0] * numbers[1]

print(result)
