import re


def day9part1():
    with open("/Users/thusithadayaratne/Downloads/adavent2023/9.txt") as file:
        total = 0
        for line in file:
            series = list(map(int, re.split(r'\s+', line.strip())))
            diffs = [series]
            index = 0
            while index < len(diffs):
                res = [j - i for i, j in zip(diffs[index][: -1], diffs[index][1 :])]
                if all(i == 0 for i in res):
                    break
                diffs.append(res)
                print(res)
                index += 1
            for i in range(len(diffs)-1, 0, -1):
                diffs[i-1].append(diffs[i-1][len(diffs[i-1])-1] + diffs[i][len(diffs[i])-1])
            total += diffs[0][-1]
        print(total)


def day9part2():
  with open("9.txt") as file:
      total = 0
      sum_of_extrapolated_values = 0
      indexL = 1
      for line in file:
          series = list(map(int, re.split(r'\s+', line.strip())))
          diffs = [series]
          index = 0
          while index < len(diffs):
              res = [j - i for i, j in zip(diffs[index][: -1], diffs[index][1 :])]
              if all(i == 0 for i in res):
                  break
              diffs.append(res)
              print(res)
              index += 1
          for i in range(len(diffs)-1, 0, -1):
              diffs[i-1].insert(0, diffs[i-1][0] - diffs[i][0])
          total += diffs[0][0]
      print(total)
