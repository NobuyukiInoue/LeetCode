# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # 306ms - 740ms
        cnts = collections.defaultdict(int)
        ans, max_cnts = sys.maxsize, 0
        for _, num in enumerate(nums):
            if num % 2 == 0:
                cnts[num] += 1
                if cnts[num] == max_cnts:
                    ans = min(ans, num)
                if cnts[num] > max_cnts:
                    max_cnts = cnts[num]
                    ans = num
        if len(cnts) == 0:
            return -1
        return ans

    def mostFrequentEven_2liner(self, nums: List[int]) -> int:
        # 631ms - 695ms
        ctr = collections.Counter(nums)
        return max([c for c in ctr if not c%2], key = lambda x:(ctr[x], -x), default = -1)

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.mostFrequentEven(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
