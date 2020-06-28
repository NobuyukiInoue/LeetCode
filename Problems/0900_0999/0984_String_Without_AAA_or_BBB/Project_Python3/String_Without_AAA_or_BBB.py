# coding: utf-8

import os
import sys
import time

class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ret = ""
        while A > B > 0:
            ret += "aab"
            A -= 2
            B -= 1
        while B > A > 0:
            ret += "bba"
            A-=1
            B-=2
        if A==0 or B==0:
            #ret += 'a'*A if B==0 else 'b'*B
            if B==0:
                ret += 'a'*A
            else:
                ret += 'b'*B

        elif len(ret) == 0 or ret[-1]=='a':
            ret += 'ba'*A
        else:
            ret += 'ab'*A
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
    flds = temp.replace("[","").replace("]","").rstrip().split(",")
    A = int(flds[0])
    B = int(flds[1])

    sl = Solution()
    time0 = time.time()
    result = sl.strWithout3a3b(A, B)
    print("result = {0}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
