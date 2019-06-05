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

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    rowIndex = int(temp.replace("\"","").replace("[","").replace("]","").rstrip())

    time0 = time.time()

    sl = Solution()
    result = sl.getRow(rowIndex)

    time1 = time.time()
    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()

