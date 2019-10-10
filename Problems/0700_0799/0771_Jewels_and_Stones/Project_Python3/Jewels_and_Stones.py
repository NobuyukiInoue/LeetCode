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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    words = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    J = words[0]
    S = words[1]
    print("J = %s, S = %s" %(J, S))

    time0 = time.time()

    sl = Solution()
    result = sl.numJewelsInStones(J, S)

    time1 = time.time()

    print("result = %d" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
