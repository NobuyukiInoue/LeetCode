# coding: utf-8

import os
import sys
import time

class Solution:
#   def gameOfLife(self, board: List[List[int]]) -> None:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # 16ms
        board[:] = [[int(3 in (count, count - live))
                for j, live in enumerate(row)
                for count in [sum(sum(row[j - (j > 0):j + 2])
                for row in board[i - (i > 0):i + 2])]]
                for i, row in enumerate(board)]
        
        print_board(board)

    def gameOfLife2(self, board):
        # 32ms
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.check(board, i, j, m, n)
                if board[i][j] == 1 and (lives == 2 or lives == 3):
                    board[i][j] = 3
                    continue
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

        print_board(board)

    def check(self, board, i, j, max_row, max_col):
        lives = 0
        for a, b in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                     (i, j - 1), (i, j), (i, j + 1),
                     (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
            if a > -1 and b > -1 and a < max_row and b < max_col:
                if board[a][b] % 2 == 1:
                    lives += 1
        if board[i][j] == 1:
            lives -= 1
        return lives

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

def print_board(board):
    print("board = [")
    for i in range(len(board)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(board[i])):
            if j == 0:
                print("{0:3d}".format(board[i][j]), end = "")
            else:
                print(",{0:3d}".format(board[i][j]), end = "")
        print("]")
    print("]")

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    board = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print_board(board)

    time0 = time.time()

    sl = Solution()
    sl.gameOfLife(board)

    time1 = time.time()

#   print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
