# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # 952ms
        wait = cur = 0.0
        for t, d in customers:
            cur = max(cur, t) + d
            wait += cur - t
        return wait / len(customers)

    def averageWaitingTime2(self, customers: List[List[int]]) -> float:
        # 936ms
        waitting_time = [0]*len(customers)
        latest_arrival_time = customers[0][0] + customers[0][1]
        waitting_time[0] = customers[0][1]
        waitting_total_time = waitting_time[0]
    #   print("latest_arrival_time = {1:d}, waitting_time[{0:d}] = {2:d}".format(0, latest_arrival_time, waitting_time[0]))
        for i in range(1, len(customers)):
            if latest_arrival_time - customers[i][0] > 0:
                latest_arrival_time = customers[i][1] + latest_arrival_time
            else:
                latest_arrival_time = customers[i][0] + customers[i][1]
            waitting_time[i] = latest_arrival_time - customers[i][0]
            waitting_total_time += waitting_time[i]
        #   print("latest_arrival_time = {1:d}, waitting_time[{0:d}] = {2:d}".format(i, latest_arrival_time, waitting_time[i]))
        return waitting_total_time/len(waitting_time)

    def averageWaitingTime_work(self, customers: List[List[int]]) -> float:
        # 936ms
        arrival_time, waitting_time = [0]*len(customers),  [0]*len(customers)
        arrival_time[0]  = customers[0][0] + customers[0][1]
        waitting_time[0] = customers[0][1]
    #   print("arrival_time[{0:d}] = {1:d}, waitting_time[{0:d}] = {2:d}".format(0, arrival_time[0], waitting_time[0]))

        for i in range(1, len(customers)):
            if arrival_time[i - 1] - customers[i][0] > 0:
            #   arrival_time[i] = (customers[i][0] + customers[i][1]) + (arrival_time[i - 1] - customers[i][0])
                arrival_time[i] = customers[i][1] + arrival_time[i - 1]
            else:
                arrival_time[i] = customers[i][0] + customers[i][1]
            waitting_time[i] = arrival_time[i] - customers[i][0]
        #   print("arrival_time[{0:d}] = {1:d}, waitting_time[{0:d}] = {2:d}".format(i, arrival_time[i], waitting_time[i]))

        return sum(waitting_time)/len(waitting_time)

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
    customers = [[int(n) for n in fld.split(",")] for fld in flds]
    print("customers = {0}".format(customers))

    sl = Solution()

    time0 = time.time()

    result = sl.averageWaitingTime(customers)

    time1 = time.time()

    print("result = {0:f}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
