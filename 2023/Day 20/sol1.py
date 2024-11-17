from collections import deque

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

pulses = [0, 0]

for _ in range(1000):
    pulses[0] += 1
    queue = deque()
    for target in modules['broadcaster'][1]:
        queue.append(('broadcaster', target, False))

    while len(queue) > 0:
        sender, receiver, pulse = queue.popleft()
        key = 1 if pulse else 0
        pulses[key] += 1
        if receiver not in modules:
            continue
        
        moduleType, targets = modules[receiver]

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

result = pulses[0] * pulses[1]
print(result)
