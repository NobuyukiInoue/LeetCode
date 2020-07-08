# coding: utf-8

import os
import sys
import time

class Solution:
#   def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word):
        # 360ms
        m = len(board)
        n = len(board[0])
        l = len(word)
        def fn(i, j, idx):
            if idx == l:
                return True
            board[i][j], temp = -1, board[i][j]
            for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if a >= 0 and b >= 0 and a < m and b < n and board[a][b] == word[idx] and fn(a, b, idx + 1):
                    return True
            board[i][j] = temp
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and fn(i, j, 1):
                        return True
        return False

    def exist_my(self, board, word):
        # 320ms
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.helper(board, i, j, word):
                    return True
        return False

    def helper(self, board, i, j, word):
        if len(word) <= 1:
            if board[i][j] == word[0]:
                return True
            else:
                return False
        if board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = ""
        if i - 1 >= 0:
            if self.helper(board, i - 1, j, word[1:]):
                return True
        if i + 1 < len(board):
            if self.helper(board, i + 1, j, word[1:]):
                return True
        if j - 1 >= 0:
            if self.helper(board, i, j - 1, word[1:]):
                return True
        if j + 1 < len(board[i]):
            if self.helper(board, i, j + 1, word[1:]):
                return True
        board[i][j] = temp
        return False

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

def board_to_str(board):
    res = "[\n"
    for i in range(len(board)):
        if i == 0:
            res += " ["
        else:
            res += ",["
        for j in range(len(board[i])):
            if j == 0:
                res += "\'" + board[i][j] + "\'"
            else:
                res += ", \'" + board[i][j] + "\'"
        res += "]\n"
    res += "]"
    return res

def loop_main(temp):
    args = temp.replace(" ","").replace("\"","").replace("[[[","").rstrip()
    flds = args.split("]],[")

    board = [[col for col in row.split(",")] for row in flds[0].replace("\'", "").split("],[")]
    word = flds[1].replace("]","")
#   print("board = {0}".format(board))
    print("board = {0}".format(board_to_str(board)))
    print("word = {0}".format(word))

    sl = Solution()
    time0 = time.time()

    result = sl.exist(board, word)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
