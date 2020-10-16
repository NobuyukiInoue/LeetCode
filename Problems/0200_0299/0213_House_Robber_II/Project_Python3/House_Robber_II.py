# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def rob(self, nums: List[int]) -> int:
    def rob0(self, nums):
        # 32ms
        def simple_rob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

    def rob1(self, nums):
        # 36ms
        def rob_sub(nums, circle=True):
            if circle:
                return max([0] + [nums[i] + rob_sub((nums[i:] + nums[0:i])[2:-1], False) for i in range(len(nums))])
            pre, now = 0, 0
            for i in nums: pre, now = now, max(pre + i, now)
            return now

        return rob_sub(nums, True)

    def rob(self, nums):
        # 28ms
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        else:
            s1 = self.rob_a_line(nums[0:len(nums) - 1], 0, dict())
            s2 = self.rob_a_line(nums[1:], 0, dict())
            return max(s1, s2)

    def rob_a_line(self, nums, i, mem):
        if i == len(nums) - 1:
            return nums[i]
        if i == len(nums) - 2:
            return max(nums[i], nums[i + 1])
        else:
            s1, s2 = None, None

            if i + 2 in mem:
                s1 = nums[i] + mem[i + 2]
            else:
                to_mem = self.rob_a_line(nums, i + 2, mem)
                s1 = nums[i] + to_mem
                mem[i + 2] = to_mem

            if i < len(nums) - 3:
                if i + 3 in mem:
                    s2 =  nums[i + 1] + mem[i + 3]
                else:
                    to_mem = self.rob_a_line(nums, i + 3, mem)
                    s2 = nums[i + 1] + to_mem
                    mem[i + 3] = to_mem
            else:
                s2 = nums[i + 1]

            return max(s1, s2)

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

    result = sl.rob(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
