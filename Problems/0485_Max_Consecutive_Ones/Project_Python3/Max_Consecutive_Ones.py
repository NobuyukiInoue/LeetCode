# coding: utf-8

import os
import sys
import time

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max, count = 0, 0
        for n in nums:
            if n == 0:
                count = 0
                continue
            count += 1
            if count > max:
                max = count
        
        return max

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


def loop_main(temp):
    flds = temp.replace("[","").replace("]","").rstrip().split(",")

    nums = [0]*len(flds)
    for i in range(len(flds)):
        nums[i] = int(flds[i])

    time0 = time.time()

    sl = Solution()
    result = sl.findMaxConsecutiveOnes(nums)
    print("result = %d" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
