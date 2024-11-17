def getCalValue(line):
    nums = [n for n in line if n.isdigit()]
    return int(nums[0] + nums[len(nums) - 1])

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

result = sum([getCalValue(line) for line in lines])
print(result)
