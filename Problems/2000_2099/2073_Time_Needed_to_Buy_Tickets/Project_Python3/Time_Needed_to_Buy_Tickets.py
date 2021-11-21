# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # 36ms
        return sum(min(tickets[k] - (i > k), num) for i, num in enumerate(tickets))

    def timeRequiredToBuy2(self, tickets: List[int], k: int) -> int:
        # 36ms
        ans = 0
        for i, num in enumerate(tickets):
            if i > k:
                ans += min(tickets[k] - 1, num)
            else:
                ans += min(tickets[k], num)
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

    tickets = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("tickets = {0}, k = {1:d}".format(tickets, k))

    sl = Solution()
    time0 = time.time()

    result = sl.timeRequiredToBuy(tickets, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
