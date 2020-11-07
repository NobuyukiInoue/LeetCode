# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def solve(self, board: List[List[str]]) -> None:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # 124ms
        if not board:
            return []

        def dfs(board, i, j, visited):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == 'X':
                return
            if (i, j) in visited:
                return
            if board[i][j] == 'O':
                visited[(i, j)] = True

            dfs(board, i - 1, j, visited)
            dfs(board, i + 1, j, visited)
            dfs(board, i, j - 1, visited)
            dfs(board, i, j + 1, visited)
            return visited

        visited = {}
        for j in range(len(board[0])):
            if board[0][j] == 'O' :
                dfs(board, 0, j, visited)
            if board[len(board) - 1][j] == 'O':
                dfs(board, len(board) - 1, j, visited)

        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(board, i, 0, visited)
            if  board[i][len(board[0]) - 1] == 'O':
                dfs(board, i, len(board[0]) - 1, visited)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited:
                    board[i][j] = 'X'

    def solve2(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # 164ms
        if not board:
            return

        M, N = len(board), len(board[0])
        arr = None
        self.isSurround = None

        def dfs(board, i, j):
            if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                self.isSurround= False
            board[i][j] = "T"
            arr.append([i, j])
            if i - 1 >= 0 and board[i - 1][j] == "O":
                dfs(board, i - 1, j)
            if i + 1 < M and board[i + 1][j] == "O":
                dfs(board, i + 1, j)
            if j - 1 >= 0 and board[i][j - 1] == "O":
                dfs(board, i, j - 1)
            if j + 1 < N and board[i][j + 1] == "O":
                dfs(board, i, j + 1)

        def setSurround():
            for (i, j) in arr:
                board[i][j] = "X"

        def setNotSurround():
            for (i, j) in arr:
                board[i][j] = "N"

        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if board[i][j] == "O":
                    arr = []
                    self.isSurround = True
                    dfs(board.copy(), i, j)
                    if self.isSurround:
                        setSurround()
                    else:
                        setNotSurround()

        for i in range(M):
            for j in range(N):
                if board[i][j] == "N":
                    board[i][j] = "O"

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0}".format(grid[i][j]), end = "")
            else:
                print(" {0}".format(grid[i][j]), end = "")
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

    board = [[col for col in data.split(",")] for data in flds.split("],[")]
    printGrid("board", board)

    sl = Solution()
    time0 = time.time()

    result = sl.solve(board)

    time1 = time.time()

    printGrid("board", board)
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
