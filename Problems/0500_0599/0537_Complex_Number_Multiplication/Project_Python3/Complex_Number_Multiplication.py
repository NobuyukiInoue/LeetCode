import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # 40ms - 41ms
        flds1, flds2 = num1.split("+"), num2.split("+")
        n1r, n1i = int(flds1[0]), int(flds1[1][:-1])
        n2r, n2i = int(flds2[0]), int(flds2[1][:-1])
        re = n1r*n2r - n1i*n2i
        im = n1r*n2i + n1i*n2r
        return str(re) + "+" + str(im) + "i"

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    num1, num2 = flds[0], flds[1]
    print("num1 = \"{0}\", num2 = \"{1}\"".format(num1, num2))
  
    sl = Solution()
    time0 = time.time()

    result = sl.complexNumberMultiply(num1, num2)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
