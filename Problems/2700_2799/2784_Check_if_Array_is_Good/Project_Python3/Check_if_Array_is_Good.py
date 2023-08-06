import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # 56ms - 57ms
        n = len(nums)
        return sorted(nums) == list(range(1, n))+[n - 1]

    def isGood(self, nums: List[int]) -> bool:
        # 55ms - 63ms
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] != prev + 1:
                return False
            prev = nums[i]
        if nums[-1] == len(nums) - 1 and nums[-2] == nums[-1]:
            return True
        return False

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

    result = sl.isGood(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
