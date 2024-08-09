import math
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # 32ms - 39ms
        if red < blue:
            return self.maxHeightOfTriangle(blue, red)
        h1, h2 = math.isqrt(blue*4 + 1), math.isqrt(blue)*2
        if (h1+1)**2//4 <= red:
            return h1
        if ((h2+1)**2-1)//4 <= red:
            return h2
        if (h1-1)**2//4 <= red:
            return h1 - 1
        return h2 - 1

    def maxHeightOfTriangle2(self, red: int, blue: int) -> int:
        # 24ms - 36ms
        ans = 0
        b1, b2, r1, r2 = 0, 0, 0, 0
        for i in range(1, 10**10):
            if i%2 == 0:
                b1 += i
                r2 += i
            else:
                b2 += i
                r1 += i
            if (blue >= b1 and red >= r1) or (blue >= b2  and red >= r2):
                ans = i
            else:
                return ans

    def maxHeightOfTriangle3(self, red: int, blue: int) -> int:
        # 39ms - 40ms
        x, c, t, r, b = 0, 1, 0, red, blue
        while r + b >= c:
            if c % 2 == 0:
                if b >= c:
                    b -= c
                    c += 1
                    t += 1
                else:
                    break
            else:
                if r >= c:
                    r -= c
                    c += 1
                    t += 1
                else:
                    break
        x, c, r, b, t = max(x, t), 1, red, blue, 0
        while r + b >= c:
            if c % 2 == 0:
                if r >= c:
                    r -= c
                    c += 1
                    t += 1
                else:
                    break
            else:
                if b >= c:
                    b -= c
                    c += 1
                    t += 1
                else:
                    break
        x = max(x, t)
        return x

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
    
    red, blue = int(flds[0]), int(flds[1])
    print("red = {0:d}, blue = {1:d}".format(red, blue))

    sl = Solution()
    time0 = time.time()

    result = sl.maxHeightOfTriangle(red, blue)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
