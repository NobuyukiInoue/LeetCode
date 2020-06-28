# coding: utf-8

import os
import sys
import time

class Solution:
#   def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    def distanceBetweenBusStops(self, distance, start, destination):
        # 52ms
        return min(sum(distance[min(start, destination):max(start, destination)]), sum(distance[:min(start, destination)] + distance[max(start, destination):]))

    def distanceBetweenBusStops2(self, distance, start, destination):
        # 52ms
        if destination == start:
            return 0
        if start < destination:
            r = sum(distance[start:destination])
            l = sum(distance[destination:]) + sum(distance[:start])
        else:
            r = sum(distance[destination:start])
            l = sum(distance[start:]) + sum(distance[:destination])
        if r < l:
            return r
        else:
            return l

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

    distance = [int(n) for n in flds[0].split(",")]
    flds2 = flds[1].split(",")
    start, destination = int(flds2[0]), int(flds2[1])

    print("distance = {0}, start = {1:d}, destination = {2:d}".format(distance, start, destination))

    sl = Solution()
    time0 = time.time()
    result = sl.distanceBetweenBusStops(distance, start, destination)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
