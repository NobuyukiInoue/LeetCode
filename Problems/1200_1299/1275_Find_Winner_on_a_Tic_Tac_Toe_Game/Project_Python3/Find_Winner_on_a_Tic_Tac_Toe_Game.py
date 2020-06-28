# coding: utf-8

import os
import sys
import time

import collections

class Solution:
#   def tictactoe(self, moves: List[List[int]]) -> str:
    def tictactoe(self, moves):
        # 24ms
        row, col = [[0] * 3 for _ in range(2)], [[0] * 3 for _ in range(2)]
        d1, d2, id = [0] * 2, [0] * 2, 0
        for r, c in moves:
            row[id][r] += 1
            col[id][c] += 1
            d1[id] += r == c
            d2[id] += r + c == 2
            if 3 in (row[id][r], col[id][c], d1[id], d2[id]):
                return 'AB'[id]
            id ^= 1
        return 'Draw' if len(moves) == 9 else 'Pending'

    def tictactoe2(self, moves):
        # 28ms
        # List winner case
        win = [
            [(0, 0),(0, 1),(0, 2)], [(0, 0),(1, 0),(2, 0)],
            [(1, 0),(1, 1),(1, 2)], [(0, 1),(1, 1),(2, 1)],
            [(2, 0),(2, 1),(2, 2)], [(0, 2),(1, 2),(2, 2)],
            [(0, 0),(1, 1),(2, 2)], [(0, 2),(1, 1),(2, 0)]
        ]
        
        # Distribute
        A = set(tuple(step) for step in moves[::2])
        B = set(tuple(step) for step in moves[1::2])
            
        # Check winner
        for win_case in win:
            if win_case[0] in A and win_case[1] in A and win_case[2] in A:
                return "A"
            if win_case[0] in B and win_case[1] in B and win_case[2] in B:
                return "B"
               
        # No winner
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    moves = [[int(col) for col in data.split(",")] for data in flds]
    print("moves = {0}".format(moves))

    sl = Solution()
    time0 = time.time()
    result = sl.tictactoe(moves)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
