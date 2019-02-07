# coding: utf-8

import os
import sys
import time
import copy

class Solution:
    def findErrorNums(self, nums):
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]

    def findErrorNums2(self, nums: 'List[int]') -> 'List[int]':
        nums.sort()
        print("sorted nums = %s" %nums)

        results = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i - 1]:
                results.append(nums[i])
                results.append(nums[i] + 1)
        return results

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

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    tempStr = temp.replace("[","").replace("]","").rstrip()
    flds = tempStr.split(',')
    nums = array_str_to_int(flds)

    print("nums = %s" %nums)

    time0 = time.time()

    sl = Solution()
    result = sl.findErrorNums(nums)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
