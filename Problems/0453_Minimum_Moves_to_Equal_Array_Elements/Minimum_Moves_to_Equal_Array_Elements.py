# coding: utf-8

import os
import sys
import time
#from collections import defaultdict
import collections

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)
    
    def get_Max(self, nums):
        max = -1
        for i in range(0, len(nums)):
            if nums[i] > max:
                max = nums[i]
        return max


def str_to_int_array(flds):
    nums = [0]*len(flds)

    if len(flds) <= 0:
        return None
    for i in range(0, len(flds)):
        nums[i] = int(flds[i])

    return nums

def print_array(nums):
    resultStr = "[" + str(nums[0])
    for i in range(1, len(nums)):
        resultStr += "," + str(nums[i])
    return resultStr + "]"

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
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    var_str = temp.replace("[","").replace("]","").rstrip()
    flds = var_str.split(",")
    nums = str_to_int_array(flds)
    print("%s" %(print_array(nums)))

    time0 = time.time()

    sl = Solution()
    result = sl.minMoves(nums)

    print("result = %d" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
