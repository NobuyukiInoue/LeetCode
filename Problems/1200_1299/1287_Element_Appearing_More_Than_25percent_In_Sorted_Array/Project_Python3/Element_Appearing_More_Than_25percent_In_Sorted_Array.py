# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def findSpecialInteger(self, arr: List[int]) -> int:
    def findSpecialInteger(self, arr):
        # 96ms
        return collections.Counter(arr).most_common(1)[0][0]

    def findSpecialInteger2(self, arr):
        # 92ms
        dict1 = collections.Counter(arr)
        for each in dict1:
            if dict1[each] > float(len(arr))/4:
                return each

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

    arr = [int(n) for n in flds.split(",")]
    print("arr = {0}".format(arr))

    sl = Solution()
    time0 = time.time()
    result = sl.findSpecialInteger(arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
