# coding: utf-8

import os
import sys
import time

class Solution:
#   def uniquePaths(self, m: int, n: int) -> int:
    def uniquePaths2(self, m, n):
        # 28ms
        count = [[1 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                count[i][j] = count[i - 1][j] + count[i][j - 1]

        return count[m - 1][n - 1]

    def uniquePaths(self, m: int, n: int) -> int:
        # 24ms
        def Helper(m):
            temp = 1
            while m > 1:
                temp = temp*m
                m -= 1
            return temp

        return int(Helper(m + n - 2)/(Helper(m - 1)*Helper(n - 1)))
    


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    m, n = int(flds[0]), int(flds[1])
    print("m = {0:d}, n = {1:d}".format(m, n))

    time0 = time.time()

    sl = Solution()
    result = sl.uniquePaths(m, n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
