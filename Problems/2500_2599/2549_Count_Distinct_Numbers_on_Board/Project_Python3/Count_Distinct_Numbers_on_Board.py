# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def distinctIntegers(self, n: int) -> int:
        # 26ms - 33ms
        return max(n - 1, 1)

    def distinctIntegers_deque(self, n: int) -> int:
        # 38ms - 39ms
        que = collections.deque([])
        que.append(n)
        visited = set()
        visited.add(n)
        while que:
            n = que.popleft()
            for num in range(2, n):
                if num in visited:
                    continue
                if n % num == 1:
                    visited.add(num)
                    que.append(num)
        return len(visited)

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
    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()

    time0 = time.time()

    result = sl.distinctIntegers(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
