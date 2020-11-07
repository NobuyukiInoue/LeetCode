# coding: utf-8

import json
import os
import sys
import time

class Solution:
#   def getWinner(self, arr: List[int], k: int) -> int:
    def getWinner(self, arr: [int], k: int) -> int:
        # 596ms
        cur = arr[0]
        win = 0
        for i in range(1, len(arr)):
            if arr[i] > cur:
                cur = arr[i]
                win = 0
            win += 1
            if (win == k):
                break
        return cur

    def getWinner3(self, arr: [int], k: int) -> int:
        # Time Limit Exceeded.
        count = 0
        while count < k:
            if arr[0] < arr[1]:
                arr = arr[1:] + [arr[0]]
            else:
                arr =  [arr[0]] + arr[2:] + [arr[1]]
                count += 1
        return arr[0]

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

    result = sl.getWinner(arr, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
