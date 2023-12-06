import re

def day3part1():
    with open("3.txt") as file:
        content = []
        for line in file:
            content.append(line.strip())
        sum = 0
        for i in range(len(content)):
            line = content[i]
            numbers = re.finditer(r'(\d+)', line)
            for matchGroup in numbers:
                previousI = matchGroup.span()[0]
                if previousI > 1:
                    previousI -= 1
                nextI = matchGroup.span()[1]
                if nextI == len(line):
                    nextI -= 1

                # in the same line
                if not previousI < 0 and bool(re.search(r'[^\d.]', line[previousI])):
                    sum += int(matchGroup.group())
                    continue
                elif not nextI > len(line) and bool(re.search(r'[^\d.]', line[nextI])):
                    sum += int(matchGroup.group())
                    continue

                if nextI < len(line):
                    nextI += 1
                # above and below lines
                if i > 0:
                    nextLine = content[i-1]
                    if bool(re.search(r'[^\d.]', nextLine[previousI:nextI])):
                        sum += int(matchGroup.group())
                        continue
                if i < len(content)-1:
                    previousLine = content[i+1]
                    if bool(re.search(r'[^\d.]', previousLine[previousI:nextI])):
                        sum += int(matchGroup.group())
        print(sum)
