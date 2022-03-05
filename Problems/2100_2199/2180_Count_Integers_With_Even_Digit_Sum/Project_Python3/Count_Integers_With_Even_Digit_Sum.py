import collections
from operator import truediv
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countEven(self, num: int) -> int:
        # 43ms
        total, k = 0, num
        num -= num%10
        while num:
            total += num%10
            num //= 10
        if total%2 == 0:
            return k//2
        if total%2 != 0:
            return (k + 1)//2 - 1

    def countEven2(self, num: int) -> int:
        # 50ms
        def evenDigitSum(n: int) -> bool:
            total = 0
            while n > 0:
                total += n%10
                n //= 10
            if total%2 == 0:
                return True
            return False
        ans = 0
        for i in range(2, num + 1):
            if evenDigitSum(i):
                ans += 1
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
    flds = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    num = int(flds)
    print("num = {0:d}".format(num))

    sl = Solution()
    time0 = time.time()

    result = sl.countEven(num)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
