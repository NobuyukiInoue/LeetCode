# coding: utf-8

import os
import sys
import time

class Solution:
#   def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    def calculateMinimumHP(self, dungeon):
        # 68ms
        n = len(dungeon[0])
        need = [2**31] * (n-1) + [1]
        for row in dungeon[::-1]:
            for j in range(n)[::-1]:
                need[j] = max(min(need[j:j+2]) - row[j], 1)
        return need[0]

    def calculateMinimumHP_work(self, dungeon):
        if dungeon == None:
            return 1
        res = self.helper(dungeon, 0, 0, 0, 0)
        if res != None:
            if res[1] > 0:
                return res[1]
            else:
                return -res[1] + 1
        else:
            return 1
  
    def helper(self, dungeon, row, col, health, loses_max):
        health += dungeon[row][col]
        if health < 0 and health < loses_max:
            loses_max = health
        if row == len(dungeon) - 1 and col == len(dungeon[row]) - 1:
            return (health, loses_max)
        
        res_d, res_r = None, None
        if row < len(dungeon) - 1:
            res_d = self.helper(dungeon, row + 1, col, health, loses_max)
        if col < len(dungeon[row]) - 1:
            res_r = self.helper(dungeon, row, col + 1, health, loses_max)

        return self.get_bestResult(res_d, res_r)

    def get_bestResult(self, res1, res2):
        if res1 == None:
            return res2
        if res2 == None:
            return res1
        if res1[1]*res2[1] > 0:
            if abs(res1[1]) < abs(res2[1]):
                return res1
            else:
                return res2
        elif res1[1] > 0:
            return res1
        elif res2[1] > 0:
            return res2
        elif res1[1] == res2[1]:
            return res1
        else:
            if abs(res1[1]) < abs(res2[1]):
                return res1
            else:
                return res2
        print("get_bestResult() Error.")
        exit(-1)

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

def loop_main(temp):
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()

    dungeon_str = flds.split("],[")
    dungeon = [[int(col) for col in data.split(",")] for data in dungeon_str]
    print("dungeon = {0}".format(dungeon))

    time0 = time.time()

    sl = Solution()
    result = sl.calculateMinimumHP(dungeon)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
