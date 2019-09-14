# coding: utf-8

import bisect
import os
import sys
import time

class Solution:
#   def countSmaller(self, nums: List[int]) -> List[int]:
    def countSmaller(self, nums):
        # 112ms
        fir, sec, res = [], [], []
        for i in nums[::-1]:
            res += [bisect.bisect_left(fir,i) + bisect.bisect_left(sec,i)]
            bisect.insort_left(sec,i)
            if len(fir) < 4*len(sec):
                fir = sorted(fir+sec)
                sec = []
        return res[::-1]

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    nums = [int(val) for val in flds]
    print("nums = %s" %nums)

    time0 = time.time()

    sl = Solution()
    result = sl.countSmaller(nums)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
