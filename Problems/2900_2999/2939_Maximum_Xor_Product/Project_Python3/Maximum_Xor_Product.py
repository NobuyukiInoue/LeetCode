import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        # 30ms - 37ms
        for i in range(n):
            x = 1 << i
            t1, t2 = a^x, b^x
            if t1*t2 > a*b:
                a, b = t1, t2
        MOD = 10**9 + 7
        return (a*b)%MOD

    def maximumXorProduct_bad(self, a: int, b: int, n: int) -> int:
        m = pow(2, n) - 1
        r_a, r_b = m - a, m - b
        x = r_a & r_b
        return (a^x)*(b^x)

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    a, b, n = int(flds[0]), int(flds[1]), int(flds[2])
    print("a = {0:d}, b = {1:d}, n = {2:d}".format(a, b, n))

    sl = Solution()
    time0 = time.time()

    result = sl.maximumXorProduct(a, b, n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
