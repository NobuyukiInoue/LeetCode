# coding: utf-8

import os
import sys
import time


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp_nums = nums[:]

        for i in range(len(nums)):
            if i + k < len(nums):
                nums[i + k] = temp_nums[i]
            else:
                nums[(i + k) % len(nums)] = temp_nums[i]


def array_str_to_int(numbersStr):
    numbers = [0]*len(numbersStr)
    for i in range(len(numbersStr)):
        numbers[i] = int(numbersStr[i])
    return numbers


def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        print("argv[1] = %s" %temp)
        loop_main(temp)


def loop_main(temp):
    flds = temp.split(", ")
    numsStr = flds[0].replace("[","").replace("]","").split(",")
    nums = array_str_to_int(numsStr)
    k = int(flds[1])

    time0 = time.time()

    sl = Solution()
    sl.rotate(nums, k)
    print("nums(result) = %s" %nums)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
