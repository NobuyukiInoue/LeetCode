import math
import os
import sys
import time

class Solution:
#    def titleToNumber(self, s: str) -> int:
    def titleToNumber2(self, s):
        # 72ms
        from functools import reduce
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])

    def titleToNumber0(self, s):
        # 56ms ~ 60ms
        number = 0
        for i in range(0, len(s)):
            number += (ord(s[i]) - ord('A') + 1)*int(math.pow(26, len(s) - 1 - i))
        return number

    def titleToNumber(self, s):
        # 56ms ~ 60ms
        number = 0
        for i in range(0, len(s)):
            number *= 26
            number += ord(s[i]) - ord('A') + 1
        return number

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()
    result = sl.titleToNumber(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
