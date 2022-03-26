# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # 607ms
        return (dp := {}).update((x, dp.get(x - difference, 0) + 1) for x in arr) or max(dp.values())

    def longestSubsequence_4liner(self, arr: List[int], difference: int) -> int:
        # 666ms
        dp = collections.defaultdict(int)
        for x in arr:
            dp[x] = dp[x - difference] + 1
        return max(dp.values())

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    arr = [int(n) for n in flds[0].split(",")]
    difference = int(flds[1])
    print("arr = {0}, difference = {1:d}".format(arr, difference))

    sl = Solution()
    time0 = time.time()

    result = sl.longestSubsequence(arr, difference)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
