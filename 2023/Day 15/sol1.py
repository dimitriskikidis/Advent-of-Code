with open('input.txt', 'r') as infile:
    lines = infile.readlines()

steps = [step for step in lines[0].replace('\n', '').split(',')]

result = 0
for step in steps:
    value = 0
    for c in step:
        value = ((value + ord(c)) * 17) % 256
    result += value

print(result)
