import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # 148ms - 158ms
        balls = collections.Counter(map(tuple, pick))
        return len({player for (player, _), count in balls.items() if count > player})

    def winningPlayerCount2(self, n: int, pick: List[List[int]]) -> int:
        # 148ms - 163ms
        balls = [[0 for j in range(11)] for i in range(n)]
        winner = [0 for i in range(n)]
        for (player, color) in pick:
            balls[player][color] += 1
            if balls[player][color] == player + 1:
                winner[player] = 1
        return sum(winner)

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
    flds = temp.replace("]]]","").rstrip().split("],[[")
    n = int(flds[0].replace("[[", ""))
    pick = [[int(col) for col in row.split(",")] for row in flds[1].replace("]]", "").split("],[")]
    print("n = {0:d}, pick = {1}".format(n, pick))

    sl = Solution()
    time0 = time.time()

    result = sl.winningPlayerCount(n, pick)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
