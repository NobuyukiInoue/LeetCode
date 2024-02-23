import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # 39ms - 40ms
        total, i, ans = nums[0] + nums[1], 0, 0
        while i + 1 < len(nums):
            if nums[i] + nums[i + 1] != total:
                break
            ans += 1
            i += 2
        return ans

    def maxOperations2(self, nums: List[int]) -> int:
        # 41ms
        total, ans = nums[0] + nums[1], 0
        for i in range(0, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] != total:
                break
            ans += 1
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

    result = sl.maxOperations(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
