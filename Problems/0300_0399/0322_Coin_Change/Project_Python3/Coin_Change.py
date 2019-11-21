# coding: utf-8

import os
import sys
import time

class Solution:
#   def coinChange(self, coins: List[int], amount: int) -> int:
    def coinChange(self, coins, amount):
        # 568ms
        sums = {0}
        remains = {amount}
        for number in range(amount//min(coins) +1):
            if len(sums.intersection(remains)):
                return number
            if len(sums) < len(remains):         
                sums = {s + c for s in sums for c in coins} 
            else:
                remains = {r - c for r in remains for c in coins}
        return -1

    def coinChange2(self, coins, amount):
        # 1392ms
        dp = [0]
        for i in range(1, amount+1):
            dp += [min([dp[i-x]+1 for x in coins if i-x>=0 and dp[i-x]>=0] or [-1])]
        return dp[-1]

    def coinChange3(self, coins, amount):
        # 1820ms
        if amount < 1:
            return 0
        return self.helper(coins, amount, [0 for i in range(amount)])

    def helper(self, coins, rem, count):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        if count[rem - 1] != 0:
            return count[rem - 1]
        min = sys.maxsize
        for coin in coins:
            res = self.helper(coins, rem - coin, count)
            if res >= 0 and res < min:
                min = 1 + res
        if min == sys.maxsize:
            count[rem - 1] = -1
        else:
            count[rem - 1] = min
        return count[rem - 1]

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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    coins = [int(n) for n in flds[0].split(",")]
    print("coins = {0}".format(coins))
    amount = int(flds[1])
    print("amount = {0:d}".format(amount))

    time0 = time.time()

    sl = Solution()
    result = sl.coinChange(coins, amount)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
