# coding: utf-8

import sys
import time

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit


def array_str_to_int(work_str):
    resultArray = [0]*len(work_str)
    
    for i in range(0, len(work_str)):
        resultArray[i] = int(work_str[i])

    return resultArray


def main():
    args = sys.argv
    argc = len(args)

    print("args[0] = %s %s" %(args[0], args[1]) )
    str_prices = args[1].rstrip().replace("\"", "").split(",")

    print("str = %s" %str_prices)
    prices = array_str_to_int(str_prices)
    print("prices = %s" %prices)

    time0 = time.time()

    sl = Solution()
    print(sl.maxProfit(prices))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
