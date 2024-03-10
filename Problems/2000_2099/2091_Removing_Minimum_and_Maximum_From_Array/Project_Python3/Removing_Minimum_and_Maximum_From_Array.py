import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # 678ms - 684ms
        v_min, v_max = [nums[0], 0],[nums[0], 0]
        for i, num in enumerate(nums):
            if num < v_min[0]:
                v_min = [num, i]
            elif num > v_max[0]:
                v_max = [num, i]
        left, right = min(v_min[1], v_max[1]), max(v_min[1], v_max[1])
        n = len(nums)
        return min(right + 1, n - left, left + 1 + (n - right))

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

    result = sl.minimumDeletions(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
