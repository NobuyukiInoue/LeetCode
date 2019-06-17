# coding: utf-8

import os
import sys
import time

class Solution:
#   def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        if nums == []:
           return -1
        l, r = 0, len(nums) - 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        while l < r:
            if nums[l]==target:
                return l
            elif nums[r]==target:
                return r
            else:
                m = (l + r)//2
                if nums[m] > target:
                    r -= 1
                elif nums[m] < target:
                    l += 1
                else:
                    return m
        return -1

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
    print("nums = %s, target = %d" %(nums, target))

    time0 = time.time()

    sl = Solution()
    result = sl.search(nums, target)

    time1 = time.time()

    print("result = %d" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
