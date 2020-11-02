# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    def canFormArray(self, arr, pieces):
        for piece in pieces:
            if piece[0] not in arr:
                return False
            idx = arr.index(piece[0])
            if arr[idx:idx + len(piece)] != piece:
                return False
        return True

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
    flds = temp.replace(" ","").replace("\"","").rstrip().split("],[[")
    arr = [int(col) for col in flds[0].replace("[[", "").split(",")]
    pieces = [[int(col) for col in data.split(",")] for data in flds[1].replace("]]]", "").split("],[")]
    print("arr = {0}".format(arr))
    print("pieces = {0}".format(pieces))
  
    sl = Solution()
    time0 = time.time()

    result = sl.canFormArray(arr, pieces)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
