# coding: utf-8

import os
import sys
import time

class Solution:
#  def canJump(self, nums: List[int]) -> bool:
   def canJump(self, nums):
        # 96ms
        if len(nums) < 2:
            return True
        for curr in range(len(nums) - 2, -1, -1):
            if nums[curr] == 0:
                neededJumps = 1
                while neededJumps > nums[curr]:
                    neededJumps +=1
                    curr -= 1
                    if curr < 0:
                        return False
        return True

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
    nums = [int(n) for n in flds]

    sl = Solution()
    time0 = time.time()

    result = sl.canJump(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
