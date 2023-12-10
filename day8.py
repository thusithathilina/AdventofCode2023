import re
import math


def day8part1():
    with open("8.txt") as file:
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


def day8part2():
    with open("8.txt") as file:
        routeMap = {}
        inst = file.readline().strip()
        file.readline()
    
        startKeys = []
        for line in file:
            parts = re.split(r'=', line)
            key = parts[0].strip()
            routeMap[key] = parts[1].strip()[1:-1]
            if key.endswith('A'):
                startKeys.append(key)
    
        lcm = 1
        for key in startKeys:
            index = 0
            count = 0
            while not key.endswith('Z'):
                possibilities = routeMap[key].split(",")
                if inst[index] == 'L':
                    key = possibilities[0].strip()
                else:
                    key = possibilities[1].strip()
                count += 1
                index = (index + 1) % len(inst)
            lcm = math.lcm(lcm, count)
        print(lcm)
