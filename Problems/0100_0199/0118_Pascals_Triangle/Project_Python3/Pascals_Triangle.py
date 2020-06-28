# coding: utf-8

import os
import sys
import time

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result

    def generate_old(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[]]*numRows
        for i in range(numRows):
            result[i] = [1]*(i + 1)
        #   result[i][0] = 1
        #   result[i][i] = 1
            for j in range(1, i):
                result[i][j] = result[i - 1][j] + result[i - 1][j - 1]
        return result


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
    numRows = int(temp.replace("\"","").replace("[","").replace("]","").rstrip())

    sl = Solution()
    time0 = time.time()
    result = sl.generate(numRows)
    print("result = {0}".format(result))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

