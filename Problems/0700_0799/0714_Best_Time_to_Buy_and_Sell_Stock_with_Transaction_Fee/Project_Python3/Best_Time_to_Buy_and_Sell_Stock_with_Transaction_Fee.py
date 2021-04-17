# coding: utf-8

import itertools
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 608ms
        n = len(prices)
        if n < 2:
             return 0
        ans = 0
        minimum = prices[0]
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                minimum = prices[i] - fee
        return ans

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        # 696ms
        for stock_price in prices:
            dp_not_hold = max(dp_not_hold, dp_hold + stock_price)
            dp_hold = max(dp_hold, dp_not_hold - stock_price - fee)
        return dp_not_hold if prices else 0

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    prices = [int(n) for n in flds[0].split(",")]
    fee = int(flds[1])
    print("prices = {0}, fee = {1:d}".format(prices, fee))

    sl = Solution()

    time0 = time.time()

    result = sl.maxProfit(prices, fee)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
