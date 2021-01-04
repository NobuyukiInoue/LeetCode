# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # 68ms
        res = 0
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                if board[i][j] == "X":
                    if i > 0 and board[i - 1][j] == "X" or j > 0 and board[i][j - 1] == "X":
                        continue
                    res += 1
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
    str_args = temp.replace(" ","").replace("\",\"","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    flds = str_args.split("],[")
    board = [list(row) for row in flds]
  # print("board = {0}".format(board))
    for row in board:
        print("{0}".format(row))

    sl = Solution()
    time0 = time.time()

    result = sl.countBattleships(board)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
