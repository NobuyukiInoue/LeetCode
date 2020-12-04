# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def maximumWealth(self, accounts: List[List[int]]) -> int:
    def maximumWealth(self, accounts: [[int]]) -> int:
        # 48ms
        ans = 0
        for account in accounts:
            temp = sum(account)
            if temp > ans:
                ans = temp
        return ans

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    accounts = [[]]*len(flds)
    for i, data in enumerate(accounts):
        accounts[i] = [int(n) for n in flds[i].split(",")]
    print("accounts = {0}".format(accounts))

    sl = Solution()

    time0 = time.time()

    result = sl.maximumWealth(accounts)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
