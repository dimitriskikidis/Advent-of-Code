with open('input.txt', 'r') as infile:
    lines = infile.readlines()

times = [int(num) for num in lines[0][0 : -1].split(':')[1].split()]
distances = [int(num) for num in lines[1].split(':')[1].split()]
prod = 1

for time, distance in zip(times, distances):
    prod *= sum([1 for i in range(1, time) if i * (time - i) > distance])
    
print(prod)
