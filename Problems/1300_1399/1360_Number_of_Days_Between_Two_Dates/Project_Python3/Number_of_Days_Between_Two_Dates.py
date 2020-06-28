# coding: utf-8

import datetime
import os
import sys
import time

class Solution:
#   def daysBetweenDates(self, date1: str, date2: str) -> int:
    def daysBetweenDates2(self, date1, date2):
        # 28ms
        return abs((datetime.datetime.strptime(date1, '%Y-%m-%d') - datetime.datetime.strptime(date2, '%Y-%m-%d')).days)

    def daysBetweenDates(self, date1, date2):
        # 28ms
        def f(date):
            y, m, d = map(int, date.split('-'))
            if m < 3:
                m += 12
                y -= 1
            return 365 * y + y // 4 + y // 400 - y // 100 + d + (153 * m + 8) // 5
        
        return abs(f(date1) - f(date2))

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").replace("\"","").replace(" ","").rstrip().split(",")

    date1, date2 = flds[0], flds[1]
    print("date1 = {0}, date2 = {1}".format(date1, date2))

    sl = Solution()
    time0 = time.time()

    result = sl.daysBetweenDates(date1, date2)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
