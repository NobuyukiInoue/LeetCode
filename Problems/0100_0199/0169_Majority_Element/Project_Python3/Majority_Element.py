# coding: utf-8

import os
import sys
import time

class Solution:
#    def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums):
        from collections import Counter # 48ms
        count = Counter(nums)
        for k, v in count.items():
            if v >= len(nums) / 2:
                return k

    def majorityElement2(self, nums):
        result = [ x for x in set(nums) if nums.count(x) > len(nums)/2 ]
        return result[0]

    def majorityElement3(self, nums):   # 60ms
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement_work(self, nums):   # 60ms
        dic = {}
        for num in nums:
            if not num in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1
        max_val, max_key = 0, 0
        for key, val in dic.items():
            if val > max_val:
                max_val = val
                max_key = key
        return max_key

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
    flds = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()

    nums = [int(val) for val in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.majorityElement(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
