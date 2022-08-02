# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # 35ms - 61ms
        cnt = max(collections.Counter(ranks).values())
        ans = "High Card"   
        if len(set(suits)) == 1:
            ans = "Flush"
        elif cnt >= 3:
            ans = "Three of a Kind"
        elif cnt == 2:
            ans = "Pair"
        return ans

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    rands = [int(n) for n in flds[0].split(",")]
    suits = [_ for _ in flds[1].split(",")]
    print("rands = {0}, suits = {1}".format(rands, suits))

    sl = Solution()
    time0 = time.time()

    result = sl.bestHand(rands, suits)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
