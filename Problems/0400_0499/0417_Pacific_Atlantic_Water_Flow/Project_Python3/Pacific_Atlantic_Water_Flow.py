# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#   def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    def pacificAtlantic(self, matrix):
        # 264ms
        if not matrix:
            return []

        p_visited = set()
        a_visited = set()
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if matrix[next_i][next_j] >= matrix[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)

        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(p_visited & a_visited)

def printGrid(title, grid):
    if grid is None:
        print("{0} = []".format(title))
        return
    print("{0} = [".format(title))
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:d}".format(grid[i][j]), end = "")
            else:
                print(",{0:d}".format(grid[i][j]), end = "")
        print("]")
    print("]")

def printResult(title, result):
    print("{0} = [".format(title))
    for i in range(len(result)):
        print(result[i])
    print("]")

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    matrix = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("matrix", matrix)
  
    sl = Solution()
    time0 = time.time()

    result = sl.pacificAtlantic(matrix)

    time1 = time.time()

    printGrid("result", result)
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
