# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    def canCompleteCircuit(self, gas, cost):
        # 48ms
        start, count, cur, n = 0, 0, 0, len(gas)
        while count < n and start < 2 * n:
            cur += gas[start % n] - cost[start % n]
            if cur < 0:
                count = 0
                cur = 0
            else:
                count += 1
            start += 1
        if count < n:
            return  -1
        else:
            return start % n
    
    def canCompleteCircuit2(self, gas, cost):
        # 36ms
        n = len(gas)
        if n < 1: return -1
        dp = [0]*n
        dp[0] = gas[0] - cost[0]
        for i in range(1,n):
            dp[i] = dp[i-1] + gas[i] - cost[i]
        if dp[-1] >= 0:
            pos = dp.index(min(dp)) + 1
            if pos >= n:
                return 0
            else:
                return pos
        else:
            return -1

    def canCompleteCircuit_work(self, gas, cost):
        # 4660ms
        total, length = 0, len(gas)
        for start_pos in range(length):
            total = gas[start_pos]
            failed = False
            for count in range(length):
                locate = start_pos + count
                if locate >= length:
                    locate -= length
                total -= cost[locate]
                if total < 0:
                    failed = True
                    break
                locate += 1
                if locate >= length:
                    locate = 0
                total += gas[locate]
            if failed == False:
                return start_pos
        return -1

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    gas = [int(col) for col in flds[0].split(",")]
    cost = [int(col) for col in flds[1].split(",")]

    print("gas = {0}".format(gas))
    print("cost = {0}".format(cost))

    sl = Solution()
    time0 = time.time()

    result = sl.canCompleteCircuit(gas, cost)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
