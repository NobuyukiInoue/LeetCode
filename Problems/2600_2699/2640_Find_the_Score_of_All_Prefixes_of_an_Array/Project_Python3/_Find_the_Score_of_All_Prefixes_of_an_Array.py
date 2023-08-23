import itertools
import operator
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        # 425ms - 442ms
        n = len(nums)
        maxs = [0]*(n + 1)
        t_max = 0
        for i in range(n):
            t_max = max(t_max, nums[i])
            maxs[i + 1] = maxs[i] + t_max + nums[i]
        return maxs[1:]

    def findPrefixScore_2liner(self, nums: List[int]) -> List[int]:
        # 423ms - 427ms
        ans = itertools.accumulate(map(operator.add, nums, itertools.accumulate(nums, max)))
        return list(ans)

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

    result = sl.findPrefixScore(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
