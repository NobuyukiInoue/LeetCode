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

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

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
    flds = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()
    nums = str_to_int_array(flds)

    print("nums = %s" %nums)
    time0 = time.time()

    sl = Solution()
    result = sl.majorityElement(nums)

    time1 = time.time()
    print("result = %d" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()