# coding: utf-8

from functools import reduce
import os
import sys
import time

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_check = [False]*len(nums)

        for i in range(len(nums)):
            if nums_check[i]:
                continue

            for j in range(i + 1, len(nums)):
                if nums_check[j]:
                    continue
                if nums[i] == nums[j]:
                    nums_check[i] = nums_check[j] = True

            if nums_check[i] == False:
                return nums[i]

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
    flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").rstrip()

    nums = [int(val) for val in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.singleNumber(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
