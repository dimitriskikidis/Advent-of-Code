with open('input.txt', 'r') as infile:
    lines = infile.readlines()

seeds = lines[0].split('seeds: ')[1].split()
categories = [line.replace('\n', '') for line in lines[2:] if len(line) > 1]
catIndices = [i for i, line in enumerate(categories) if not line[0].isdigit()]
catIndices.append(len(categories))
mapCount = [(catIndices[i] - catIndices[i - 1] - 1) for i in range(1, len(catIndices))]
catIndices = catIndices[0 : -1]
finalMapping = [int(seed) for seed in seeds]

for i, ind in enumerate(catIndices):
    m = []
    for j in range(ind + 1, ind + 1 + mapCount[i]):
        s = categories[j].split()
        dest = int(s[0])
        source = int(s[1])
        r = int(s[2])
        m.append([source, dest, r])
    
    for j, mapping in enumerate(finalMapping):
        for source, dest, r in m:
            if mapping >= source and mapping <= source + r - 1:
                finalMapping[j] = dest + (mapping - source)
                break

print(min(finalMapping))
