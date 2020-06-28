# coding: utf-8

import os
import sys
import time

class Solution:
#    def hasAlternatingBits(self, n: int) -> bool:
    def hasAlternatingBits(self, n):
        return '00' not in bin(n) and '11' not in bin(n)

    def hasAlternatingBits2(self, n):
        return all((int(k) for k in bin(((n<<1) ^ n)>>1)[2:]))

    def hasAlternatingBits_work(self, n):
        mod_pre = n % 2
        n //= 2
        while n > 0:
            mod_cur = n % 2
            if mod_cur == mod_pre:
                return False
            n //= 2
            mod_pre = mod_cur
        return True

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
    flds = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()

    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.hasAlternatingBits(n)

    time1 = time.time()
    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
