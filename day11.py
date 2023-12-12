import numpy as np

def day11part1():
  with open("11.txt") as file:
      lines = [list(line.strip()) for line in file]
      t = np.array(lines)
      i = 0
      while i < len(t):
          if not '#' in t[i]:
              t = np.insert(t, i, '.', axis=0)
              i += 1
          i += 1
      i = 0
      while i < len(t[0]):
          if not '#' in t[:,i]:
              t = np.insert(t, i, '.', axis=1)
              i += 1
          i += 1
  
      indexes = list(zip(*np.where(t == '#')))
      i = 0
      distance = 0
      while i < len(indexes):
          pair = indexes[i]
          j = i + 1
          while j < len(indexes):
              nxtPair = indexes[j]
              distance += abs(nxtPair[0] - pair[0]) + abs(nxtPair[1] - pair[1])
              j += 1
          i += 1
      print(distance)


def day11part2():
  with open("11.txt") as file:
      lines = [list(line.strip()) for line in file]
      t = np.array(lines)
      i = 0
      rowIndexes = []
      while i < len(t):
          if not '#' in t[i]:
              rowIndexes.append(i)
          i += 1
      i = 0
      columnIndexes = []
      while i < len(t[0]):
          if not '#' in t[:,i]:
              columnIndexes.append(i)
              # i += 1
          i += 1
      indexes = list(zip(*np.where(t == '#')))
  
      i = 0
      distance = 0
      while i < len(indexes):
          pair = indexes[i]
          j = i + 1
          while j < len(indexes):
              nxtPair = indexes[j]
              rcount = 0
              ccount = 0
              for r in rowIndexes:
                  if pair[0] < r < nxtPair[0] or pair[0] > r > nxtPair[0]:
                      rcount += 1000000-1
              for c in columnIndexes:
                  if pair[1] < c < nxtPair[1] or pair[1] > c > nxtPair[1]:
                      ccount += 1000000-1
              print(f"{rcount},{ccount}")
              distance += abs(nxtPair[0] - pair[0])+rcount + abs(nxtPair[1] - pair[1])+ccount
              j += 1
          i += 1
      print(distance)
