from math import ceil, floor, sqrt

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

Time = int(''.join(lines[0][0 : -1].split(':')[1].split()))
Distance = int(''.join(lines[1].split(':')[1].split()))

D = Time ** 2 - 4 * Distance

t1 = ceil((Time - sqrt(D)) / 2)
t2 = floor((Time + sqrt(D)) / 2)
numWays = t2 - t1 + 1

print(numWays)
