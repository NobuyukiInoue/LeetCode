import math
import os
import sys
import time
import Solution1
import Solution2

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    board = [[col for col in row.split(",")] for row in flds]

    print("board = ")
    for i in range(0, len(board)):
        print("%s" %board[i])
        """
        for col in board[i]:
            print("%s" %col, end="")
        print("")
        """

    time0 = time.time()

    sl = Solution1.Solution()
 #  sl = Solution2.Solution()
    sl.solveSudoku(board)

    time1 = time.time()

    print("board = ")
    for i in range(0, len(board)):
        print("%s" %board[i])
        """
        for col in board[i]:
            print("%s" %col, end="")
        print("")
        """
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
