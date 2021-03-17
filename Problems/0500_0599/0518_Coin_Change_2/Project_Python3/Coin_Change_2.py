# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 132ms
        dp = [0]*(amount+1)
        dp[0] = 1
        for _, coin in enumerate(coins):
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]

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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    amount = int(flds[0])
    print("amount = {0:d}".format(amount))
    coins = [int(n) for n in flds[1].split(",")]
    print("coins = {0}".format(coins))

    sl = Solution()
    time0 = time.time()
    result = sl.change(amount, coins)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
