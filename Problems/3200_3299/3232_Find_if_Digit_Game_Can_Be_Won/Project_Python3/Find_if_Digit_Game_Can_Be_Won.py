import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        # 50ms - 58ms
        s_digits, d_digits = 0, 0
        for num in nums:
            if num < 10:
                s_digits += num
            elif num < 100:
                d_digits += num
        return False if s_digits == d_digits else True

    def canAliceWin2(self, nums: List[int]) -> bool:
        # 49ms - 55ms
        digits = [0, 0, 0]
        for num in nums:
            if num < 10:
                digits[0] += num
            elif num < 100:
                digits[1] += num
            else:
                digits[2] += num
        if digits[0] > digits[1] + digits[2] \
        or digits[1] > digits[0] + digits[2] \
        or digits[2] > digits[0] + digits[2]:
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

    result = sl.canAliceWin(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
