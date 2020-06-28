# coding: utf-8

import os
import sys
import time

class Solution:
#   def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
    def maxAbsValExpr(self, arr1, arr2):
        # 320ms
        return max(max(l) - min(l) for l in ([a*x + b*y + i for i, (a, b) in enumerate(zip(arr1, arr2))] for x, y in ((1, 1), (1, -1), (-1, 1), (-1, -1))))

    def maxAbsValExpr2(self, arr1, arr2):
        # 380ms
        res, n = 0, len(arr1)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            closest = p * arr1[0] + q * arr2[0] + 0
            for i in range(n):
                cur = p * arr1[i] + q * arr2[i] + i
                res = max(res, cur - closest)
                closest = min(closest, cur)
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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    arr1 = [int(n) for n in flds[0].split(",")]
    arr2 = [int(n) for n in flds[1].split(",")]

    print("arr1 = {0}, arr2 = {1}".format(arr1, arr2))

    sl = Solution()
    time0 = time.time()
    result = sl.maxAbsValExpr(arr1, arr2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
