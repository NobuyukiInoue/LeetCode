# coding: utf-8

from collections import defaultdict
import os
import sys
import time

class Solution:
#   def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
    def oddCells(self, n, m, indices):
        # 36ms
        row, col = [False] * n, [False] * m
        for r, c in indices:
            row[r] ^= True
            col[c] ^= True
        return sum(ro ^ cl for ro in row for cl in col)

    def oddCells2(self, n, m, indices):
        # 40ms
        cells = [[0 for _ in range(m)] for _ in range(n)]
    #   print("cells = {0}".format(printcells(cells)))
        for target in indices:
            t_row, t_col = target[0], target[1]
            for j in range(len(cells[t_row])):
                cells[t_row][j] += 1
            for i in range(len(cells)):
                cells[i][t_col] += 1
    #   print("cells = {0}".format(printcells(cells)))
        result = 0
        for t_row in cells:
            for t_cell in t_row:
                if t_cell % 2 == 1:
                    result += 1
        return result


def printcells(cells):
    resultStr = "["
    for i in range(len(cells)):
        if i == 0:
            resultStr += "\n  ["
        else:
            resultStr += "\n, ["
        for j in range(len(cells[i])):
            if j == 0:
                resultStr += str(cells[i][j])
            else:
                resultStr += "," + str(cells[i][j])
        resultStr += "]"
    resultStr += "\n]"
    return resultStr

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
    str_args = temp.replace("\"","").replace("]]]","").rstrip()
    flds = str_args.split("],[[")

    fld0 = flds[0].replace("[","").split(",")
    n, m = int(fld0[0]), int(fld0[1])
    print("n = {0:d}, m = {1:d}".format(n, m))

    indices = [[int(col) for col in data.split(",")] for data in flds[1].split("],[")]
    print("indices = {0}".format(indices))

    sl = Solution()
    time0 = time.time()
    result = sl.oddCells(n, m, indices)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
