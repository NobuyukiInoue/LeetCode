# coding: utf-8

import os
import sys
import time

class Solution:
#   def nthUglyNumber(self, n: int) -> int:
    def nthUglyNumber(self, n):
        # 116ms
        ugly = [1] * n
        i2 = i3 = i5 = -1
        x = v2 = v3 = v5 = 1
        for k in range(n):
            x = min(v2, v3, v5)
            ugly[k] = x
            if x == v2:
                i2 += 1
                v2 = ugly[i2] * 2
            if x == v3:
                i3 += 1
                v3 = ugly[i3] * 3
            if x == v5:
                i5 += 1
                v5 = ugly[i5] * 5
        return x

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    fld = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(fld)

    time0 = time.time()

    sl = Solution()
    result = sl.nthUglyNumber(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
