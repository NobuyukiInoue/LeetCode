# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # 320ms
        return all(abs(A[i] - i) <= 1 for i in range(len(A)))

    def isIdealPermutation2(self, A: List[int]) -> bool:
        # 344ms
        cmax = 0
        for i in range(len(A) - 2):
            cmax = max(cmax, A[i])
            if cmax > A[i + 2]:
                return False
        return True

    def isIdealPermutation_bad(self, A: List[int]) -> bool:
        # Time Limite Exceeded.
        lenA = len(A)
        count1, count2 = 0, 0
        for i in range(lenA - 1):
            if A[i] > A[i + 1]:
                count2 += 1
            for j in range(i + 1, lenA):
                if A[i] > A[j]:
                    count1 += 1
        return (count1 == count2)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    A = [int(n) for n in flds.split(",")]
    print("A = {0}".format(A))

    sl = Solution()

    time0 = time.time()

    result = sl.isIdealPermutation(A)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
