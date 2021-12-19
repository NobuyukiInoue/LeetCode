import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countPoints(self, rings: str) -> int:
        # 24ms
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            rods[int(rings[i+1])].add(rings[i])
        return sum(len(rod) >= 3 for rod in rods)

    def countPoints2(self, rings: str) -> int:
        # 28ms
        rods = collections.defaultdict(set)
        for i in range(0, len(rings) - 1, 2):
            rods[rings[i + 1]].add(rings[i])
        return sum(len(v) == 3 for v in rods.values())

    def countPoints3(self, rings: str) -> int:
        # 32ms
        rods = [[False for j in range(3)] for i in range(10)]
        for i in range(0, len(rings), 2):
            if rings[i] == "R":
                rods[int(rings[i + 1])][0] = True
            elif rings[i] == "G":
                rods[int(rings[i + 1])][1] = True
            else:
                rods[int(rings[i + 1])][2] = True
        ans = 0
        for rod in rods:
            if rod[0] == rod[1] == rod[2] == True:
                ans += 1
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
    rings = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("rings = {0}".format(rings))

    sl = Solution()
    time0 = time.time()

    result = sl.countPoints(rings)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
