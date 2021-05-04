import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 96ms
        dominoes = 'L' + dominoes + 'R'
        res = ""
        left = 0
        for right in range(1, len(dominoes)):
            if dominoes[right] == '.':
                continue
            middle = right - left - 1
            if left:
                res += dominoes[left]
            if dominoes[left] == dominoes[right]:
                res += dominoes[left] * middle
            elif dominoes[left] == 'L' and dominoes[right] == 'R':
                res += '.' * middle
            else:
                res += 'R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2)
            left = right
        return res

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
    dominoes = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("dominoes = {0}".format(dominoes))

    sl = Solution()
    time0 = time.time()

    result = sl.pushDominoes(dominoes)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
