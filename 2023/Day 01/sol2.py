def getCalValue(line):
    newLine = ""
    i = 0
    while i < len(line):
        char = line[i]
        if char.isdigit():
            newLine += char
        else:
            for j, word in enumerate(words):
                if (i + len(word) - 1 < len(line)) and (line[i : i + len(word)] == word):
                    newLine += str(j + 1)
                    break
        i += 1

    line = newLine
    return int(line[0] + line[len(line) - 1])


words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

result = sum([getCalValue(line) for line in lines])
print(result)
