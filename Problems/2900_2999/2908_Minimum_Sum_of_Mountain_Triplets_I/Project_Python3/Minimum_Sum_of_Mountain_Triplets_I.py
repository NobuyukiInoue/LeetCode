import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # 50ms - 51m
        pref = list(itertools.accumulate(nums, func = min))
        suff = list(itertools.accumulate(nums[::-1], func = min))[-3::-1]
        return min((p + n + s for p, n, s in zip(pref, nums[1:-1], suff) if (p < n and n > s)), default=-1)

    def minimumSum_normal(self, nums: List[int]) -> int:
        # 66ms - 72m
        ans, m = sys.maxsize, len(nums)
        for i in range(m - 2):
            for j in range(i + 1, m - 1):
                if nums[i] < nums[j]:
                    for k in range(j + 1, m):
                        if nums[k] < nums[j]:
                            ans = min(ans, nums[i] + nums[j] + nums[k])
        if ans == sys.maxsize:
            return -1
        return ans

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

    result = sl.minimumSum(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
