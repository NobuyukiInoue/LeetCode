# coding: utf-8

import os
import sys
import time

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        sum_max = 0
        min = sys.maxsize
        for i in range(len(prices)):
            if min > prices[i]:
                min = prices[i]
            profit = prices[i] - min
            if profit > max:
                max = profit
            if profit > 0:
                sum_max += profit
                min = prices[i]
        
        if max > sum_max:
            return max
        else:
            return sum_max

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    prices = [int(val) for val in flds.split(",")]
    print("prices = %s" %prices)

    time0 = time.time()

    sl = Solution()
    result = sl.maxProfit(prices)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
