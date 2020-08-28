# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def makeGood(self, s: str) -> str:
    def makeGood(self, s):
        # 28ms
        stack = []
        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

    def makeGood2(self, s):
        # 36ms
        enable_retry = True
        while enable_retry:
            enable_retry = False
            for i in range(len(s) - 1):
                if abs(ord(s[i]) - ord(s[i + 1])) == 0x20:
                    s = s[:i] + s[i + 2:]
                    enable_retry = True
                    break
        return s

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
    s = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.makeGood(s)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
