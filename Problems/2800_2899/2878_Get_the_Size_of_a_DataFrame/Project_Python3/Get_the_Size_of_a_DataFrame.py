import os
import sys
import time
from typing import List, Dict, Tuple

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # 449ms - 507ms
    return [players.shape[0], players.shape[1]]
#   return list(players.shape)

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:2d}".format(grid[i][j]), end = "")
            else:
                print(",{0:2d}".format(grid[i][j]), end = "")
        print("]")
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
    print("args = ")
    for line in lines:
        print(line, end="")
    print()

    loop_main(lines)

def loop_main(lines):
    column_names = lines[0].replace(" ", "").split("|")[1:-1]
    data = [lines[i].replace(" ", "").replace("\n", "").split("|")[1:-1] for i in range(2, len(lines))]
    players = pd.DataFrame(data, columns=column_names)
    print("players = \n{0}\n".format(players))

    time0 = time.time()

    result = getDataframeSize(players)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
