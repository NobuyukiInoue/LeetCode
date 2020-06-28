# coding: utf-8

import os
import sys
import time

class Solution:
#   def nextPermutation(self, nums: List[int]) -> None:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                b, j = nums[i], i
                for k in range(i + 1, n):
                    if nums[k] > nums[i - 1]:
                        b, j = nums[k], k
                nums[j] = nums[i - 1]
                nums[i - 1] = b
                x = nums[i:n]
                x.sort()
                nums[i:n] = x
                break
            elif i == 1 and nums[i] < nums[i - 1]:
                nums.sort()

    def nextPermutation2(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 40ms
        firstSmaller = -1
        for i in reversed(range(1, len(nums))):
            if (nums[i] > nums[i - 1]):
                firstSmaller = i - 1
                break
        leastGreater = sys.maxsize
        leastGreaterIndex = 0
        if (firstSmaller == -1):
            nums.reverse()
            return
        for i in range(firstSmaller + 1, len(nums)):
            if (nums[i] > nums[firstSmaller] and leastGreater > nums[i]):
                leastGreater = nums[i]
                leastGreaterIndex = i
        nums[leastGreaterIndex] = nums[firstSmaller]
        nums[firstSmaller] = leastGreater
        nums[firstSmaller + 1:] = sorted(nums[firstSmaller + 1:])

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    nums = [int(val) for val in flds]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()

    sl.nextPermutation(nums)

    time1 = time.time()

    print("nums = {0}".format(nums))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
