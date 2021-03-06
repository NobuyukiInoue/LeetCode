# coding: utf-8

import os
import sys
import time

class Solution:
#   def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums):
        if len(nums) < 1:
            return 0
        i, j = 1, 0
        ans = [0]
        while i < len(nums):
            if nums[i] > nums[ans[j]]:
                ans.append(i)
                j += 1
            else:
                l, r = -1, j
                while l < r-1:
                    m = l + (r - l)//2
                    if nums[ans[m]] >= nums[i]:
                        r = m
                    else:
                        l = m
                ans[r] = i
            i += 1
        return len(ans)

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

    result = sl.lengthOfLIS(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
