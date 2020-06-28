# coding: utf-8

import os
import sys
import time

class Solution:
#    def findLengthOfLCIS(self, nums: List[int]) -> int:
    def findLengthOfLCIS(self, nums):
        if len(nums) <= 0:
            return 0
        count, max_count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
        return max_count

    def findLengthOfLCIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        prev = nums[0]
        cur_max = 1
        tot_val = 1
        
        for i in range(1,len(nums)):
            if nums[i] > prev:
                cur_max+=1
                tot_val = max(cur_max,tot_val)
            else:
                cur_max = 1
                
            prev = nums[i]
            
        return tot_val

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
    flds = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip().split(",")

    nums = [0]*len(flds)
    for i in range(len(flds)):
        nums[i] = int(flds[i])
    print("nums[] = {0}".format(nums))

    sl = Solution()
    time0 = time.time()

    result = sl.findLengthOfLCIS(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
