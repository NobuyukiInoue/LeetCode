# coding: utf-8

import json
import os
import sys
import time

class Solution:
#   def findKthPositive(self, arr: List[int], k: int) -> int:
    def findKthPositive(self, arr, k):
        # 44ms
        count, index = 0, 0
        for i in range(1, arr[-1]):
            if i < arr[index]:
                count += 1
                if count == k:
                    return i
            else:
                index += 1
        return arr[-1] + k - count

    def findKthPositive2(self, arr, k):
        # 48ms
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k

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
    arr, k = [int(n) for n in flds[0].split(",")], int(flds[1])
    print("arr = {0}, k = {1}".format(arr, k))

    sl = Solution()
    time0 = time.time()

    result = sl.findKthPositive(arr, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
