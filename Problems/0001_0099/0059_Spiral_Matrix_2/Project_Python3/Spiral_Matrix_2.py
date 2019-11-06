# coding: utf-8

import os
import sys
import time

class Solution:
#   def generateMatrix(self, n: int) -> List[List[int]]:
    def generateMatrix(self, n):
        # 32ms
        result = [[0] * n for _ in range(n)]
        count, top, bottom, left, right = 1, 0, n - 1, 0, n - 1
        while left < right and top < bottom:
            for j in range(left, right):
                result[top][j] = count
                count += 1
            for i in range(top, bottom):
                result[i][right] = count
                count += 1
            for j in range(right, left, -1):
                result[bottom][j] = count
                count += 1
            for i in range(bottom, top, -1):
                result[i][left] = count
                count += 1
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        if left == right:
            result[top][right] = count
        return result

    def generateMatrix2(self, n):
        result, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(result), lo
            result = [range(lo, hi)] + zip(*result[::-1])
        return result

    def generateMatrix3(self, n):
        # 40ms
        def dirToIndex(x, y, d):
            if d == "r": return (x, y + 1, d) if y + 1 < n and matrix[x][y + 1] == 0 else (x + 1, y, "d")
            elif d == "d": return (x + 1, y, d) if x + 1 < n and matrix[x + 1][y] == 0 else (x, y - 1, "l")
            elif d == "l": return (x, y - 1, d) if y > 0 and matrix[x][y - 1] == 0 else (x - 1, y, "u")
            else: return (x - 1, y, d) if x > 0 and matrix[x - 1][y] == 0 else (x, y +1, "r")
        matrix = [[0 for i in range(1, n + 1)] for j in range(n)]
        num, dir, i, j = 1, "r", 0, 0
        while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1
            i, j, dir = dirToIndex(i, j, dir)
        return matrix

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
    fld = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(fld)

    time0 = time.time()

    sl = Solution()
    result = sl.generateMatrix(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
