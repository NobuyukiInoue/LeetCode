import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        # 399ms - 405ms
        ans = 0
        for i, j in itertools.combinations(range(len(nums)+1), 2):
            ans += all(n1 < n2 for n1, n2 in 
                itertools.pairwise(nums[:i]+ nums[j:]))
        return ans

    def incremovableSubarrayCount2(self, nums: List[int]) -> int:
        # 957ms - 1146ms
        ans, n = 0, len(nums)
        for i in range(n):
            for j in range(i, n):
                ok = True
                lst = -1
                for k in range(n):
                    if i <= k <= j:
                        continue
                    ok &= lst < nums[k]
                    lst = nums[k]
                ans += int(ok)
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

    result = sl.incremovableSubarrayCount(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
