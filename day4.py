import re

def day4part1():
  with open("4.txt") as file:
      sum = 0
      for line in file:
          parts = line.split(":")
          cardNo = int(parts[0].split("Card")[1].strip())
          parts = parts[1].strip().split("|")
          winning = list(map(int, re.split(r'\s+', parts[0].strip())))
          winning.sort()
          mine = list(map(int, re.split(r'\s+', parts[1].strip())))
          mine.sort()
  
          winIdx = 0
          mineIdx = 0
          count = 0
          while winIdx < len(winning) and mineIdx < len(mine):
              if winning[winIdx] == mine[mineIdx]:
                  count += 1
                  winIdx += 1
                  mineIdx += 1
              elif winning[winIdx] > mine[mineIdx]:
                  mineIdx += 1
              else:
                  winIdx += 1
          #ar^(n-1)
          if count > 0:
              sum += 2**(count-1)
      print(sum)


def day4part2():
    with open("4.txt") as file:
        sum = 0
        cardCount = {}
        cardWin = {}
        for line in file:
            parts = line.split(":")
            cardNo = int(parts[0].split("Card")[1].strip())
            parts = parts[1].strip().split("|")
            winning = list(map(int, re.split(r'\s+', parts[0].strip())))
            winning.sort()
            mine = list(map(int, re.split(r'\s+', parts[1].strip())))
            mine.sort()
    
            winIdx = 0
            mineIdx = 0
            count = 0
            while winIdx < len(winning) and mineIdx < len(mine):
                if winning[winIdx] == mine[mineIdx]:
                    count += 1
                    winIdx += 1
                    mineIdx += 1
                elif winning[winIdx] > mine[mineIdx]:
                    mineIdx += 1
                else:
                    winIdx += 1
            cardCount[cardNo] = 1
            cardWin[cardNo] = count
        for card in cardWin.keys():
            nextNCard = cardWin[card]
            times = cardCount[card]
            i = card + 1
            while i <= card + nextNCard:
                cardCount[i] += times
                i += 1
        for v in cardCount.values():
            sum += v
        print(sum)
