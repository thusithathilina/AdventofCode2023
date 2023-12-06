import re

def day2part1():
    with open("2.txt") as file:
        sum = 0
        red = 12
        green = 13
        blue = 14

        for line in file:
            gameNo = int(re.match(r'Game (\d+):', line).group(1))
            line = line.replace("Game " + str(gameNo)+":", "")
            skip = False
            for gameSet in line.split(";"):
                for oneSet in gameSet.split(","):
                    if not skip:
                        oneSet = oneSet.strip()
                        matchGroup = re.match(r'\s*(\d+)\s*(\w+)', oneSet)
                        if matchGroup is not None and not skip:
                            color = matchGroup.group(2)
                            count = int(matchGroup.group(1))

                            if color == 'red':
                                skip = count > red
                            elif color == 'green':
                                skip = count > green
                            else:
                                skip = count > blue
                    if skip:
                        break
                if skip:
                    break
            if not skip:
                sum += gameNo
                print(gameNo)
        print(sum)


def day2part2():
    with open("2.txt") as file:
        sum = 0
        for line in file:
            maxRed = 0
            maxGreen = 0
            maxBlue = 0
            gameNo = int(re.match(r'Game (\d+):', line).group(1))
            line = line.replace("Game " + str(gameNo)+":", "")
            for gameSet in line.split(";"):
                for oneSet in gameSet.split(","):
                    oneSet = oneSet.strip()
                    matchGroup = re.match(r'\s*(\d+)\s*(\w+)', oneSet)
                    if matchGroup is not None:
                        color = matchGroup.group(2)
                        count = int(matchGroup.group(1))
                        if color == 'red' and count > maxRed:
                            maxRed = count
                        elif color == 'green' and count > maxGreen:
                            maxGreen = count
                        elif color == 'blue' and count > maxBlue:
                            maxBlue = count
            print(f"{maxRed},{maxGreen},{maxBlue}")
            sum += (maxBlue*maxRed*maxGreen)
        print(sum)
