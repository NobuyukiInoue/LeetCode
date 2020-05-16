# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    def findItinerary(self, tickets):
        # 80ms
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    tickets = [[col for col in data.split(",")] for data in flds.split("],[")]
    print("tickets = {0}".format(tickets))
  
    time0 = time.time()

    sl = Solution()
    result = sl.findItinerary(tickets)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
