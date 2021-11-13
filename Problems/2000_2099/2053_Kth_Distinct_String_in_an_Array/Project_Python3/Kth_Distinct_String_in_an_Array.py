# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # 68ms
        counts = collections.Counter(arr)
        arr_count1 = [s for s in arr if counts[s] == 1]
        return k <= len(arr_count1) and arr_count1[k - 1] or ''

    def kthDistinct2(self, arr: List[str], k: int) -> str:
        # 336ms
        arr_count1 = [i for i in arr if arr.count(i) == 1]
        return "" if k > len(arr_count1) else arr_count1[k - 1]

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
    flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").rstrip().split("],[")

    arr = flds[0].split(",")
    k = int(flds[1])
    print("arr = {0}, k = {1:d}".format(arr, k))

    sl = Solution()
    time0 = time.time()

    result = sl.kthDistinct(arr, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
