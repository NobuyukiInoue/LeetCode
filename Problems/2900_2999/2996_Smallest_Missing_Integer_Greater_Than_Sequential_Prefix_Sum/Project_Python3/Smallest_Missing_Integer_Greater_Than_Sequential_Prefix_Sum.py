import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # 33ms - 37ms
        n, total = len(nums), nums[0]
        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                total += nums[i]
            else:
                break
        while True:
            if total not in nums:
                return total
            total += 1

    def missingInteger2(self, nums: List[int]) -> int:
        # 37ms - 45ms
        n = len(nums)
        total = nums[0]
        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                total += nums[i]
            else:
                break
        nums.sort()
        for num in nums:
            if total == num:
                total += 1
        return total

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

    result = sl.missingInteger(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
