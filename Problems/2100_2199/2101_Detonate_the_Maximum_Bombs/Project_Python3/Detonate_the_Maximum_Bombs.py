# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # 684ms
        count_store = collections.defaultdict(int)
        radius_store = collections.defaultdict(int)
        for x, y, z in bombs:
            count_store[(x, y)] += 1
            radius_store[(x, y)] = max(z,radius_store.get((x, y),0))
            
        def check_distance(x, y, a, b):
            return ((a-x)**2 + (y-b)**2)**0.5 <= radius_store[(x, y)]
        
        graph = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                x, y, z = bombs[i]
                a, b,c = bombs[j]
                if check_distance(x, y, a, b):
                    graph[(x, y)].append((a, b))
        
        def recur_fn(x, y):
            result = [0]
            for a, b in graph[(x, y)]:
                if (a, b) not in curr_visited:
                    curr_visited.add((a, b))
                    result.append(count_store[(a, b)]+recur_fn(a, b))
            return sum(result)
        
        visited = set()
        ans = 0
        for x, y, z in bombs:
            if (x, y) not in visited:
                curr_visited = set()
                curr_visited.add((x, y))
                ans = max(count_store[(x, y)]+recur_fn(x, y), ans)
                visited = visited | curr_visited
        return ans

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:d}".format(grid[i][j]), end = "")
            else:
                print(",{0:d}".format(grid[i][j]), end = "")
        print("]")
    print("]")

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    bombs = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("bombs", bombs)
  
    sl = Solution()
    time0 = time.time()

    result = sl.maximumDetonation(bombs)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
