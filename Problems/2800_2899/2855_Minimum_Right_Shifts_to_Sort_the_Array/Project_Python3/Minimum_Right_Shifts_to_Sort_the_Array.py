import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        # 46ms - 56ms
        n, ind, pos = len(nums), 0, 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                ind = i
                pos += 1
        if pos > 1:
            return -1
        if ind == 0:
            return 0
        return -1 if nums[n - 1] > nums[0] else n - ind 

    def minimumRightShifts2(self, nums: List[int]) -> int:
        # 55ms
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                nums = nums[i:] + nums[:i]
                return n - i if nums == sorted(nums) else -1
        return 0

    def minimumRightShifts3(self, nums: List[int]) -> int:
        # 56ms
        sorted_nums = sorted(nums)
        result = 0
        while result < len(nums):
            if nums == sorted_nums:
                return result
            result += 1
            last_element = nums.pop()
            nums.insert(0, last_element)
        return -1

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

    result = sl.minimumRightShifts(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
