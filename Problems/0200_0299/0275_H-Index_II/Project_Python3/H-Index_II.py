# coding: utf-8

import bisect
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 134ms - 146ms
        n = len(citations)
        low, high = 0, n
        while low < high:
            mid = (low + high)//2
            k = n - mid
            if k > citations[mid]:
                low = mid + 1
            elif mid == 0 or k < citations[mid - 1]:
                high = mid
            else:
                return k
        return n - low

    def hIndex_use_reverse(self, citations: List[int]) -> int:
        # 137ms - 147ms
        citations = citations[::-1]
        for i, _ in enumerate(citations):
            if citations[i] <= i:
                return i
        return len(citations)

    def hIndex_use_bisect(self, citations: List[int]) -> int:
        # 176ms - 183ms
        for i in range(len(citations), -1, -1):
            if len(citations) - bisect.bisect_left(citations, i) >= i: return i
        return -1

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
