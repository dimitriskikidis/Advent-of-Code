from functools import cache

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

result = 0

@cache
def count(row, nums):
    if row == '':
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if '#' in row else 1
    
    result = 0
    if row[0] in '.?':
        result += count(row[1:], nums)
    
    if row[0] in '#?':
        if nums[0] <= len(row) and '.' not in row[:nums[0]] and (nums[0] == len(row) or row[nums[0]] != '#'):
            result += count(row[nums[0] + 1:], nums[1:])
    
    return result
    

for line in lines:
    row, nums = line.split()
    row = '?'.join([row] * 5)
    nums = tuple(map(int, nums.split(',')))
    nums = nums * 5
    result += count(row, nums)

print(result)
