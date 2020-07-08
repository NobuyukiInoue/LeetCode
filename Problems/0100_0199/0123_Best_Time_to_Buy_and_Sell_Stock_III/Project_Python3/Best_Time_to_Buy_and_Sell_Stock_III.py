# coding: utf-8

import os
import sys
import time
import numpy as np

class Solution:
#   def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        # 100ms
        pricesLength = len(prices)
        if pricesLength <= 1:
            return 0

        start, end = [0]*(pricesLength + 1), [0]*(pricesLength + 1)
        maxp = prices[-1]
        for i in range(pricesLength - 1, -1, -1):
            if prices[i] < maxp:
                start[i] = max(start[i + 1], maxp - prices[i])
            elif prices[i] >= maxp:
                start[i] = start[i + 1]
                maxp = prices[i]

        minp = prices[0]
        for i in range(1, pricesLength):
            if prices[i] > minp:
                end[i] = max(end[i - 1], prices[i] - minp)
            elif prices[i] <= minp:
                end[i] = end[i - 1]
                minp = prices[i]

        res = 0
        for i in range(pricesLength):
            if start[i + 1] + end[i] > res:
                res = start[i + 1] + end[i]
        return res

    def maxProfit2(self, prices):
        # 124ms
        if not prices:
            return 0
        sell, buyd, n, minp, maxp = [0], [0], len(prices), prices[0], prices[-1]
        for i in range(1, n):
            minp, maxp = min(minp, prices[i]), max(maxp, prices[n - i - 1])
            sell.append(max(sell[i - 1], prices[i] - minp))
            buyd.append(max(buyd[i - 1], maxp - prices[n - i - 1]))
        return max(sell[i] + buyd[n - i - 1] for i in range(n))

    def maxProfit3(self, prices):
        # 120ms
        if not prices:
            return 0

        k, pricesLength, T = 2, len(prices), []
        for t in range(k + 1):
            T.append([0]*pricesLength)

        for t in range(1, k + 1):
            maxdiff = -prices[0] + T[t - 1][0]
            for d in range(1, pricesLength):
                maxdiff = max(maxdiff, -prices[d - 1] + T[t - 1][d - 1])
                T[t][d] = max(T[t][d - 1], maxdiff + prices[d])

        return T[k][-1]

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
    flds = temp.replace("[","").replace("]","").rstrip().split(",")

    prices = [int(val) for val in flds]
    print("prices = {0}".format(prices))

    sl = Solution()
    time0 = time.time()

    result = sl.maxProfit(prices)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
