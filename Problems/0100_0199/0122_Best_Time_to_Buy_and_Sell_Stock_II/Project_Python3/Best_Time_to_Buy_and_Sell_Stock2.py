import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 49ms - 56ms
        profit, prev = 0, prices[0]
        for price in prices:
            if price > prev:
                profit += price - prev
            prev = price
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        # 54ms - 74ms
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    def maxProfit3(self, prices: List[int]) -> int:
        # 61ms - 62ms
        p_max, p_min = 0, sys.maxsize
        sum_max = 0
        for price in prices:
            p_min = min(p_min, price)
            profit = price - p_min
            p_max = max(p_max, profit)
            if profit > 0:
                sum_max += profit
                p_min = price
        return p_max if p_max > sum_max else sum_max

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
