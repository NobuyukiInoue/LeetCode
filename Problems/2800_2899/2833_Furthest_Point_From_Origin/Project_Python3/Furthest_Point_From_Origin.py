import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # 19ms - 44ms
        l, r, m = 0, 0, 0
        for move in moves:
            if move == "L":
                l += 1
            elif move == "R":
                r += 1
            else:
                m += 1
        return l - r + m if l >= r else r - l + m

    def furthestDistanceFromOrigin_1liner(self, moves: str) -> int:
        # 36ms - 41ms
        return moves.count('_') + abs(moves.count('R') - moves.count('L'))


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
    moves = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("moves = \"{0}\"".format(moves))

    sl = Solution()
    time0 = time.time()

    result = sl.furthestDistanceFromOrigin(moves)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
