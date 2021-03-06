import math
import os
import sys
import time

class Solution:
#    def numJewelsInStones(self, J: str, S: str) -> int:
    def numJewelsInStones(self, J, S):
        c = 0
        for s in S:
            if s in J:
                c += 1
        return c

    def numJewelsInStones2(self, J, S):
        dic = {}
        for c in J:
            if c in dic.keys():
                dic[c] += 1
            else:
                dic[c] = 1
        result = 0
        for c in S:
            if c in dic.keys():
                result += 1
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
    words = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    J = words[0]
    S = words[1]
    print("J = {0}, S = {1}".format(J, S))

    sl = Solution()
    time0 = time.time()

    result = sl.numJewelsInStones(J, S)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
