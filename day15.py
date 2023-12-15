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
