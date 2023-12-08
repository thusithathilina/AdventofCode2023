import re

with open("/Users/tday0004/Downloads/adavent2023/8.txt") as file:
    routeMap = {}
    inst = file.readline().strip()
    file.readline()

    for line in file:
        parts = re.split(r'=', line)
        routeMap[parts[0].strip()] = parts[1].strip()[1:-1]

    count = 0
    index = 0
    key = 'AAA'
    while key != 'ZZZ':
        possibilities = routeMap[key].split(",")
        if inst[index] == 'L':
            key = possibilities[0].strip()
        else:
            key = possibilities[1].strip()
        count += 1
        index = (index + 1) % len(inst)
    print(count)
