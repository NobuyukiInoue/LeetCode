# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
    def matrixBlockSum(self, mat: [[int]], K: int) -> [[int]]:
        # 96ms
        r, c = len(mat), len(mat[0])
        temp = [[0]*c for i in range(r)]
        answer = [[0]*c for i in range(r)]

        for i in range(r):
            res = 0
            for delta_c in range(K + 1):
                if delta_c < c:
                    res += mat[i][delta_c]
            temp[i][0] = res

        for i in range(r):
            res = temp[i][0]
            for j in range(1, c):
                remove_c = j - K - 1
                if 0 <= remove_c < c:
                    res -= mat[i][remove_c]
                add_c = j + K
                if 0 <= add_c < c:
                    res += mat[i][add_c] 
                temp[i][j] = res

        for i in range(c):
            res = 0
            for delta_r in range(K + 1):
                res += temp[delta_r][i]
            answer[0][i] = res

        for i in range(c):
            res = answer[0][i]
            for j in range(1, r):
                remove_r = j - K - 1
                if 0 <= remove_r < r:
                    res -= temp[remove_r][i]
                add_r = j + K
                if 0 <= add_r < r:
                    res += temp[add_r][i] 
                answer[j][i] = res

        return answer

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
    flds = temp.replace(" ","").replace("\"","").rstrip().split("]],[")

    mat = [[int(col) for col in row.split(",")] for row in flds[0].replace("[[[", "").split("],[")]
    K = int(flds[1].replace("]]", ""))
    print("mat = {0}, K = {1:d}".format(mat, K))

    sl = Solution()
    time0 = time.time()

    result = sl.matrixBlockSum(mat, K)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
