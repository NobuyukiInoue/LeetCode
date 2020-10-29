# coding: utf-8

import os
import sys
import time
import math

class Solution:
    def integerReplacement(self, n: int) -> int:
        # 28ms
        ans = 0
        while n != 1:
            if n & 1 == 0:
                n = n >> 1
            elif n == 3 or ((n + 1) & n) > ((n - 1) & (n - 2)):
                n -= 1
            else:
                n += 1
            ans += 1
        return ans

    def integerReplacement2(self, n: int, counter=0) -> int:
        # 284ms
        if n == 1: return counter
        if not n%2: return self.integerReplacement(n/2, counter+1)
        else: return min(self.integerReplacement(n+1, counter+1), self.integerReplacement(n-1, counter+1))

    def integerReplacement3(self, n: int) -> int:
        # 256ms
        def rec(n):
            if n&(n-1) == 0:
                return int(log2(n))
            return rec(int(n/2))+1 if n%2==0 else min(rec(n-1), rec(n+1))+1
        
        return rec(n)

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
    n_str = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    n = int(n_str)
    print("n = {0:d}".format(n))

    sl = Solution()

    time0 = time.time()

    result = sl.integerReplacement(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
