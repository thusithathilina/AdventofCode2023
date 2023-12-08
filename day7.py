import re


def handValue(hand, part1=True):
    val = []
    for c in hand:
        if c == 'A':
            val.append(14)
        elif c == 'K':
            val.append(13)
        elif c == 'Q':
            val.append(12)
        elif c == 'J':
            if part1:
                val.append(11)
            else:
                val.append(1)
        elif c == 'T':
            val.append(10)
        else:
            val.append(int(c))
    return val


def findHandType(hand):
    charMap = {}
    jCount = 0
    for c in hand:
        if c == 'J':
            jCount += 1
        elif c in charMap:
            charMap[c] += 1
        else:
            charMap[c] = 1
    val = list(charMap.values())
    val.sort(reverse=True)

    if jCount == 1:
        if val[0] == 4:
            return 7
        elif val[0] == 3:
            return 6
        elif val[0] == 2 and val[1] == 2:
            return 5
        elif val[0] == 2:
            return 4
        else:
            return 2
    elif jCount == 2:
        if val[0] == 3:
            return 7
        elif val[0] == 2:
            return 6
        else:
            return 4
    elif jCount == 3:
        if val[0] == 2:
            return 7
        else:
            return 6
    elif jCount > 3:
        return 7
    else:
        if val[0] == 5:
            return 7
        elif val[0] == 4:
            return 6
        elif val[0] == 3 and val[1] == 2:
            return 5
        elif val[0] == 3:
            return 4
        elif val[0] == 2 and val[1] == 2:
            return 3
        elif val[0] == 2:
            return 2
        return 1


def value_getter(item):
    return item["type"], item["value"]


def day7part1():
    with open("7.txt") as file:
        testMap = {}
        sum = 0
        for line in file:
            parts = re.split(r'\s+', line)
            testMap[parts[0]] = {"type":findHandType(parts[0]),
                                 "value":handValue(parts[0]),
                                 "bid":int(parts[1])}
        sortedList = sorted(testMap.values(), key=value_getter)
        for i in range(len(sortedList)):
            sum += (i+1)*sortedList[i]['bid']
        print(sum)


def day7part2():
    with open("7.txt") as file:
        testMap = {}
        sum = 0
        for line in file:
            parts = re.split(r'\s+', line)
            testMap[parts[0]] = {"type":findHandType(parts[0]),
                                 "value":handValue(parts[0], False),
                                 "bid":int(parts[1])}
        sortedList = sorted(testMap.values(), key=value_getter)
        for i in range(len(sortedList)):
            sum += (i+1)*sortedList[i]['bid']
        print(sum)

