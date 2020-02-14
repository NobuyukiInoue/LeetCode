# coding: utf-8

import os
import sys
import time

import collections

class Solution:
    def numEquivDominoPairs(self, dominoes):
        # 268ms
        return sum(v * (v - 1) // 2 for v in collections.Counter(tuple(sorted(x)) for x in dominoes).values())

    #   def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    def numEquivDominoPairs2(self, dominoes):
        # 268ms
        counter = collections.defaultdict(int)
        for domino in dominoes:
            counter[tuple(sorted(domino))] += 1
        # if v =1, then v(v-1)//2 is 0  else is v choose 2.
        return sum([v*(v - 1)//2 for v in counter.values()])

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    dominoes = [[int(col) for col in data.split(",")] for data in flds]
    print("dominoes = %s" %dominoes)

    time0 = time.time()

    sl = Solution()
    result = sl.numEquivDominoPairs(dominoes)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
