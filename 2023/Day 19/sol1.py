with open('input.txt', 'r') as infile:
    lines = infile.readlines()

lines = ''.join(lines)
workflows, ratings = lines.split('\n\n')
workflows = [w for w in workflows.split('\n')]
ratings = [r for r in ratings.split('\n') if r != '']

workflowMap = {}
for w in workflows:
    name, rules = w[:-1].split('{')
    rules = rules.split(',')
    workflowMap[name] = rules

result = 0
for rating in ratings:
    xmas = rating[1 : -1].split(',')
    ratingMap = {}
    for r in xmas:
        name, value = r[0], int(r[2:])
        ratingMap[name] = value
    
    rules = workflowMap['in']
    isDone = False
    while not isDone:
        for i, rule in enumerate(rules):
            if i == len(rules) - 1:
                if rule == 'A':
                    result += sum([v for v in ratingMap.values()])
                    isDone = True
                elif rule == 'R':
                    isDone = True
                else:
                    rules = workflowMap[rule]
                break
            
            varName = rule[0]
            op = rule[1]
            lim, dest = rule[2:].split(':')
            lim = int(lim)
            
            if (op == '<' and ratingMap[varName] < lim) or (op == '>' and ratingMap[varName] > lim):
                if dest == 'A':
                    result += sum([v for v in ratingMap.values()])
                    isDone = True
                elif dest == 'R':
                    isDone = True
                else:
                    rules = workflowMap[dest]
                break
print(result)
