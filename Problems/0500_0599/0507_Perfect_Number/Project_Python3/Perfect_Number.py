# coding: utf-8

import os
import sys
import time
import numpy as np

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        # Find all the positive divisors
        div = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                div.append(i)
                div.append(num // i)
        div = set(div)
        return sum(div) - num == num

    def checkPerfectNumber_work(self, num):
        """
        :type num: int
        :rtype: bool
        """
        results = []
        n, sum = int(num / 2), 0
        while n > 0:
            if num % n == 0:
                results.append(n)
            n -= 1
        for temp in results:
            sum += temp
        if sum == num:
            return True
        else:
            return False

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
    num = int(temp.replace("[","").replace("]","").rstrip())

    sl = Solution()
    time0 = time.time()
    result = sl.checkPerfectNumber(num)
    print("result = {0}".format(result))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
