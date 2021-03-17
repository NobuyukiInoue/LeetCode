# coding: utf-8

import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def queensAttacktheKing2(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # 36ms
        [I, J], A, S, T = king, [0]*9, set(itertools.product(range(8),range(8))), [(i, j) for i, j in itertools.product(range(-1, 2),range(-1, 2))]
        for i, (j, (a, b)) in itertools.product(range(1,8),enumerate(T)):
                if not A[j] and (I + i*a,J + i*b) in S and [I + i*a,J + i*b] in queens:
                    A[j] = [I + i*a,J + i*b]
        return [p for p in A if p != 0]

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # 32ms
        [I, J], A = king, []
        for e, d in enumerate([I, J]):
            for a,b,c in (d - 1, -1, -1),(d + 1, 8, 1):
                for i in range(a, b, c):
                    p = [i,J] if e == 0 else [I,i]
                    if p in queens:
                        A.append(p)
                        break
        for d in [1, -1]:
            for a, b, c in (J - 1, -1, -1),(J + 1, 8, 1):
                for j in range(a, b, c):
                    if I + d*(J - j) < 8 and [I + d*(J - j), j] in queens:
                        A.append([I + d*(J - j), j])
                        break
        return A

    def queensAttacktheKing_work(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        targets = []
        for queen in queens:
            if abs(queen[0] - king[0]) <= 1 and abs(queen[1] - king[1]) <= 1:
                targets.append(queen)
            elif abs(queen[0] - king[0]) == abs(queen[1] - king[1]):
                targets.append(queen)
        return targets

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
    flds = temp.replace("[[[","").replace("\"","").replace(" ","").rstrip().split("]],[[")
    queens = [[int(_) for _ in fld.split(",")] for fld in flds[0].split("],[")]
    print("queens = {0}".format(queens))
    king = [int(_) for _ in flds[1].replace("]", "").split(",")]
    print("king = {0}".format(king))

    sl = Solution()

    time0 = time.time()

    result = sl.queensAttacktheKing(queens, king)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
