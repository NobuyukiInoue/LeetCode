# coding: utf-8

import os
import sys
import time

class Solution:
#   def myPow(self, x: float, n: int) -> float:
    def myPow(self, x, n):
        # 28 - 48ms
        count, res = 0, 1
        d = []
        while count < abs(n):
            if not d:
                res *= x
                count += 1
                d.append([1, res])
            else:
                i = len(d) - 1
                while d[i][0] > abs(n) - count:
                    i -= 1
                count += d[i][0]
                res *= d[i][1]
                if count > d[-1][0]:
                    d.append([count, res])
        if n < 0:
            res = 1 / res
        return res
 
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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    x = float(flds[0])
    n = int(flds[1])
    print("x = {0:f}, n = {1:d}".format(x, n))

    time0 = time.time()

    sl = Solution()
    result = sl.myPow(x, n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
