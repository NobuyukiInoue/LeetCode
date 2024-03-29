import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 786ms - 795ms
        v_max, v_min = 0, sys.maxsize
        for price in prices:
            if v_min > price:
                v_min = price
            if price - v_min > v_max:
                v_max = price - v_min
        return v_max

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
    flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").rstrip()

    prices = [int(val) for val in flds.split(",")]
    print("prices = {0}".format(prices))

    sl = Solution()
    time0 = time.time()

    result = sl.maxProfit(prices)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
