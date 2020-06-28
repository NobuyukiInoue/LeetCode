# coding: utf-8

import os
import sys
import time

class Solution:
    def largestPalindrome_cheat(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        if n == 2: return 987
        if n == 3: return 123 # 913 993
        if n == 4: return 597 # 9901 9999
        if n == 5: return 677 # 99681 99979
        if n == 6: return 1218 # 999001 999999
        if n == 7: return 877 # 9997647 9998017
        if n == 8: return 475 # 99990001 99999999

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 9
        if n==2:
            return 987
        for a in range(2, 9*10**(n-1)):
            hi=(10**n)-a
            lo=int(str(hi)[::-1])
            if a**2-4*lo < 0:
                continue
            if (a**2-4*lo)**.5 == int((a**2-4*lo)**.5):
                return (lo+10**n*(10**n-a))%1337

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
    var_str = temp.replace("[","").replace("]","").rstrip()
    n = int(var_str)

    sl = Solution()
    time0 = time.time()
    result = sl.largestPalindrome(n)

    print("result = {0}".format(result))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
