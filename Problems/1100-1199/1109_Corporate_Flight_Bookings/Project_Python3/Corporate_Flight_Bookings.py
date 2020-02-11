# coding: utf-8

import os
import sys
import time

import collections

class Solution:
#   def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    def corpFlightBookings(self, bookings, n):
        # 888ms
        res = [0] * (n + 1)
        for i, j, k in bookings:
            res[i - 1] += k
            res[j] -= k
        for i in range(1, n):
            res[i] += res[i - 1]
        return res[:-1]

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
    flds = temp.replace("\"","").replace("[[[","").rstrip().split("]],[")

    bookings_str = flds[0].split("],[")
    bookings = [[int(col) for col in data.split(",")] for data in bookings_str]
    print("bookings = {0}".format(bookings))
    n = int(flds[1].replace("]]",""))
    print("n = {0:d}".format(n))

    time0 = time.time()

    sl = Solution()
    result = sl.corpFlightBookings(bookings, n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
