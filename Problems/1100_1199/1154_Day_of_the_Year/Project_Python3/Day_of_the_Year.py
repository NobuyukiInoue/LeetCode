# coding: utf-8

import os
import sys
import time

class Solution:
#   def dayOfYear(self, date: str) -> int:
    def dayOfYear(self, date):
        # 32ms
        days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        flds = date.split("-")
        year, month, day = int(flds[0]), int(flds[1]), int(flds[2])
        if month <= 2:
            return days[month - 1] + day
        else:
            if not (year % 100 == 0 and year % 400 != 0) and year % 4 == 0:
                return days[month - 1] + day + 1
            else:
                return days[month - 1] + day

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
    date = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    print("date = {0}".format(date))
    sl = Solution()
    time0 = time.time()
    result = sl.dayOfYear(date)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
