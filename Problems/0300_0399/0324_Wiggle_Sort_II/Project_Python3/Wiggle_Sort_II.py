# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def wiggleSort(self, nums: List[int]) -> None:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 288ms
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


    def wiggleSort2(self, nums):
        # 192ms
        if not nums:
            return
        nums.sort()
        numsLength = len(nums)
        boundary = numsLength//2 if numsLength%2 == 0 else numsLength//2 + 1
        small_nums = nums[:boundary]
        large_nums = nums[boundary:]
        small_nums, large_nums = small_nums[::-1], large_nums[::-1]

        j, k = 0, 0
        for i in range(numsLength):
            if i%2 == 0:
                nums[i] = small_nums[j]
                j += 1
            else:
                nums[i] = large_nums[k]
                k += 1

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
    flds = temp.replace("[","").replace("]","").replace(" ","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    sl.wiggleSort(nums)

    time1 = time.time()

    print("result = {0}".format(nums))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
