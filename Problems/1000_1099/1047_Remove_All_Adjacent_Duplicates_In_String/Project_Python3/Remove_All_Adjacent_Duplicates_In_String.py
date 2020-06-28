import math
import os
import sys
import time

class Solution:
#   def removeDuplicates(self, S: str) -> str:
    def removeDuplicates(self, S):
        # 80ms
        stack = []
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

    def removeDuplicates2(self, S):
        # 96ms
        i = 0
        while i < len(S) - 1:
            if S[i] == S[i + 1]:
                S = S[:i] + S[i + 2:]
                if i > 0:
                    i -= 1
            else:
                i += 1
        return S

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
    S = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()
    print("S = {0}".format(S))

    sl = Solution()
    time0 = time.time()
    result = sl.removeDuplicates(S)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
