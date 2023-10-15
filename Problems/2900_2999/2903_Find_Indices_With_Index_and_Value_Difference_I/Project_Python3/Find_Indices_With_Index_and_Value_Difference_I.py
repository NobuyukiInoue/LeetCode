import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # 38ms - 45ms
        mini = maxi = 0
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[mini]:
                mini = i - indexDifference
            if nums[i - indexDifference] > nums[maxi]:
                maxi = i - indexDifference
            if nums[i] - nums[mini] >= valueDifference:
                return [mini, i]
            if nums[maxi] - nums[i] >= valueDifference:
                return [maxi, i]
        return [-1, -1]

    def findIndices2(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # 55ms - 59ms
        n = len(nums)
        for i in range(n - indexDifference):
            for j in range(i + indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    indexDifference = int(flds[1])
    valueDifference = int(flds[2])
    print("nums = {0}, indexDifference = {1:d}, valueDifference = {2:d}".format(nums, indexDifference, valueDifference))

    sl = Solution()
    time0 = time.time()

    result = sl.findIndices(nums, indexDifference, valueDifference)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
