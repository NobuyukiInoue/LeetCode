# coding: utf-8

import functools
import operator
import os
import sys
import time

class Solution:
#   def subtractProductAndSum(self, n: int) -> int:
    def subtractProductAndSum(self, n):
        # 24ms
        res_add, res_prod = 0, 1
        for val in str(n):
            res_add += int(val)
            res_prod *= int(val)
        return res_prod - res_add

    def subtractProductAndSum2(self, n):
        # 24ms
        sum, prod = 0, 1
        while n:
            digit = n % 10
            sum += digit
            prod *= digit
            n //= 10
        return prod - sum

    def subtractProductAndSum3(self, n):
        A = map(int, str(n))
        return functools.reduce(operator.mul, A) - sum(A)

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
    fld = temp.replace("[","").replace("]","").replace("\"","").replace(" ","")
    n = int(fld)
    
    print("n = {0:d}".format(n))

    time0 = time.time()

    sl = Solution()
    result = sl.subtractProductAndSum(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
