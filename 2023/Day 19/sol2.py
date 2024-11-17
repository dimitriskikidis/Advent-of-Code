with open('input.txt', 'r') as infile:
    lines = infile.readlines()

lines = ''.join(lines)
workflowws = lines.split('\n\n')[0]
workflowws = [w for w in workflowws.split('\n')]
counts = {}

workflowwMap = {}
for w in workflowws:
    name, rules = w[:-1].split('{')
    rules = rules.split(',')
    workflowwMap[name] = ([], rules.pop())
    workflowwList = []
    for rule in rules:
        comparison, target = rule.split(':')
        key = comparison[0]
        op = comparison[1]
        num = int(comparison[2:])
        workflowwMap[name][0].append((key, op, num, target))

def count(ranges, name = 'in'):
    if name == 'R':
        return 0
    if name == 'A':
        product = 1
        for low, hi in ranges.values():
            product *= hi - low + 1
        return product
    
    rules, fallback = workflowwMap[name]
    total = 0

    for key, op, n, target in rules:
        low, hi = ranges[key]
        if op == '<':
            T = (low, min(n - 1, hi))
            F = (max(n, low), hi)
        else:
            T = (max(n + 1, low), hi)
            F = (low, min(n, hi))
        
        rangeT = dict(ranges)
        rangeT[key] = T
        total += count(rangeT, target)
        ranges[key] = F
    
    total += count(ranges, fallback)
            
    return total

result = count({key: (1, 4000) for key in 'xmas'})

print(result)
