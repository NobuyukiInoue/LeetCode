# coding: utf-8

import os
import sys
import time

class Solution:
#   def getRow(self, rowIndex: int) -> List[int]:
    def getRow(self, rowIndex):
        result = [[1]*(i+1) for i in range(0, rowIndex + 1)]
        for i in range(0, rowIndex + 1):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result[i]

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
    rowIndex = int(temp.replace("\"","").replace("[","").replace("]","").rstrip())

    sl = Solution()
    time0 = time.time()
    result = sl.getRow(rowIndex)

    time1 = time.time()
    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

