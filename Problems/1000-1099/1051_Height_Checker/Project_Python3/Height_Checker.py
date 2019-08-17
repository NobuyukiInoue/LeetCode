# coding: utf-8

import os
import sys
import time

class Solution:
    def heightChecker(self, heights):
        # 36ms
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

#   def heightChecker(self, heights: List[int]) -> int:
    def heightChecker2(self, heights):
        # 40ms
        s_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != s_heights[i]:
                count += 1
        return count

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    heights = [int(val) for val in flds]
    print("time = %s" %heights)

    time0 = time.time()

    sl = Solution()
    result = sl.heightChecker(heights)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
