# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def findLongestChain(self, pairs: List[List[int]]) -> int:
    def findLongestChain(self, pairs: [[int]]) -> int:
        # 204ms
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]:
                cur, res = p[1], res + 1
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
    flds = temp.replace(" ","").replace("\"","").replace("[[", "").replace("]]", "").rstrip()

    pairs = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print("pairs = {0}".format(pairs))

    sl = Solution()
    time0 = time.time()

    result = sl.findLongestChain(pairs)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
