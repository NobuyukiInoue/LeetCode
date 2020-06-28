# coding: utf-8

import os
import sys
import time

class Solution:
#   def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    def robotSim(self, commands, obstacles):
        i = j = mx = d = 0
        move, obstacles = [(0, 1), (-1, 0), (0, -1), (1, 0), ], set(map(tuple, obstacles))
        for command in commands:
            if command == -2: d = (d + 1) % 4
            elif command == -1: d = (d - 1) % 4
            else:
                x, y = move[d]
                while command and (i + x, j + y) not in obstacles:
                    i += x
                    j += y
                    command -= 1
            mx = max(mx, i ** 2 + j ** 2)
        return mx

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
    str_args = temp.replace("\"","").rstrip().split("],[[")

    commands = [int(n) for n in str_args[0].replace("[[", "").split(",")]
    print("commands = {0}".format(commands))

    flds = str_args[1].replace("]]]","").split("],[")
    '''
    obstacles = [[0,0]]*len(flds)
    for i in range(len(flds)):
        obstacles[i] = [int(m) for m in flds[i].split(",")]
    '''
    if len(flds) > 0 and flds[0] != '':
        obstacles = [[int(m) for m in obj.split(",")] for obj in flds]
    else:
        obstacles = [[]]
    print("obstacles = {0}".format(obstacles))

    sl = Solution()
    time0 = time.time()

    result = sl.robotSim(commands, obstacles)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
