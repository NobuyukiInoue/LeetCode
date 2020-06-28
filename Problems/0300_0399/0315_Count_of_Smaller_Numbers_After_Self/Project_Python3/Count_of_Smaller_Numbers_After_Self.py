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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    nums = [int(val) for val in flds]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()

    result = sl.countSmaller(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
