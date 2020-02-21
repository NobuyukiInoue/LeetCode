# coding: utf-8

import os
import sys
import time

class Solution:
#   def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # 40ms
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        
        for i in range(1, n):
            if not obstacleGrid[0][i]:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]
            else:
                obstacleGrid[0][i] = 0
                
        for i in range(1, m):
            if not obstacleGrid[i][0]:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]
            else:
                obstacleGrid[i][0] = 0
                
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]+obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] = 0
                    
        return obstacleGrid[-1][-1]


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

def print_Grid(obstacleGrid):
    print("obstacleGrid = [")
    for i in range(len(obstacleGrid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(obstacleGrid[i])):
            if j == 0:
                print("{0:3d}".format(obstacleGrid[i][j]), end = "")
            else:
                print(",{0:3d}".format(obstacleGrid[i][j]), end = "")
        print("]")
    print("]")

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    obstacleGrid = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print_Grid(obstacleGrid)

    time0 = time.time()

    sl = Solution()
    result = sl.uniquePathsWithObstacles(obstacleGrid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
