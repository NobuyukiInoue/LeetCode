import math
import os
import sys
import time

class Solution:
#   def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board):
        # 44ms
        for i in range(len(board)):
            dic = {}
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dic:
                    return False
                else:
                    dic[board[i][j]] = 1
        for j in range(len(board[0])):
            dic = {}
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dic:
                    return False
                else:
                    dic[board[i][j]] = 1

        data = []
        for row in board:
            data = data + row
        for i in range(0, 9, 3):
            for j in range(3):
                temp = data[i*9 + j*3:i*9 + (j + 1)*3] + data[(i + 1)*9 + j*3:(i + 1)*9 + (j + 1)*3] + \
                        data[(i + 2)*9 + j*3:(i + 2)*9 + (j + 1)*3]
                temp = [elem for elem in temp if elem!="."]
                if len(temp) != len(set(temp)):
                    return False
        return True

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    board = [[col for col in row.split(",")] for row in flds]

    print("board = ")
    for i in range(0, len(board)):
        print("{0}".format(board[i]))
        """
        for col in board[i]:
            print("{0}".format(col), end="")
        print("")
        """

    sl = Solution()
    time0 = time.time()

    result = sl.isValidSudoku(board)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
