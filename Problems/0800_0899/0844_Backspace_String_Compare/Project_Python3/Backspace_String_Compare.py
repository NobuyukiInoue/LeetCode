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
    T = words[1]
    print("S = %s, T = %s" %(S, T))

    time0 = time.time()

    sl = Solution()
    result = sl.backspaceCompare(S, T)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
