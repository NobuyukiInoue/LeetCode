# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 64ms
        visited = set()
        def dfs(room: int) -> None:
            if room not in visited: 
                visited.add(room)
                for key in rooms[room]:
                    dfs(key)
        dfs(0)
        return len(visited) == len(rooms)

    def canVisitAllRooms_bad(self, rooms: List[List[int]]) -> bool:
        check = [False]*len(rooms)
        check[0] = True
        for i, keys in enumerate(rooms):
            for room_number in keys:
                if room_number != i:
                    check[room_number] = True
        return not False in check

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    rooms = [[]]*len(flds)
    for i, data in enumerate(rooms):
        if len(flds[i]) > 0:
            rooms[i] = [int(n) for n in flds[i].split(",")]
    print("rooms = {0}".format(rooms))

    sl = Solution()

    time0 = time.time()

    result = sl.canVisitAllRooms(rooms)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
