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
    S = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()

    print("S = %s" %S)

    time0 = time.time()

    sl = Solution()
    result = sl.reverseOnlyLetters(S)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
