# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def decompressRLElist(self, nums: List[int]) -> List[int]:
    def decompressRLElist(self, nums):
        # 60ms
        length, res = len(nums), []
        for i in range(0, length, 2):
            res.extend(nums[i]*[nums[i+1]])
        return res

    def decompressRLElist2(self, nums):
        # 92ms
        res = []
        for i in range(len(nums)//2):
            for _ in range(nums[2*i]):
                res.append(nums[2*i + 1])
        return res

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.decompressRLElist(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
