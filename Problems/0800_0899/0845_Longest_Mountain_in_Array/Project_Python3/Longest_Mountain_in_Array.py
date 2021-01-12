# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # 164ms
        if len(arr) < 3:
            return 0
        largest_mountain = 0       
        start = end = 0
        N = len(arr)
        while end < N:
            start = end
            if end + 1 < N and arr[end] < arr[end + 1]:
                while end + 1 < N and arr[end] < arr[end + 1]:
                    end += 1
                if end + 1 < N and arr[end] > arr[end + 1]:
                    while end + 1 < N and arr[end] > arr[end + 1]:
                        end += 1   
                    largest_mountain = max(largest_mountain, end - start + 1)
            if end == start:
                end += 1
        return largest_mountain

    def longestMountain2(self, arr: List[int]) -> int:
        # 212ms
        up, down = [0]*len(arr), [0]*len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up[i] = up[i - 1] + 1
        for i in range(len(arr) - 1)[::-1]:
            if arr[i] > arr[i + 1]:
                down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    arr   = [int(n) for n in flds.split(",")]
    print("arr   = {0}".format(arr))

    sl = Solution()

    time0 = time.time()

    result = sl.longestMountain(arr)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
