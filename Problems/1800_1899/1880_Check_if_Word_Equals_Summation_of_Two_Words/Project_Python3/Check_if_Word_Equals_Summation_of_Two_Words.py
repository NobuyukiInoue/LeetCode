import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # 32ms
        numeric_total = lambda s: int(''.join([str(ord(letter) - ord('a')) for letter in s]))
        return numeric_total(firstWord) + numeric_total(secondWord) == numeric_total(targetWord)

    def isSumEqual2(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # 32ms
        numFirst, numSecond, numTarget = 0, 0, 0
        s = ""
        for ch in firstWord:
            s += chr(ord(ch) - ord('a') + 0x30)
        numFirst = int(s)
        s = ""
        for ch in secondWord:
            s += chr(ord(ch) - ord('a') + 0x30)
        numSecond = int(s)
        s = ""
        for ch in targetWord:
            s += chr(ord(ch) - ord('a') + 0x30)
        numTarget = int(s)
        return numFirst + numSecond == numTarget

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    firstWord, secondWord, targetWord = flds[0], flds[1], flds[2]
    print("firstWord = {0}, secondWord = {1}, targetWord = {2}".format(firstWord, secondWord, targetWord))

    sl = Solution()
    time0 = time.time()

    result = sl.isSumEqual(firstWord, secondWord, targetWord)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
