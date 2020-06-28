# coding: utf-8

import os
import sys
import time
from collections import Counter as cnt

class Solution:
#   def longestCommonPrefix(self, strs: List[str]) -> str:
    def longestCommonPrefix(self, strs):
        # 40ms
        return ''.join(['#']+[[' ',p[0]][len(set(p))==1] for p in zip(*strs)]).split()[0][1:]

    def longestCommonPrefix2(self, strs):
        # 40ms
        if strs == []:
            return ""
        minLen = len(strs[0])
        for s in strs:
            minLen = min(minLen, len(s))
        idx = 0
        for col in range(minLen):
            for row in range(len(strs)):
                if strs[0][col] != strs[row][col]:
                    return strs[0][0:idx]
            idx += 1
        return strs[0][0:idx]

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
    strs = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    print("strs = {0}".format(strs))

    sl = Solution()
    time0 = time.time()

    result = sl.longestCommonPrefix(strs)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
