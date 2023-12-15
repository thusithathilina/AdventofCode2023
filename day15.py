import re


def day15part1():
    with open("15.txt") as file:
        value = 0
        terms = re.split(r',', file.readline().strip())
        for term in terms:
            hashVal = 0
            for c in term:
                ascii = ord(c)
                hashVal += ascii
                hashVal *= 17
                hashVal %= 256
            value += hashVal
        print(value)


def day15part2():
    with open("15.txt") as file:
        terms = re.split(r',', file.readline().strip())
        hashmap = {}
        for term in terms:
            hashVal = 0
            parts = re.split(r'[=-]', term)
            for c in parts[0]:
                ascii = ord(c)
                hashVal += ascii
                hashVal *= 17
                hashVal %= 256
            if '=' in term:
                if hashVal in hashmap.keys():
                    values = hashmap[hashVal]
                    updated = False
                    i = 0
                    while i < len(values):
                        if values[i][0:len(parts[0])] == parts[0]:
                            values[i] = f"{parts[0]} {parts[1]}"
                            updated = True
                        i += 1
                    if not updated:
                        values.append(f"{parts[0]} {parts[1]}")
                else:
                    hashmap[hashVal] = [f"{parts[0]} {parts[1]}"]
            else:
                if hashVal in hashmap.keys():
                    values = hashmap[hashVal]
                    i = 0
                    while i < len(values):
                        if values[i][0:len(parts[0])] == parts[0]:
                            values.remove(values[i])
                        i += 1
    
        power = 0
        for key in hashmap.keys():
            values = hashmap[key]
            i = 0
            while i < len(values):
                power += (key + 1) * (i + 1) * int(values[i][-1])
                i += 1
        print(power)
