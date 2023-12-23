import heapq
import math
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 634ms - 636ms
        heap = []
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [(x,y) for (dist,x, y) in heap]

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 660ms - 694ms
        distances = []
        for i, (x, y) in enumerate(points):
            distances.append([math.sqrt(x*x + y*y), i])
        distances.sort()
        ans = []
        for dist in distances:
            if k == 0:
                break
            ans.append(points[dist[1]])
            k -= 1
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
    flds = temp.replace(" ","").replace("\"","").replace("[[[","").replace("]]]","").rstrip().split("]],[")

    points = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
    k = int(flds[1].replace("]]", ""))
    print("points = {0}, k = {1:d}".format(points, k))

    sl = Solution()
    time0 = time.time()

    result = sl.kClosest(points, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
