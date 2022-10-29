# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # 114ms - 218ms
        new_list = []
        for name, height in zip(names, heights):
            new_list.append((height, name))
        sorted_new_list = sorted(new_list, key = lambda x: -x[0])
        ans = [new_tuple[1] for new_tuple in sorted_new_list]
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    names = [_ for _ in flds[0].split(",")]
    heights = [int(n) for n in flds[1].split(",")]
    print("names = {0}, heights = {1}".format(names, heights))

    sl = Solution()
    time0 = time.time()

    result = sl.sortPeople(names, heights)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
