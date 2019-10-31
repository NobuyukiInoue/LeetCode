# coding: utf-8

import os
import sys
import time

class Solution:
#   def numDecodings(self, s: str) -> int:
    def numDecodings(self, s):
        # 36ms
        if not s or len(s) == 0:    
            return 0
        if s[0] == '0':
            return 0
        first, second = 1, 1
        for i in range(2, len(s)+1):
            newsecond = 0
            if s[i - 1] != '0':
                newsecond = second
            if '10' <= s[i - 2:i] <= '26':
                newsecond += first
            first, second = second, newsecond
        return second

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
    s = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    time0 = time.time()

    sl = Solution()
    result = sl.numDecodings(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
