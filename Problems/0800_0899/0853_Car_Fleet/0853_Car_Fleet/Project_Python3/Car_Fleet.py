# coding: utf-8

import json
import os
import sys
import time

class Solution:
#   def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        # 148ms
        if not position:
            return 0
        posToSpeed = {position[i]: speed[i] for i in range(len(position))}
        position.sort()
        leaderTime = (target - position[-1]) / posToSpeed[position[-1]]
        currGroups = 1
        for i in range(len(position) - 2, -1, -1):
            currTime = (target - position[i]) / posToSpeed[position[i]]
            if currTime > leaderTime:
                currGroups += 1
                leaderTime = currTime
        return currGroups

    def carFleet_work(self, target: int, position: [int], speed: [int]) -> int:
        ans = 0
        currentPosition = [[]]*(target + 1)
        targetPositionCount = 0
        while len(currentPosition[target]) < len(position):
            currentPosition = [[] for _ in range(target + 1)]
            for i in range(len(position)):
                currentPosition[position[i]].append(i)
            self.print_currentPositiosn(currentPosition)
            """
            for i in range(len(position)):
                if position[i] + speed[i] >= target:
                    position[i] = target
                else:
                    position[i] += speed[i]
            """
            # get next position.
            for i in range(target - 1, -1, -1):
                lastFleetPos = target
                for carNum in currentPosition[i]:
                    if position[carNum] + speed[carNum] < lastFleetPos:
                        position[carNum] += speed[carNum]
                    else:
                        position[carNum] = lastFleetPos
                    if position[carNum] < lastFleetPos:
                        lastFleetPos = position[carNum]
            if len(currentPosition[target]) > targetPositionCount:
                ans += 1
                targetPositionCount = len(currentPosition[target])
            print("ans = {0:d}".format(ans))
        return ans

    def print_currentPositiosn(self, currentPosition: [[]]):
        print("====================")
        for i in range(len(currentPosition) - 1, -1, -1):
            print("[{0:2d}] ... {1}".format(i, currentPosition[i]))

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
    flds = temp.replace(" ","").replace("\"","").rstrip().split("],[")
    target = int(flds[0].replace("[[",""))
    if len(flds) > 1 and len(flds[1]) > 0:
        position = [int(n) for n in flds[1].split(",")]
    else:
        position = []
    flds2 = flds[2].replace("]]","")
    if len(flds) > 2 and len(flds2) > 0:
        speed = [int(n) for n in flds2.split(",")]
    else:
        speed = []
    print("target = {0}, position = {1}, speed = {2}".format(target, position, speed))

    sl = Solution()
    time0 = time.time()

    result = sl.carFleet(target, position, speed)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
