import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # 41ms - 42ms
        ans = []
        def df(i: int, n: int, val: int) -> None: 
            if n == 0:
                ans.append(val)
                return
            if i - k >= 0:
                df(i - k, n - 1, val*10 + i - k)
            if k != 0 and i + k <= 9:
                df(i + k, n - 1, val*10 + i + k)
        for i in range(1, 10):
            df(i, n - 1, i)
        return ans

    def numsSameConsecDiff2(self, n: int, k: int) -> List[int]:
        # 42ms - 46ms
        ans = []
        d = collections.deque((1, d) for d in range(1, 10))
        while d:
            pos, num = d.pop()
            if pos == n:
                ans.append(num)
            else:
                for j in range(10):
                    if abs(num % 10 - j) == k:
                        d.append((pos + 1, num * 10 + j))
        return ans

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    n, k = int(flds[0]), int(flds[1])
    print("n = {0:d}, k = {1:d}".format(n, k))

    sl = Solution()
    time0 = time.time()

    result = sl.numsSameConsecDiff(n, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
