from collections import deque
from math import lcm

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

modules = {}
state = {}

for line in lines:
    module, targets = line.replace('\n', '').split(' -> ')
    targets = targets.split(', ')
    if module != 'broadcaster':
        moduleType, name = module[0], module[1:]
        if moduleType == '%':
            state[name] = False
    else:
        moduleType, name = '', module
        state['broadcaster'] = False
    modules[name] = (moduleType, targets)

for module in modules.keys():
    if module == 'broadcaster':
        continue
    inputs = [k for k, v in modules.items() if module in v[1]]
    if modules[module][0] == '&':
        m = {}
        for input in inputs:
            m[input] = False
        state[module] = [m, True]

count = 0
finalFeed = [module for module, targets in modules.items() if 'rx' in targets[1]][0]
magic4 = [module for module, targets in modules.items() if finalFeed in targets[1]]
cycles = {}

while True:
    count += 1
    queue = deque()

    for target in modules['broadcaster'][1]:
        queue.append(('broadcaster', target, False))

    while len(queue) > 0:
        sender, receiver, pulse = queue.popleft()
        if receiver not in modules:
            continue
        
        moduleType, targets = modules[receiver]

        if pulse and sender in magic4:
            cycles[sender] = count

        if moduleType == '%' and not pulse:
            state[receiver] = not state.get(receiver)
            for target in targets:
                queue.append((receiver, target, state[receiver]))
        elif moduleType == '&':
            inputs, output = state[receiver]
            inputs[sender] = pulse
            output = not all([inp for inp in inputs.values()])
            state[receiver] = [inputs, output]
            for target in targets:
                queue.append((receiver, target, output))
    
    if len(cycles) == len(magic4):
        print(count)
        break

result = lcm(*cycles.values())
print(result)
