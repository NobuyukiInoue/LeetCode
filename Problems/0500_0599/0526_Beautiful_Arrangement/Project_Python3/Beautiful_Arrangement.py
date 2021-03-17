# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def countArrangement(self, n: int) -> int:
        # 140ms
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i - 1, X - {x})
                       for x in X
                           if x % i == 0 or i % x == 0)
        return count(n, set(range(1, n + 1)))

    def countArrangement2(self, n: int) -> int:
        # 248ms
        cache = { frozenset(): 1 }
        count = lambda x: cache.setdefault(x, sum(count(x - {m}) for m in x if not all((m % len(x), len(x) % m))))
        return count(frozenset(range(1, n + 1)))

    def countArrangement3(self, n: int) -> int:
        # 548ms
        memo = [0]*((1 << n) - 1)
        def dfs(memo: List[int], n: int, pos: int, used: int) -> int:
            if bin(used).count("1") == n:
                return 1
            if memo[used] > 0:
                return memo[used]
            res = 0
            for i in range(1, n + 1):
                if i % pos != 0 and pos % i != 0:
                    continue
                mask = 1 << (i - 1)
                if used & mask == 0:
                    res += dfs(memo, n, pos + 1, used | mask)
            memo[used] = res
            return res
        return dfs(memo, n, 1, 0)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()

    time0 = time.time()

    result = sl.countArrangement(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
