# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    def createTargetArray(self, nums, index):
        # 32ms
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res

    def createTargetArray_work(self, nums, index):
        # 32ms
        res = []
        for i in range(len(nums)):
            if index[i] == len(res):
                res.append(nums[i])
            else:
                list1 = res[:index[i]]
                list1.append(nums[i])
                list2 = res[index[i]:]
                res = list1 + list2

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(col) for col in flds[0].split(",")]
    index = [int(col) for col in flds[1].split(",")]
    print("nums = {0}, index = {1}".format(nums, index))

    sl = Solution()
    time0 = time.time()
    result = sl.createTargetArray(nums, index)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
