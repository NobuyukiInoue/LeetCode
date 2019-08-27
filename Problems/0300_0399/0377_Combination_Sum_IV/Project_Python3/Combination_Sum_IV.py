# coding: utf-8

import os
import sys
import time

class Solution:
#   def combinationSum4(self, nums: List[int], target: int) -> int:
    def combinationSum4(self, nums, target):
        # 40ms
        dp = [0] * (target + 1)
        dp[0] = 1
        nums = sorted(nums)
        for i in range(1, target + 1):
            for n in nums:
                if n > i: break
                dp[i] += dp[i - n]
        return dp[-1]

    def combinationSum4_2(self, nums, target):
        # 48ms
        dp = [-1] * (target + 1)
        dp[0] = 1
        nums.sort()
        self.combo(nums, target, dp)
        return dp[target]

    def combo(self, nums, target, dp):
        if dp[target] != -1:
            return dp[target]
        
        dp[target] = 0
        for i in range(len(nums)):
            if target - nums[i] >= 0:
                dp[target] += self.combo(nums, target - nums[i], dp)
            else:
                return dp[target]
        
        return dp[target]
 
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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    target = int(flds[1])
    print("nums = {0}, K = {1:d}".format(nums, target))

    time0 = time.time()

    sl = Solution()
    result = sl.combinationSum4(nums, target)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
