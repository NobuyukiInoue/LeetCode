# coding: utf-8

import sys
import time
from functools import reduce

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


def output_nums(nums):
    resultStr = str(nums[0])

    for i in range(1, len(nums)):
        resultStr += "," + str(nums[i])
    return resultStr


def main():
    args = sys.argv
    argc = len(args)

    print("args[0] = %s %s" %(args[0], args[1]) )
    tempStr = args[1].rstrip()
    tempnums = tempStr.split(',')

    nums = [0]*len(tempnums)
    for i in range(0, len(tempnums)):
        nums[i] = int(tempnums[i])

    print("nums = %s" %(output_nums(nums)))

    time0 = time.time()

    sl = Solution()
    print("num = %s" %(sl.singleNumber(nums)))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
