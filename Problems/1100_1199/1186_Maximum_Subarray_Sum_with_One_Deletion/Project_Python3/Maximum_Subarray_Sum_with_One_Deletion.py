# coding: utf-8

import os
import sys
import time

from functools import lru_cache

class Solution:
#   def maximumSum(self, arr: List[int]) -> int:
    def maximumSum(self, arr):
        # 272ms
        notused, used, res = 0, 0, arr[0]
        for num in arr:
            if num >= 0:
                notused += num
                used += num
            else:
                notused = max(notused + num, used)
                used += num
            if notused != 0:
                val1 = notused
            else:
                val1 = float('-inf')
            if used != 0:
                val2 = used
            else:
                val2 = float('-inf')
            res = max([res, val1, val2])
            if notused < 0:
                notused = 0
            if used < 0:
                used = 0
        return max(res, max(arr))

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    arr = [int(n) for n in flds]
    print("arr = {0}".format(arr))

    time0 = time.time()

    sl = Solution()
    result = sl.maximumSum(arr)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
