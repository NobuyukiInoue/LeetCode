# coding: utf-8

import json
import os
import sys
import time

class Solution:
#   def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
    def escapeGhosts(self, ghosts: [[int]], target: [int]) -> bool:
        # 40ms
        return abs(target[0])+abs(target[1])< min([abs(g[0]-target[0])+abs(g[1]-target[1]) for g in ghosts ])

    def escapeGhosts2(self, ghosts: [[int]], target: [int]) -> bool:
        # 48ms
        t = abs(target[0]) + abs(target[1])
        for g in ghosts:
            if t >= abs(g[0] - target[0]) + abs(g[1] - target[1]):
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
    flds = temp.replace(" ", "").replace("\"", "").rstrip().split("]],[")
    ghosts = [[int(n) for n in pt.split(",")] for pt in flds[0].replace("[[[", "").split("],[")]
    target = [int(pt) for pt in flds[1].replace("]]", "").split(",")]
    print("ghosts = {0}, target = {1}".format(ghosts, target))

    sl = Solution()
    time0 = time.time()

    result = sl.escapeGhosts(ghosts, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
