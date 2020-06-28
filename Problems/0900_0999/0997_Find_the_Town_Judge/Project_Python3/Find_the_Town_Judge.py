# coding: utf-8

import os
import sys
import time

class Solution:
#   def findJudge(self, N: int, trust: List[List[int]]) -> int:
    def findJudge(self, N, trust):
        l = [0]*(N + 1)
        for villager, judge in trust:
            l[judge] += 1
            l[villager] -= 1
        
        for i in range(1, N + 1):
            if l[i] == N - 1:
                return i
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
    flds = temp.replace("\"", "").rstrip().split("],[[")

    N = int(flds[0].replace("[", "").replace("]", ""))
    flds1 = flds[1].replace("]]]", "").split("],[")

    trust = [[int(col) for col in data.split(",")] for data in flds1]
    print("N = {0:d}, trust = {1}".format(N, trust))

    sl = Solution()
    time0 = time.time()

    result = sl.findJudge(N, trust)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
