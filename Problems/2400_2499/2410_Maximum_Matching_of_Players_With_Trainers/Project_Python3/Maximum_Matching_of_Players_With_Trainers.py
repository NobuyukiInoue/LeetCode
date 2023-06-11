# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # 821ms
        players.sort()
        trainers.sort()
        res, i, j = 0, 0, 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                res += 1
                i += 1
            j += 1
        return res

    def matchPlayersAndTrainers_bad(self, players: List[int], trainers: List[int]) -> int:
        # Time Limit Exceeded. 33/35
        players.sort()
        trainers.sort()
        ans = 0
        for _, p in enumerate(players):
            j = 0
            while j < len(trainers):
                if p > trainers[j]:
                    trainers = trainers[:j] + trainers[j+1:]
                elif p <= trainers[j]:
                    trainers = trainers[:j] + trainers[j+1:]
                    ans += 1
                    break
                else:
                    j += 1
        return ans

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    players = [int(col) for col in flds[0].split(",")]
    trainers = [int(col) for col in flds[1].split(",")]
    print("players = {0}, trainers = {1}".format(players, trainers))

    sl = Solution()
    time0 = time.time()

    result = sl.matchPlayersAndTrainers(players, trainers)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
