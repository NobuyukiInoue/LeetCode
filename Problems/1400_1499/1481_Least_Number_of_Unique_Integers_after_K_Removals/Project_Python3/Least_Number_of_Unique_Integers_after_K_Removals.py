import collections
import heapq
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # 338ms - 381ms
        values = sorted(collections.Counter(arr).values())
        removed_cnts = 0
        for v in values:
            if k - v >= 0:
                k -= v
                removed_cnts += 1
        return len(values) - removed_cnts

    def findLeastNumOfUniqueInts2(self, arr: List[int], k: int) -> int:
        # 356ms - 387ms
        values = sorted(collections.Counter(arr).values())
        removed_cnts = 0
        for v in values:
            if k - v < 0:
                break
            k -= v
            removed_cnts += 1
        return len(values) - removed_cnts

    def findLeastNumOfUniqueInts3(self, arr: List[int], k: int) -> int:
        # 367ms - 369ms
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        unique_elements = len(d)
        curr_deleted = 0
        count = 0
        for frequency in sorted(d.values()):
            curr_deleted += frequency
            count += 1
            if curr_deleted < k:
                continue
            elif curr_deleted == k:
                return unique_elements-count
            else:
                return unique_elements-(count-1)

    def findLeastNumOfUniqueInts4(self, arr: List[int], k: int) -> int:
        # 369ms - 381m
        hp = list(collections.Counter(arr).values())
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)
        return len(hp) + (k < 0)

    def findLeastNumOfUniqueInts5(self, arr: List[int], k: int) -> int:
        # 515ms - 526ms
        cnts = collections.Counter(arr)
        s = sorted(arr, key = lambda x:(cnts[x],x))
        return len(set(s[k:]))

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    arr = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("arr = {0}, k = {1:d}".format(arr, k))

    sl = Solution()
    time0 = time.time()

    result = sl.findLeastNumOfUniqueInts(arr, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
