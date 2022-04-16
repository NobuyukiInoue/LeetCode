# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 304ms - 477ms
        left, right = 0, len(arr) - 1
        while right - left + 1 != k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
        return arr[left:right + 1]

    def findClosestElements_1liner(self, arr: List[int], k: int, x: int) -> List[int]:
        # 358ms - 643ms
        return sorted([p[1] for p in sorted([(abs(num - x), num) for num in arr])[0:k]])


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

    arr = [int(n) for n in flds[0].split(",")]
    k, x = int(flds[1]), int(flds[2])

    print("arr = {0}, k = {1:d}, x = {2:d}".format(arr, k, x))

    sl = Solution()
    time0 = time.time()

    result = sl.findClosestElements(arr, k, x)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
