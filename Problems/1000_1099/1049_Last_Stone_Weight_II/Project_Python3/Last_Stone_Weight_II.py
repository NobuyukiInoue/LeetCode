import functools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 43ms - 48ms
        total = sum(stones)
        dp = [False for _ in range(total//2 + 1)]
        dp[0] = True
        for i, stone in enumerate(stones):
            for j in range(total//2, stone - 1, -1):
                if dp[j - stone]:
                    dp[j] = True
        i = total//2
        while i >= 0 and dp[i] is False:
            i -= 1
        return total - 2*i

    def lastStoneWeightII_1liner(self, stones: List[int]) -> int:
        # 46ms
        return min(functools.reduce(lambda dp, y: {x + y for x in dp} | {abs(x - y) for x in dp}, stones, {0}))

    def lastStoneWeightII2(self, stones: List[int]) -> int:
        # 56ms
        if len(stones) == 1:
            return stones[0]
        s = set()
        s.add(stones[0])
        s.add(-stones[0])
        dp = set()
        for i in range(1, len(stones)):
            for j in s:
                dp.add(abs(j - stones[i]))
                dp.add(abs(j + stones[i]))
            s = dp
            dp = set()
        return min(s)

    def lastStoneWeightII_bad(self, stones: List[int]) -> int:
        # Time Limit Exceeded. 3/90
        def df(stones, min_val):
            if len(stones) == 1:
                return min(stones[0], min_val)
            elif len(stones) == 0:
                return min_val
            for i in range(len(stones) - 1):
                for j in range(i + 1, len(stones)):
                    t_stones = stones.copy()
                    if t_stones[i] > t_stones[j]:
                        t_stones[i] = t_stones[i] - t_stones[j]
                        t_stones.pop(j)
                    elif stones[j] > stones[i]:
                        t_stones[j] = t_stones[j] - t_stones[i]
                        t_stones.pop(i)
                    else:
                        if i > j:
                            t_stones.pop(i)
                            t_stones.pop(j)
                        else:
                            t_stones.pop(j)
                            t_stones.pop(i)
                    min_val = df(t_stones, min_val)
            return min_val
        return df(stones, sys.maxsize)

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    stones = [int(n) for n in flds.split(",")]
    print("stones = {0}".format(stones))

    sl = Solution()

    time0 = time.time()

    result = sl.lastStoneWeightII(stones)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
