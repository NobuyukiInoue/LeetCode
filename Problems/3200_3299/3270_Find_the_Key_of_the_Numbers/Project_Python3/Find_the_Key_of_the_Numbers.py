import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # 32ms - 41ms
        ans, dv = 0, 10
        while dv < 100000:
            d1, d2, d3 = num1%dv, num2%dv, num3%dv
            ans += min(d1, d2, d3)
            num1 -= d1
            num2 -= d2
            num3 -= d3
            dv *= 10
        return ans

    def generateKey_2liner(self, num1: int, num2: int, num3: int) -> int:
        # 32ms - 36ms 
        vals = [str(x).zfill(4) for x in (num1, num2, num3)]
        return int("".join(map(min, zip(*vals))))

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
    
    num1, num2, num3 = int(flds[0]), int(flds[1]), int(flds[2])
    print("num1 = {0:d}, num2 = {1:d}, num3 = {2:d}".format(num1, num2, num3))

    sl = Solution()
    time0 = time.time()

    result = sl.generateKey(num1, num2, num3)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
