import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # 28ms
        xy, yx = 0, 0
        for i in list(zip(s1, s2)):
            if i[0] != i[1]:
                if i[0] == 'x':
                    xy += 1 
                else:
                    yx += 1    
        if (xy + yx)&1:
            return -1  
        return xy//2 + xy%2 + yx//2 + yx%2

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
    flds = temp.replace("\"","").replace(", ",",").replace("[[","").replace("]]","").rstrip().split("],[")
    s1, s2 = flds[0], flds[1]
    print("s1 = \"{0}\", s2 = {1}".format(s1, s2))

    sl = Solution()
    time0 = time.time()

    result = sl.minimumSwap(s1, s2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
