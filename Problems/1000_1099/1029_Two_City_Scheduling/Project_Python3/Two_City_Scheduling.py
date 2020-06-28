# coding: utf-8

import os
import sys
import time

class Solution:
#   def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    def twoCitySchedCost(self, costs):
        y = sorted(costs, key = lambda x: x[0] - x[1])
        ans = 0
        for i, e in enumerate(y):
            if i < len(y)//2:
                ans += e[0]
            else:
                ans += e[1]
        return ans

    def twoCitySchedCost_work1(self, costs):
        result = 0
        for data in costs:
            result += min(data)
        return result

    def twoCitySchedCost_work2(self, costs):
        if costs == None:
            return 0
        cities = [[0 for _ in range(len(costs))] for _ in range(len(costs[0]))]
        for row in range(len(costs)):
            for city in range(len(costs[row])):
                cities[city][row] = costs[row][city]

        for city in range(len(cities)):
            cities[city].sort()

        print("cities = {0}".format(cities))
        result = 0
        for city in range(len(cities)):
            for num in range(len(costs)//2):
                result += cities[city][num]

        return result

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    costs = [[int(col) for col in data.split(",")] for data in flds]
    print("costs = {0}".format(costs))

    sl = Solution()
    time0 = time.time()

    result = sl.twoCitySchedCost(costs)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
