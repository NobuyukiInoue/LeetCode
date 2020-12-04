# coding: utf-8

import collections
import os
import sys
import time
import math

class Solution:
#   def totalFruit(self, tree: List[int]) -> int:
    def totalFruit(self, tree: List[int]) -> int:
        # 656ms
        fruits = [None, None]
        count = [0,0]
        last_count, last, total = 0, 1, 0

        for t in tree:
            if t in fruits:
                if t != fruits[last]:
                    last = int(not last)
                    last_count = count[last]
                count[last] += 1
            else:
                total = max(total, sum(count))
                count[last] -= last_count
                last = int(not last)
                fruits[last] = t
                count[last] = 1
                last_count = 0

        total = max(total, sum(count))
        return total

    def totalFruit2(self, tree: [int]) -> int:
        # 748ms
        count, i = {}, 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
        return j - i + 1

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    tree = [int(n) for n in flds.split(",")]
    print("tree = {0}".format(tree))

    sl = Solution()

    time0 = time.time()

    result = sl.totalFruit(tree)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
