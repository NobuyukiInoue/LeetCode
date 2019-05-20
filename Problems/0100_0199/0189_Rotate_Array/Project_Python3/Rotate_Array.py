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
    flds = temp.replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(val) for val in flds[0].split(",")]
    k = int(flds[1])
    print("nums = %s, k = %s" %(nums, k))

    time0 = time.time()

    sl = Solution()
    sl.rotate(nums, k)

    time1 = time.time()

    print("nums(result) = %s" %nums)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
