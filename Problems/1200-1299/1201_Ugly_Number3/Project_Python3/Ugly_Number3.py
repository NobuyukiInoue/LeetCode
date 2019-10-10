# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
    def nthUglyNumber(self, n, a, b, c):
        # 32ms
        [a, b, c] = sorted([a, b, c])
        if a == 1:
            return n

        def lcm(x,y):
            return x*y//math.gcd(x, y)

        AB, BC, AC, ABC, r, s = lcm(a, b), lcm(b, c), lcm(a, c), lcm(lcm(a, b), c), n*a//3, n*a + 1

        def unc(x):
            return x//a + x//b + x//c - x//AB - x//BC - x//AC + x//ABC

        while unc(s - 1) - n > 0:
            m = (r + s)//2
            if unc(m) - n > 0:
                s = m
            else:
                r = m
        return max(i*((s - 1)//i) for i in [a, b, c])

    def nthUglyNumber2(self, n, a, b, c):
        # 52ms
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)
        def count(val,a,b,c):
            return val//a + val//b + val//c -val//lcm(a, b)-val//lcm(a, c)-val//lcm(c, b) + val//lcm(lcm(a, b),c)
        l = 1
        r = min([a,b,c]) * n
        tmp = (l+r)//2
        while count(tmp,a,b,c) != n-1:
            if count(tmp,a,b,c) > n-1:
                r = tmp
            else:
                l = tmp
            tmp = (l+r)//2
        while count(tmp,a,b,c) != n:
            tmp += 1
        return tmp

    def nthUglyNumber_work(self, n, a, b, c):
        # Time Limit Exceeded
        x = 0
        ia, ib, ic = 1, 1, 1
        res, res_a, res_b, res_c = 0, a*ia, b*ib, c*ic

        while x < n:
            if res_a < res_b and res_a < res_c:
                if res_a != res:
                    x += 1
                    res = res_a
                ia += 1
                res_a = a*ia
            elif res_b < res_a and res_b < res_c:
                if res_b != res:
                    x += 1
                    res = res_b
                ib += 1
                res_b = b*ib
            else:
                if res_c != res:
                    x += 1
                    res = res_c
                ic += 1
                res_c = b*ic
        return res

    def nthUglyNumber_bad(self, n, a, b, c):
        results = [0]*(n*3)
        x = 0
        for i in range(1, n + 1):
            results[x] = a*i
            x += 1
        for i in range(1, n + 1):
            results[x] = b*i
            x +=1
        for i in range(1, n + 1):
            results[x] = c*i
            x +=1
        s_results = list(set(results))
        return s_results[n - 1]
 
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

    if len(flds) != 4:
        return
    n = int(flds[0])
    a = int(flds[1])
    b = int(flds[2])
    c = int(flds[3])
    print("n = {0:d}, a = {1:d}, b = {2:d}, c = {3:d}".format(n, a, b, c))

    time0 = time.time()

    sl = Solution()
    result = sl.nthUglyNumber(n, a, b, c)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
