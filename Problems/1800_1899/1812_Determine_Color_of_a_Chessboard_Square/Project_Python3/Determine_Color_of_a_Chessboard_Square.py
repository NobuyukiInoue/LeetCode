import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # 32ms
        if (ord(coordinates[0]) + ord(coordinates[1])) % 2 == 1:
            return True
        return False

    def squareIsWhite2(self, coordinates: str) -> bool:
        # 32ms
        return ord(coordinates[0]) % 2 != int(coordinates[1]) % 2

    def numDifferentIntegers3(self, word: str) -> int:
        # 32ms
        pos1, pos2 = -1, -1
        targets = []
        for i, ch in enumerate(word):
            ch_val = ord(ch)
            if ord('0') <= ch_val <= ord('9'):
                if pos1 == -1:
                    pos1 = i
            else:
                if pos1 >= 0:
                    pos2 = i
                    targetVal = int(word[pos1:pos2])
                    if not targetVal in targets:
                        targets.append(targetVal)
                    pos1 = -1
        if pos1 >= 0:
            pos2 = len(word)
            targetVal = int(word[pos1:pos2])
            if not targetVal in targets:
                targets.append(targetVal)
        return len(targets)

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
    coordinates = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("coordinates = {0}".format(coordinates))

    sl = Solution()
    time0 = time.time()

    result = sl.squareIsWhite(coordinates)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
