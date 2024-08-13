import os
import sys
import time
from typing import List, Dict, Tuple

class NeighborSum:
    # 172ms - 179ms
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.pos = {grid[i][j]: (i, j) for i in range(self.n) for j in range(self.n)}

    def adjacentSum(self, value: int) -> int:
        x, y = self.pos[value]
        dirr = [(x -1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        total = 0
        for n_x, n_y in dirr:
            if 0 <= n_x < self.n and 0 <= n_y < self.n:
                total += self.grid[n_x][n_y]
        return total

    def diagonalSum(self, value: int) -> int:
        x, y = self.pos[value]
        dirr = [(x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]
        total = 0
        for n_x, n_y in dirr:
            if 0 <= n_x < self.n and 0 <= n_y < self.n:
                total += self.grid[n_x][n_y]
        return total

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)


class Solution:
    def main(self, cmds, args):
        res = []
        n = len(cmds)
        for i in range(n):
            if cmds[i] == "NeighborSum":
                neighborSum = NeighborSum(args[i])
                res.append(None)
                print("Exec NeighborSum().")
            else:
                if neighborSum is None:
                    print("NeighborSum not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "adjacentSum":
                    res.append(neighborSum.adjacentSum(args[i]))
                    print("adjacentSum({0}) ... {1}".format(args[i], res[-1]))
                elif cmds[i] == "diagonalSum":
                    res.append(neighborSum.diagonalSum(args[i]))
                    print("diagonalSum({0}) ... {1}".format(args[i], res[-1]))
                else:
                    print("error... {0}".format(cmds[i]))
                    exit(1)
        return res

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
    flds = temp.replace("\"", "").replace(", ", ",").rstrip().split("],[[")
    cmds = flds[0].replace("[", "").replace("]", "").split(",")
    flds1 = flds[1].replace("[[", "").split("]]],[")
    args = []
    args.append([[int(col) for col in row.split(",")] for row in flds1[0].split("],[")])
    for fld in flds1[1].replace("]]]]", "").split("],["):
        args.append(int(fld))
    print("cmds[] = {0}".format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution()
    time0 = time.time()
    result = sl.main(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
