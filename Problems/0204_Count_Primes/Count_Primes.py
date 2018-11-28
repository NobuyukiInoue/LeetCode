# coding: utf-8

import os
import sys
import time
import math

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        if n == 3:
            return 1

        prime_flag = [True]*n

        count = 1
        for i in range(2, n, 2):
                prime_flag[i] = False

        for i in range(3, n, 2):
            if prime_flag[i] == True:
                prime_flag[i] = False
                count += 1
                for j in range(i + i, n, i):
                    if prime_flag[j] == True:
                        prime_flag[j] = False
        return count


    def countPrimes_old(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        if n == 3:
            return 1
        count = 1
        for i in range(3, n, 2):
            k = 0
            for j in range(3, int(math.sqrt(i)) + 1, 2):
                if i % j == 0:
                    k = 1
                    break
            if k == 0:
                count += 1
        return count

    def countPrimes_work(self, n):
        """
        :type n: int
        :rtype: int
        """
        return calc_prime_number(n)


def calc_prime_number(n):
    count, resultStr = 1, "2"
    for i in range(3, n + 1, 2):
        k = 0
        for j in range(3, int(math.sqrt(i)) + 1, 2):
            if i % j == 0:
                k = 1
                break
        if k == 0:
            resultStr += " " + str(i)
            count += 1
    print("%s" %resultStr)
    return count


def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        print("argv[1] = %s" %temp)
        loop_main(temp)


def loop_main(temp):
    n = int(temp)

    time0 = time.time()

    sl = Solution()
    result = sl.countPrimes(n)
    print("result = %d" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
