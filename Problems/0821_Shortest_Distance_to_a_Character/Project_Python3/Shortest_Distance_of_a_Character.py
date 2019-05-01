import math
import os
import sys
import time

class Solution:
#    def shortestToChar(self, S: str, C: str) -> List[int]:
    def shortestToChar2(self, S, C):
        return [min(abs(i - ll) for ll in [i for i, e in enumerate(S) if e == C]) for i in range(len(S))]

    def shortestToChar(self, S, C):
        n = len(S)
        res = [n] * n
        pos = -n
        for i in range(n):
            if S[i] == C:
                pos = i
            res[i] = i - pos
        for i in range(n - 1, -1, -1):
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    words = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    S = words[0]
    C = words[1]
    print("S = %s, C = %s" %(S, C))

    time0 = time.time()

    sl = Solution()
    result = sl.shortestToChar(S, C)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
