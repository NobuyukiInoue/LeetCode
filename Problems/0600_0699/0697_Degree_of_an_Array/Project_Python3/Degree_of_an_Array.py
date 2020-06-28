# coding: utf-8

import os
import sys
import time

class Solution:
#    def findShortestSubArray(self, nums: List[int]) -> int:
    def findShortestSubArray(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        degree = max(dic.values())
        if degree == 1:
            return 1
        max_vec = []
        for i in dic:
            if dic[i] == degree:
                max_vec.append(i)
                
        shortest_len = float('inf')
        for i in range(len(max_vec)):
            temp = len(nums) - nums.index(max_vec[i]) - nums[::-1].index(max_vec[i])
            shortest_len = min(shortest_len,temp)
        return shortest_len

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

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()

    result = sl.findShortestSubArray(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
