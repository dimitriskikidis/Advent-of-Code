def isPossible(line):
    line = line.split('\n')[0]
    splitLine = line.split(': ', 1)
    games = splitLine[1].split('; ')
    maxR = 0
    maxG = 0
    maxB = 0

    for game in games:
        stats = game.split(', ')
        for s in stats:
            count, color = s.split(' ')
            count = int(count)
            if (color == 'red' and count > maxR):
                maxR = count
            if (color == 'green' and count > maxG):
                maxG = count
            if (color == 'blue' and count > maxB):
                maxB = count

    return maxR * maxG * maxB

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

result = sum([isPossible(line) for line in lines])
print(result)
