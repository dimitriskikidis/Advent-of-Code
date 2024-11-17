import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

result = 0

for line in lines:
    line = re.sub(r'\s+', ' ', line)
    winningNums, nums = line[0 : -1].split(': ')[1].split(' | ')
    winningNums = winningNums.split()
    nums = nums.split()
    
    count = 0
    for num in nums:
        if num in winningNums:
            count += 1
    if count > 0:
        result += 2 ** (count - 1)

print(result)
