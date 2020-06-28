# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def canCross(self, stones: List[int]) -> bool:
    def canCross(self, stones):
        # 56ms
        stones_set = set(stones)
        step = 1
        for i in range(len(stones) - 1):
            if stones[i + 1] - stones[i] > step:
                return False
            step += 1
        def helper(start, end, step):
            if start == end:
                return True
            if start not in stones_set:
                return False
            if helper(start + step + 1, end, step + 1):
                return True
            if helper(start + step, end, step):
                return True
            if step > 1 and helper(start + step - 1, end, step - 1):
                return True
            return False
        return helper(1, stones[-1], 1)

    def canCross2(self, stones):
        # 108ms - 120ms
        step = 1
        for i in range(len(stones) - 1):
            if stones[i + 1] - stones[i] > step:
                return False
            step += 1
        def helper(start, end, step):
            if start == end:
                return True
            if start not in stones:
                return False
            if helper(start + step + 1, end, step + 1):
                return True
            if helper(start + step, end, step):
                return True
            if step > 1 and helper(start + step - 1, end, step - 1):
                return True
            return False
        return helper(1, stones[-1], 1)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    stones = [int(n) for n in flds.split(",")]
    print("stones = {0}".format(stones))

    sl = Solution()
    time0 = time.time()
    result = sl.canCross(stones)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
