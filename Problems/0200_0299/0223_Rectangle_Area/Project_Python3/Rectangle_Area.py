# coding: utf-8

import collections
import os
import sys
import time

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (G - E) * (H - F) + (C - A) * (D - B) - (max(min(C, G)  -  max(E, A), 0) * max(min(D, H) - max(F, B), 0))

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

    nums = [int(n) for n in flds.split(",")]
    A, B, C, D, E, F, G, H = nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7]
    print("A = {0:d}, B = {1:d}, C = {2:d}, D = {3:d}, E = {4:d}, F = {5:d}, G = {6:d}, H = {7:d}".format(A, B, C, D, E, F, G, H))

    sl = Solution()
    time0 = time.time()
    result = sl.computeArea(A, B, C, D, E, F, G, H)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
