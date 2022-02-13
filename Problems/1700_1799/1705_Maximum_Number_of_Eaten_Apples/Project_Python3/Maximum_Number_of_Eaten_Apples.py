# coding: utf-8

import heapq
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # 616ms
        lastday = len(apples)
        day, res = 0, 0
        apple_heap = []
        heapq.heapify(apple_heap)

        while day < lastday:
            if apples[day] > 0:
                heapq.heappush(apple_heap, [day + days[day], apples[day]])
            if apple_heap and apple_heap[0][0] > day:
                res += 1
                apple_heap[0][1] -= 1
                if apple_heap[0][1] == 0:
                    heapq.heappop(apple_heap)
            day += 1
            while apple_heap and apple_heap[0][0] <= day:
                heapq.heappop(apple_heap)

        while apple_heap:
            [expire, counts] = heapq.heappop(apple_heap)
            if day < expire:
                jump_to = min(expire, day + counts)
                res += jump_to - day
                day = jump_to

        return res

    def eatenApples2(self, apples: List[int], days: List[int]) -> int:
        # 965ms
        res, i = 0, 0
        apple_heap = []
        while i < len(apples) or apple_heap:
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(apple_heap, [i + days[i], apples[i]])
            while apple_heap and (apple_heap[0][0] <= i or apple_heap[0][1] == 0):
                heapq.heappop(apple_heap)
            if apple_heap:
                apple_heap[0][1] -= 1
                res += 1
            i += 1
        return res

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    apples = [int(col) for col in flds[0].split(",")] 
    days = [int(col) for col in flds[1].split(",")] 
    print("apples = {0}, days = {1}".format(apples, days))

    sl = Solution()
    time0 = time.time()

    result = sl.eatenApples(apples, days)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
