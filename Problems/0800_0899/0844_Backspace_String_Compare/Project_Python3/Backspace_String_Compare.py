import math
import os
import sys
import time

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ans = ''
        ans_2 = ''
        for i in S:
            if i == '#':
                ans = ans[:-1]
            else:
                ans += i
        for i in T:
            if i == '#':
                ans_2 = ans_2[:-1]
            else:
                ans_2 += i
        return ans == ans_2

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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    words = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    S = words[0]
    T = words[1]
    print("S = {0}, T = {1}".format(S, T))

    sl = Solution()
    time0 = time.time()

    result = sl.backspaceCompare(S, T)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
