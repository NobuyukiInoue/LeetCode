# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # 168ms
        dic = collections.Counter(hand)
        for i in sorted(dic):
            if dic[i] > 0:
                for j in range(W)[::-1]:
                    dic[i + j] -= dic[i]
                    if dic[i + j] < 0:
                        return False
        return True

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    hand = [int(n) for n in flds[0].split(",")]
    W = int(flds[1])
    print("code = {0}, W = {1:d}".format(hand, W))

    sl = Solution()

    time0 = time.time()

    result = sl.isNStraightHand(hand, W)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
