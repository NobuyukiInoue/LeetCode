# coding: utf-8

import os
import sys
import time

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count('U')== moves.count('D') and moves.count('L')==moves.count('R'):
            return True
        else:
            return False

    def judgeCircle_work(self, moves: str) -> bool:
        x, y = 0, 0
        for ch in moves:
            if ch == "U":
                x += 1
            elif ch == "D":
                x -= 1
            elif ch == "L":
                y -= 1
            elif ch == "R":
                y += 1
        if x == 0 and y == 0:
            return True
        else:
            return False

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
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

def loop_main(temp):
    moves = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    print("moves = %s\n" %moves)

    time0 = time.time()

    sl = Solution()
    result = sl.judgeCircle(moves)

    time1 = time.time()
    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
