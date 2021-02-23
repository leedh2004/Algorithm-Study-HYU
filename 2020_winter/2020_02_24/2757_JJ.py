import sys


def parse(string):
  strList = list(string)
  rIdx = strList.index('R')
  cIdx = strList.index('C')
  rowNumber = int("".join(strList[rIdx+1:cIdx]))
  colummNumber = int("".join(strList[cIdx+1:]))
  return rowNumber,colummNumber

def getAlpha(columm):
  val = columm - 1
  ret = ""
  while True:
    ret = ret +  chr( ord('A') + (val%26))
    val = (val // 26)

    if val==0:
      break
    else :
      val = val - 1
  return ret[::-1]

while True:
  text = sys.stdin.readline()
  row,columm = parse(text)
  if row==0 and columm==0:
    break
  print(getAlpha(columm)+str(row))

