# coding: utf-8

import bisect
import os
import sys
import time

class Solution:
#   def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    def insert(self, intervals, newInterval):
        # 92-104ms
        start = newInterval[0]
        end = newInterval[1]
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i][1]:
                if end < intervals[i][0]:
                    break
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            else:
                result.append(intervals[i])
            i += 1
        result.append([start, end])
        result += intervals[i:]
        return result

    def insert2(self, intervals, newInterval):
        # 96ms
        new, i = [], 0
        for i, it in enumerate(intervals):
            if newInterval[1] < it[0]:
                i -= 1
                break
            elif it[1] < newInterval[0]:
                new += it,
            else:
                newInterval[0], newInterval[1] = min(it[0], newInterval[0]), max(it[1], newInterval[1])
        return new + [newInterval] + intervals[i + 1:]

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
    flds = temp.replace("\"","").replace(" ","").replace("[[[","").rstrip().split("]],[")

    data0 = flds[0].split("],[")
    intervals = [[0 for j in range(len(data0[0].split(",")))] for i in range(len(data0))]
    newInterval = [int(val) for val in flds[1].replace("]]", "").split(",")]

    for i in range(len(data0)):
        line = data0[i].split(",")
        for j in range(len(line)):
            intervals[i][j] = int(line[j])
    print("intervals = {0}".format(intervals))
    print("newInterval = {0}".format(newInterval))

    sl = Solution()
    time0 = time.time()

    result = sl.insert(intervals, newInterval)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
