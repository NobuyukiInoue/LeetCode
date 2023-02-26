# coding: utf-8

import heapq
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 35ms
        n = len(citations)
        citations.sort()
        i = 0
        while i < n and n - i > citations[i]:
            i += 1
        return n - i

    def hIndex_user_heapq(self, citations: List[int]) -> int:
        # 31ms - 39ms
        cit = [-i for i in citations]
        heapq.heapify(cit)
        res, i = 0, 1
        while i <= len(citations):
            if i > -heapq.heappop(cit):
                break
            res = i
            i += 1
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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    citations = [int(n) for n in flds.split(",")]
    print("citations = {0}".format(citations))

    sl = Solution()

    time0 = time.time()

    result = sl.hIndex(citations)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
