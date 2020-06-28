# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def arrayRankTransform(self, arr: List[int]) -> List[int]:
    def arrayRankTransform(self, arr):
        # 392ms
        new = sorted(arr)
        d = {}
        count = 1
        for num in new:
            if num not in d:
                d[num] = count
                count += 1
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
        return arr


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

    if len(flds) > 0:
        arr = [int(n) for n in flds.split(",")]
    else:
        arr = [None]

    print("arr = {0}".format(arr))

    sl = Solution()
    time0 = time.time()
    result = sl.arrayRankTransform(arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
