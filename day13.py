import numpy as np


def day13part1():
  with open("13.txt") as file:
      lines = [list(line.strip()) for line in file]
      lineBreaks = []
      i = 0
      while i < len(lines):
          if len(lines[i]) == 0:
              lineBreaks.append(i)
          i += 1
      lineBreaks.append(len(lines))
      start = 0
      h = []
      v = []
      for index in lineBreaks:
          print(index)
          data = np.array(lines[start:index])
          i = 0
          found = False
          while i < len(data) - 1:
             if (data[i] == data[i+1]).all():
                 if len(data) % 2 == 0 and i == len(data)/2-1:
                     if (data[0:i] == data[i+2:][::-1]).all():
                         h.append(i+1)
                         found = True
                         break
                 elif i > len(data) - (i + 2):
                     l = len(data) - (i + 2)
                     if (data[i-l:i] == data[i+2:][::-1]).all():
                         h.append(i+1)
                         found = True
                         break
                 else:
                     if (data[0:i] == data[i+2:i+2+i][::-1]).all():
                         h.append(i+1)
                         found = True
                         break
             i += 1
          if not found:
              i = 0
              while i < len(data[0]) - 1:
                  if (data[:,i] == data[:,i+1]).all():
                      if len(data[0]) % 2 == 0 and i == len(data[0])/2-1:
                          if (data[:,0:i] == data[:,i+2:][::,::-1]).all():
                              v.append(i+1)
                              break
                      elif i > len(data[0]) - (i + 2):
                          l = len(data[0]) - (i + 2)
                          if l == 0:
                              v.append(i+1)
                              break
                          if (data[:,i-l:i] == data[:,-l:][::,::-1]).all():
                              v.append(i+1)
                              break
                      else:
                          if (data[:,0:i] == data[:,i+2:i+2+i][::,::-1]).all():
                              v.append(i+1)
                              break
                  i += 1
          start = index+1
      print(sum(v) + 100*sum(h))
