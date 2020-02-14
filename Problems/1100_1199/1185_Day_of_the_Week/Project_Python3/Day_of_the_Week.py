# coding: utf-8

import calendar
import datetime
from datetime import date
import os
import sys
import time

class Solution:
#   def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    def dayOfTheWeek(self, day, month, year):
        # 24-36ms
       	return date(year, month, day).strftime("%A")

    def dayOfTheWeek2(self, day, month, year):
        # 40ms
        return calendar.day_name[datetime.date(year, month, day).weekday()]

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

    if len(flds) != 3:
        print("Not 3 argument...")
        return

    day = int(flds[0])
    month = int(flds[1])
    year = int(flds[2])
    print("day = {0:d}, month = {1:d}, year = {2:d}".format(day, month, year))

    time0 = time.time()

    sl = Solution()
    result = sl.dayOfTheWeek(day, month, year)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
