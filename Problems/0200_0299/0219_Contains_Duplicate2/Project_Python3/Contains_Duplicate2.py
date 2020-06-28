# coding: utf-8

import os
import sys
import time

class Solution:
#    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    def containsNearbyDuplicate(self, nums, k):
        if len(list(set(nums))) == len(nums):
            return False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if j - i > k:
                    break
                if nums[i] == nums[j]:
                    return True
        return False

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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(val) for val in flds[0].split(",")]
    k = int(flds[1])
    print("nums = {0}".format(nums))
    print("k = {0}".format(k))

    sl = Solution()
    time0 = time.time()

    result = sl.containsNearbyDuplicate(nums, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
