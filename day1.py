import re

def day1part2():
    replacements = [("one", "o1e"), ("two", "t2o"), ("three", "th3ee"), ("four", "fo4r"),
                  ("five", "fi5e"), ("six", "s6x"), ("seven", "se7en"), ("eight", "ei8ht"),
                  ("nine", "ni9e")]

    with open("1.txt") as file:
        sum = 0
        for line in file:
            for pat,repl in replacements:
                line = re.sub(pat, repl, line)
            start = ""
            end = ""
            i = 0
            for c in line:
                if c.isdigit():
                    start = c
                    break
                i += 1
            i = len(line) - 1
            for c in reversed(line):
                if c.isdigit():
                    end = c
                    endI = i
                    endSet = True
                    break
                i -= 1

            sum += int(str(start) + str(end))
        print(sum)
