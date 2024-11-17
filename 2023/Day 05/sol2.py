with open('input.txt', 'r') as infile:
    lines = infile.readlines()

seeds = lines[0].split('seeds: ')[1].split()
seedPairs = []
i = 0
while i < len(seeds):
    start = int(seeds[i])
    end = start + int(seeds[i + 1]) - 1
    seedPairs.append([start, end])
    i += 2
seedPairs.sort(key=lambda seedPair: seedPair[0])

categories = [line.replace('\n', '') for line in lines[2:] if len(line) > 1]
catIndices = [(i + 1) for i, line in enumerate(categories) if not line[0].isdigit()]
catIndices.append(len(categories) + 1)
mapCount = [(catIndices[i] - catIndices[i - 1] - 1) for i in range(1, len(catIndices))]
catIndices = catIndices[0 : -1]

allMaps = []
for i, ind in enumerate(catIndices):
    m = []
    for j in range(ind, ind + mapCount[i]):
        s = categories[j].split()
        dest = int(s[0])
        source = int(s[1])
        r = int(s[2])
        m.append([source, source + r - 1, dest, dest + r - 1, r])
    
    m.sort(key=lambda m: m[0])
    allMaps.append(m)

for i in range(0, len(catIndices)):
    newSeedPairs = []
    procSeeds = seedPairs
    while len(procSeeds) > 0:
        seedStart, seedEnd = procSeeds[-1]
        filtered = False
        for mSourceStart, mSourceEnd, mDestStart, mDestEnd, mR in allMaps[i]:
            if seedStart >= mSourceStart and seedStart <= mSourceEnd and seedEnd >= mSourceEnd:
                length = mSourceEnd - seedStart + 1
                offset = seedStart - mSourceStart
                procSeeds.pop()
                if mSourceEnd != seedEnd:
                    procSeeds.append([mSourceEnd + 1, seedEnd])
                filtered = True
            elif mSourceStart >= seedStart and seedEnd >= mSourceEnd:
                length = mR
                offset = 0
                procSeeds.pop()
                if mSourceStart != seedStart:
                    procSeeds.append([seedStart, mSourceStart - 1])
                if mSourceEnd != seedEnd:
                    procSeeds.append([mSourceEnd + 1, seedEnd])
                filtered = True
            elif mSourceStart <= seedStart and seedEnd <= mSourceEnd:
                length = seedEnd - seedStart + 1
                offset = seedStart - mSourceStart
                procSeeds.pop()
                filtered = True
            elif mSourceStart >= seedStart and mSourceStart <= seedEnd and mSourceEnd >= seedEnd:
                length = seedEnd - mSourceStart + 1
                offset = 0
                procSeeds.pop()
                if mSourceStart != seedStart:
                    procSeeds.append([seedStart, mSourceStart - 1])
                filtered = True
            else:
                continue
            
            newSeedStart = mDestStart + offset
            newSeedPairs.append([newSeedStart, newSeedStart + length - 1])
            if filtered:
                break
        
        if not filtered:
            newSeedPairs.append(procSeeds[-1])
            procSeeds.pop()
    
    seedPairs = newSeedPairs

seedPairs.sort(key=lambda seedPair: seedPair[0])
print(seedPairs[0][0])
