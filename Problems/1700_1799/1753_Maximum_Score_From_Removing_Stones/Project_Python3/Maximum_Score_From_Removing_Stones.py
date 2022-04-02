# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # 32ms - 43ms
        return min((a + b + c) // 2, a + b + c - max(a, b, c))

    def maximumScore2(self, a: int, b: int, c: int) -> int:
        # 288ms - 418ms
        ans = 0
        while not (a == b == 0 or a == c == 0 or b == c == 0):
            if a >= b and a >= c:
                if b >= c:
                    pass
                else:
                    b, c = c, b
            elif b >= a and b >= c:
                if a >= c:
                    a, b, c = b, a, c
                else:
                    a, b, c = b, c, a
            elif c >= a and c >= b:
                if a >= b:
                    a, b, c = c, a, b
                else:
                    a, b, c = c, b, a
            if b == c:
                ans += 1
                b -= 1
                a -= 1
            else:
                ans += b - c
                a-= b - c
                b-= b - c
        return ans

    def maximumScore3(self, a: int, b: int, c: int) -> int:
        # 648ms - 1235ms
        ans = 0
        while True:
            v_min = min(min(a, b), c)
            if v_min == c:
                a -= 1
                b -= 1
            elif v_min == b:
                a -= 1
                c -= 1
            else:
                b -= 1
                c -= 1
            ans += 1
            if a + b == 0 or b + c == 0 or c + a == 0:
                break
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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    a, b, c = nums[0], nums[1], nums[2]
    print("a = {0:d}, b = {1:d}, c = {2:d}".format(a, b, c))

    sl = Solution()

    time0 = time.time()

    result = sl.maximumScore(a, b, c)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
