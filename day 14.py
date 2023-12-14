def day14part1():
    with open("14.txt") as file:
        lines = [list(line.strip()) for line in file]
        i = 1
        while i < len(lines):
            k = i
            while k > 0:
                j = 0
                while j < len(lines[k]):
                    if lines[k][j] == 'O' and lines[k-1][j] == '.':
                        lines[k][j] = '.'
                        lines[k-1][j] = 'O'
                    j += 1
                k -= 1
            i += 1

        load = 0
        i = 0
        while i < len(lines):
            j = 0
            while j < len(lines[i]):
                if lines[i][j] == 'O':
                    load += len(lines) - i
                j += 1
            i += 1
        print(load)
