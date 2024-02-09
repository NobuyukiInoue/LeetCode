import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 465ms - 513ms
        piles.sort(reverse=True)
        return sum(piles[i] for i in range(1, len(piles)*2//3, 2))

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    piles = [int(n) for n in flds.split(",")]
    print("piles = {0}".format(piles))

    sl = Solution()

    time0 = time.time()

    result = sl.maxCoins(piles)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
