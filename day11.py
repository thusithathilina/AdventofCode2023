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
