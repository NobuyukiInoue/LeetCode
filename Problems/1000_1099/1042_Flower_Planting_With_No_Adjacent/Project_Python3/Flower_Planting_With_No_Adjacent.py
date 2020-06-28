# coding: utf-8

import os
import sys
import time

class Solution:
#   def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
    def gardenNoAdj(self, N, paths):
        res = [0] * N
        G = [[] for i in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
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
    str_args = temp.replace("\"","").replace("]]]","").rstrip()
    flds = str_args.split("],[[")
    N = int(flds[0].replace("[[", ""))

    paths = [[int(col) for col in data.split(",")] for data in flds[1].split("],[")]
    print("N = {0:d}, paths = {1}".format(N, paths))

    sl = Solution()
    time0 = time.time()

    result = sl.gardenNoAdj(N, paths)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
