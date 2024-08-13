import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # 69ms - 70ms
        x, y = 0, 0
        for cmd in commands:
            if cmd == "LEFT":
                y -= 1
            elif cmd == "RIGHT":
                y += 1
            elif cmd == "UP":
                x -= 1
            else:
                x += 1
        return x*n + y

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

    n, commands = int(flds[0]), flds[1].replace("\"", "").split(",")
    print("n = {0:d}, commands = {1}".format(n, commands))

    sl = Solution()
    time0 = time.time()

    result = sl.finalPositionOfSnake(n, commands)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
