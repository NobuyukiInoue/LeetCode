# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # 1056ms
        for x in [A[0],B[0]]:
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # 1100ms
        def get_count(num):
            rotations_a = rotations_b = 0 
            for i in range(length):
                if num != A[i] and num != B[i]:
                    return -1
                elif num != A[i]:
                    rotations_a +=1
                elif num != B[i]:
                    rotations_b +=1
            return min(rotations_a, rotations_b)
        length = len(A)
        rotations = get_count(A[0])
        if rotations != -1 or A[0] == B[0]:
            return rotations
        else:
            return get_count(B[0])

    def minDominoRotations_bad(self, A: List[int], B: List[int]) -> int:
        resA, resB = 0, 0
        nextA, nextB = True, True
        for i in range(len(A) - 1):
            if resA >= 0:
                if nextA:
                    if A[i] == A[i + 1]:
                        pass
                    elif A[i] == B[i + 1]:
                        resA += 1
                        nextA = False
                    else:
                        resA = -1
                else:
                    if B[i] == A[i + 1]:
                        nextA = True
                    elif B[i] == B[i + 1]:
                        resA += 1
                    else:
                        resA = -1
            if resB >= 0:
                if nextB:
                    if B[i] == B[i + 1]:
                        pass
                    elif B[i] == A[i + 1]:
                        resB += 1
                        nextB = False
                    else:
                        resB = -1
                else:
                    if A[i] == B[i + 1]:
                        pass
                    elif A[i] == A[i + 1]:
                        resB += 1
                    else:
                        resB = -1
        if resA == -1 and resB == -1:
            return -1
        elif resA == -1:
            return resB
        elif resB == -1:
            return resA
        return min(resA, resB)

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

    A = [int(n) for n in flds[0].split(",")]
    B = [int(n) for n in flds[1].split(",")]
    print("A = {0}".format(A))
    print("B = {0}".format(B))

    sl = Solution()

    time0 = time.time()

    result = sl.minDominoRotations(A, B)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
