# coding: utf-8

import bisect
import os
import sys
import time
import heapq

class Solution:
#   def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    def getSkyline(self, buildings):
        # 128ms
        buildings.sort(key = lambda x:x[2])
        axis = [float('-inf'),float('inf')]
        heights = [0, 0]
        for l, r, h in buildings:
            idl = bisect.bisect_left(axis, l)
            idr = bisect.bisect_right(axis, r)
            if h != heights[idl - 1]:
                axis[idl :idr] = [l, r]
                heights[idl :idr] = [h, heights[idr - 1]]
            elif idr > idl:
                axis[idl :idr] = [r]
                heights[idl :idr] = [heights[idr - 1]]
        return [[axis[i],heights[i]] for i in range(1,len(axis) - 1)]

    def getSkyline2(self, buildings):
        # 148ms
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]

    def getSkyline_timeover(self, buildings):
        heights = [0]*10001
        max_x = 0
        for i in range(len(buildings)):
            if buildings[i][1] > max_x:
                max_x = buildings[i][1]
            for pos in range(buildings[i][0], buildings[i][1]):
                if buildings[i][2] > heights[pos]:
                    heights[pos] = buildings[i][2]
        pre_height = 0
        results = [[]]*0
        for x in range(0, max_x + 1):
            print("height[{0:d}] = {1:d}".format(x, heights[x]))
            if heights[x] != pre_height:
                results.append([x, heights[x]])
                pre_height = heights[x]
        return results

    def getSkyline_work(self, buildings):
        heights = {}
        for i in range(len(buildings)):
            for pos in (buildings[i][0], buildings[i][1]):
                if not pos in heights:
                    heights[pos] = buildings[i][2]
                elif buildings[i][2] > heights[pos]:
                    heights[pos] = buildings[i][2]

        sorted_heights = sorted(heights.items(), key = lambda x:x[0])

        pre_height = 0
        results = [[]]*0
        for i in range(len(sorted_heights)):
            print("sorted_heights[{0:d}] = {1:d}".format(sorted_heights[i][0], sorted_heights[i][1]))
            if sorted_heights[i][1] > pre_height:
                pre_height = sorted_heights[i][1]
            """
            if i < len(sorted_heights) - 1:
                if sorted_heights[i][0] != pre_height and sorted_heights[i][1] < sorted_heights[i + 1][1]:
                    sorted_heights[i + 1] = (sorted_heights[i + 1][1], sorted_heights[i][1])
                    continue
            """
            results.append([sorted_heights[i][0], sorted_heights[i][1]])
            pre_height = sorted_heights[i][1]
        return results

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

    buildings = [[int(n) for n in fld.split(",")] for fld in flds]
    print("buildings = {0}".format(buildings))

    sl = Solution()
    time0 = time.time()
    result = sl.getSkyline(buildings)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
