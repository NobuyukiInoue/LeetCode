# coding: utf-8

import os
import sys
import time

class Solution:
#   def maximalSquare(self, matrix: List[List[str]]) -> int:
    def maximalSquare(self, matrix):
        # 200ms
        if not matrix:
            return 0
        res = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            res[i][0] = int(matrix[i][0])
        for j in range(len(matrix[0])):
            res[0][j] = int(matrix[0][j])
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                res[i][j] = 1 + min(res[i - 1][j], res[i][j - 1],res[i - 1][j - 1]) if matrix[i][j] == "1" else 0
        return max(map(max,res))**2

    def maximalSquare2(self, matrix):
        # 204ms
        if not matrix: return 0
        m , n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j]=='0' else 1 for j in range(n)]for i in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] =='1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
        
        ans = max([max(i) for i in dp])
        return ans ** 2

    def maximalSquare_bad(self, matrix):
        if not matrix:
            return 0
        result = 0
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if matrix[i][j] == '1':
                    if result == 0:
                        result = 1
                    if i > j:
                        max = len(matrix)
                    else:
                        max = len(matrix[i])
                    num = 1
                    while num < max:
                        if self.checkRowCol(matrix, i, j, num):
                            area = (num + 1)*(num + 1)
                            if area > result:
                                result = area
                        else:
                            break
                        num += 1
                    j = j + num - 1
                j += 1
            i += 1
        return result
    
    def checkRowCol(self, matrix, i, j, num):
        if i + num >= len(matrix):
            return False
        if j + num >= len(matrix[i]):
            return False
        for x in range(i, i + num + 1):
            if matrix[x][j + num] != '1':
                return False
        for y in range(j, j + num + 1):
            if matrix[i + num][y] != '1':
                return False
        return True

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
    str_args = temp.replace(" ","").replace("\",\"","").replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    matrix = [[ch for ch in row] for row in flds]
    print("matrix = [")
    for i in range(len(matrix)):
        if i == 0:
            print(" [{0}]".format(matrix[i]))
        else:
            print(",[{0}]".format(matrix[i]))
    print("]")

    time0 = time.time()

    sl = Solution()
    result = sl.maximalSquare(matrix)
    print("result = {0:d}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
