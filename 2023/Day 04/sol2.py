import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

cards = [1 for i in range(0, len(lines))]

for cardNum, line in enumerate(lines):
    line = re.sub(r'\s+', ' ', line)
    winningNums, nums = line[0 : -1].split(': ')[1].split(' | ')
    winningNums = winningNums.split()
    nums = nums.split()
    
    count = sum([1 for num in nums if num in winningNums])
    cardCount = cards[cardNum]
    for i in range(cardNum + 1, cardNum + count + 1):
        cards[i] += cardCount

result = sum(cards)
print(result)
