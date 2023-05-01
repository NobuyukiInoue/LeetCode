# coding: utf-8

import collections
import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # 6602ms - 6639ms
        def dfs(bottom):
            if len(bottom) == 2 and bottom in dic:
                return True
            options = []
            for i in range(len(bottom) - 1):
                if bottom[i:i+2] in dic:
                    options.append(dic[bottom[i:i+2]])
                else:
                    return False
            for bot in itertools.product(*options):
                if dfs(''.join(bot)):
                    return True
            return False
        dic = dict()
        for triplet in allowed:
            if triplet[:2] not in dic:
                dic[triplet[:2]] = []
            dic[triplet[:2]] += [triplet[2]]
        return dfs(bottom)

    def pyramidTransition2(self, bottom: str, allowed: List[str]) -> bool:
        # 9648ms - 9666ms
        def dfs(state: str, i: int, nxt: str) -> bool:
            if len(state) == 1:
                return True
            if len(state) - 1 == len(nxt):
                return dfs(nxt, 0, "")
            if i == len(state) - 1:
                return False
            for c in dic[state[i]+state[i + 1]]:
                if dfs(state, i + 1, nxt + c):
                    return True
            return False
        dic = collections.defaultdict(list)
        for s in allowed:
            dic[s[:2]].append(s[2])
        return dfs(bottom, 0, "")

    def pyramidTransition3(self, bottom: str, allowed: List[str]) -> bool:
        # Time Limit Exceedec(62/62)
        def pyramid(bottom):
        #   return len(bottom) == 1 or any(pyramid(i) for i in itertools.product(*(dic[a][b] for a, b in zip(bottom, bottom[1:]))))
            if len(bottom) == 1:
                return True
            for i in itertools.product(*(dic[a][b] for a, b in zip(bottom, bottom[1:]))):
                if pyramid(i):
                    return True
            return False
        dic = collections.defaultdict(lambda: collections.defaultdict(list))
        for a, b, c in allowed:
            dic[a][b].append(c)
        return pyramid(bottom)

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
    flds = temp.replace(", ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    bottom, allowed = flds[0], flds[1].split(",")
    print("bottom = {0}, allowed = [{1}]".format(bottom, allowed))

    sl = Solution()
    time0 = time.time()

    result = sl.pyramidTransition(bottom, allowed)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
