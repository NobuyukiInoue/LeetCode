# coding: utf-8

import os
import sys
import time

class Solution:
#   def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        dp = []
        dp_max = [0]
        dp_2 = []
        dp_2_max = [0]
        prices = prices[::-1]
        for i, price in enumerate(prices):
            if i>=2:dp_2.append(price+dp_max[i-1])
            else:dp_2.append(price)
            dp_2_max.append(max(dp_2_max[-1],dp_2[-1]))
            dp.append(dp_2_max[-1]-price)
            dp_max.append(max(dp[-1],dp_max[-1]))
        return dp_max[-1]

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

    prices = [int(val) for val in flds]
    print("prices = {0}",format(prices))

    sl = Solution()
    time0 = time.time()

    result = sl.maxProfit(prices)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
