# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 180ms
        directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
        n, m = len(board), len(board[0])
        def recursive(board, row, col):
            mines = 0
            if board[row][col] == 'M' or board[row][col] == 'E':
                if board[row][col] == 'M':
                    board[row][col] = 'X'
                    return board
                elif board[row][col] == "E":
                    l = []
                    mines = 0
                    for i, j in directions:
                        r, c = row + i, col + j
                        if (r, c) and 0 <= r < n and 0 <= c < m:
                            if board[r][c] == "M" or board[r][c] == "X":
                                mines+=1
                            if board[r][c] == "M" or board[r][c] == "E":
                                l.append((r, c))
                    if mines == 0:
                        board[row][col] = 'B'
                        for i, j in l:
                            recursive(board, i, j)
                    else:
                        board[row][col] = str(mines)
            return board
        return recursive(board, click[0], click[1])

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
    flds = temp.replace(" ","").replace("\",\"","").replace("\"","").replace("[[[","").rstrip().split("]],[")

    board = [list(row.replace(",", "")) for row in flds[0].split("],[")]
    print("board = [")
    for row in board:
        print(",{0}".format(row))
    print("]")

    click = [int(pos) for pos in flds[1].replace("]]", "").split(",")]
    print("click = {0}".format(click))

    sl = Solution()
    time0 = time.time()

    result = sl.updateBoard(board, click)

    time1 = time.time()

    print("result = ")
    for row in result:
        print(",{0}".format(row))
    print("]")
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
