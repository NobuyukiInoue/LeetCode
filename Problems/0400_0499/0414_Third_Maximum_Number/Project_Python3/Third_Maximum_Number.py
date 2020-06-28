# coding: utf-8

import os
import sys
import time
import copy

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array_max = [-(sys.maxsize - 1)]*3
        for i in range(len(nums)):
            if nums[i] > array_max[0]:
                array_max[2] = array_max[1]
                array_max[1] = array_max[0]
                array_max[0] = nums[i]
            elif nums[i] > array_max[1] and nums[i] != array_max[0]:
                array_max[2] = array_max[1]
                array_max[1] = nums[i]
            elif nums[i] > array_max[2] and nums[i] != array_max[0] and nums[i] != array_max[1]:
                array_max[2] = nums[i]

        if array_max[2] != -(sys.maxsize - 1):
            return array_max[2]
        else:
            return array_max[0]

def array_str_to_int(flds):
    if len(flds) <= 0:
        return None
    nums = [0]*len(flds)
    nums[0] = int(flds[0])
    for i in range(1, len(flds)):
        nums[i] = int(flds[i])
    return nums

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
    tempStr = temp.replace("[","").replace("]","").rstrip()
    flds = tempStr.split(',')
    nums = array_str_to_int(flds)

    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.thirdMax(nums)

    print("result = {0:d}".format(result))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
