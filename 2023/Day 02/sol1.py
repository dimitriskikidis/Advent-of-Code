maxR = 12
maxG = 13
maxB = 14

def isPossible(line):
    line = line.split('\n')[0]
    splitLine = line.split(': ', 1)
    gameId = int(splitLine[0].split(' ')[1])
    games = splitLine[1].split('; ')
    for game in games:
        stats = game.split(', ')
        for s in stats:
            count, color = s.split(' ')
            count = int(count)
            if (color == 'red' and count > maxR) or (color == 'green' and count > maxG) or (color == 'blue' and count > maxB):
                return 0
    return gameId

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

result = sum([isPossible(line) for line in lines])
print(result)
