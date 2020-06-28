import math
import os
import sys
import time

class Solution:
#   def reverseOnlyLetters(self, S: str) -> str:
    def reverseOnlyLetters(self, S):
        # 36ms
        gen_S = (i for i in S[::-1] if i.isalpha())
        new_S = ""
        for i in S:
            if i.isalpha():
                new_S += next(gen_S)
            else:
                new_S += i
        return(new_S)

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
    result = sl.reverseOnlyLetters(S)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
