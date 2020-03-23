# coding: utf-8

import bisect
import os
import sys
import time
import heapq

class Solution:
#   def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    def canFinish(self, numCourses, prerequisites):
        # 72ms
        G = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def intArrayToString(data):
    if len(data) <= 0:
        return "[]"
    resStr = "[" + str(data[0])
    for i in range(1, len(data)):
        resStr += ", " + str(data[i])
    resStr += "]"

    return resStr

def intintArrayToString(data):
    if len(data) <= 0:
        return "[]"

    resStr = "[\n" + "  " + intArrayToString(data[0]) + "\n"
    for i in range(1, len(data)):
        resStr += ", " + intArrayToString(data[i]) + "\n"
    resStr += "]"

    return resStr


def loop_main(temp):
    flds = temp.replace(", ", ",").split("],[[")
    flds[1] = flds[1].replace("]]]", "")

    if len(flds[1]) > 0:
        dataStr = flds[1].split("],[")
        prerequisites = [[int(n) for n in data.split(",") ] for data in dataStr]
    else:
        prerequisites = [[]]

    numCourses = int(flds[0].replace("[", ""))

    print("numCourses = {0:d}".format(numCourses))
    print("prerequisites = {0}".format(intintArrayToString(prerequisites)))

    time0 = time.time()

    sl = Solution()
    result = sl.canFinish(numCourses, prerequisites)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
