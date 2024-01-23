import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # 538ms - 579ms
        new_nums = []
        for row in nums:
            new_nums.append(sorted(row, reverse=True))
        trans = zip(*new_nums)
        s = 0
        for cols in trans:
            s += max(cols)
        return s

    def matrixSum2(self, nums: List[List[int]]) -> int:
        # 581ms - 585ms
        for i, row in enumerate(nums):
            nums[i] = sorted(row, reverse=True)
        ans = 0
        for col in range(len(nums[0])):
            col_max = nums[0][col]
            for i in range(1, len(nums)):
                col_max = max(col_max, nums[i][col])
            ans += col_max
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    nums = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()

    result = sl.matrixSum(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
