import math
import os
import collections
import sys
import time
from functools import reduce

class Solution:
#   def isRobotBounded(self, instructions: str) -> bool:
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R':
                dx, dy = dy, -dx
            if i == 'L':
                dx, dy = -dy, dx
            if i == 'G':
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)

    def isRobotBounded2(self, instructions):
        ins = instructions.replace('LLLL', '').replace('RRRR', '').replace('RL', '').replace('LR', '')
        d, p = 1, 0
        for c in ins:
            if c == 'G':
                p += d
            else:
                d *= {'L':1j, 'R':-1j}[c]
        return d.real == 0 or p == 0 or d.real < 0

    def isRobotBounded3(self, instructions):
        instructions *= 4
        direction = 'N'
        directionNext = {'N': ('W', 'E'), 'E': ('N', 'S'), 'S': ('E', 'W'), 'W': ('S', 'N')}
        x, y = 0, 0
        for move in instructions:
            if move == 'G':
                if direction == 'N':
                    y += 1
                elif direction == 'E':
                    x += 1
                elif direction == 'S':
                    y -= 1
                else:
                    x -= 1
            elif move == 'L':
                direction = directionNext[direction][0]
            else: 
                direction = directionNext[direction][1]
        return x == 0 and y == 0

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
    instructions = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()
    print("instructions = {0}".format(instructions))

    sl = Solution()
    time0 = time.time()

    result = sl.isRobotBounded(instructions)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
