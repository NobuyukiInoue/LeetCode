import math
import os
import sys
import time

class Solution:
#    def toLowerCase(self, str: str) -> str:
    def toLowerCase(self, str):
        ret = ""
        for c in str:
            c_val = ord(c)
            #if ord("A") <= c_val <= ord("Z"):
            if 0x40 <= c_val <= 0x5a:
                ret += chr(c_val + 0x20)
            else:
                ret += c
        return ret

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
    str = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("str = {0}".format(str))

    sl = Solution()
    time0 = time.time()

    result = sl.toLowerCase(str)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
