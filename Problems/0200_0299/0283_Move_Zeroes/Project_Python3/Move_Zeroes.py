# coding: utf-8

import os
import sys
import time
import copy

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = nums[:]
        dst_i = 0
        for src_i in range(len(nums)):
            if temp[src_i] != 0:
                nums[dst_i] = temp[src_i] 
                dst_i += 1
        
        for leaset_i in range(dst_i, len(nums)):
            nums[leaset_i] = 0

    def moveZeroes_old1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = [0]*len(nums)
        dst_i = 0
        for src_i in range(len(nums)):
            if nums[src_i] != 0:
                temp[dst_i] = nums[src_i] 
                dst_i += 1
        for i in range(len(temp)):
            nums[i] = temp[i]
        '''
        nums = copy.deepcopy(temp)
        '''

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

    sl.moveZeroes(nums)

    time1 = time.time()

    print("result = {0}".format(nums))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
