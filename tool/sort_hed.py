path = input('path: ').strip('"')
with open(path, 'r') as f:
    lines = f.readlines()
lines.sort()
with open(path + '_sorted', 'w') as f:
    f.writelines(lines)
