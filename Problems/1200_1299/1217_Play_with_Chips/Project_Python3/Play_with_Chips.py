# coding: utf-8

import os
import sys
import time

class Solution:
#   def minCostToMoveChips(self, chips: List[int]) -> int:
    def minCostToMoveChips(self, chips):
        # 32ms
        nOdd, nEven = 0, 0
        for i in chips:
            if i % 2 == 0:
                nEven += 1
            else:
                nOdd += 1
        return min(nEven, nOdd)

    def minCostToMoveChips_work(self, chips):
        # 36ms
        pos = {}
        for num in chips:
            if num in pos:
                pos[num] += 1
            else:
                pos[num] = 1
        """
        for k, v in pos.items():
            print("pos[{0:d}] = {1:d}".format(k, v))
        """
        result_even, result_odd = 0, 0
        for k, v in pos.items():
            if k % 2 == 0:
                result_even += v
            else:
                result_odd += v
        if result_even < result_odd:
            return result_even
        else:
            return result_odd

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

    chips = [int(n) for n in flds.split(",")]
    print("chips = {0}".format(chips))

    sl = Solution()
    time0 = time.time()
    result = sl.minCostToMoveChips(chips)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
