# coding: utf-8

import os
import sys
import time

class Solution:
#   def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinationSum2(self, candidates, target):
        # 52ms
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
        return map(list, table[target])


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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    candidate = [int(num) for num in flds[0].split(",")]
    target = int(flds[1])
    print("candidate = {0}, target = {1:d}".format(candidate, target))

    sl = Solution()
    time0 = time.time()

    result = sl.combinationSum2(candidate, target)

    time1 = time.time()

    print("result = [")
    for tmp in result:
        print("{0}".format(tmp))
    print("result = ]")

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
