import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        # 37ms - 40ms
        cnt = 0
        while x > 0 and y > 3:
            x -= 1
            y -= 4
            cnt += 1
        return "Alice" if cnt%2 == 1 else "Bob"

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    x, y = int(flds[0]), int(flds[1])
    print("x = {0:d}, y = {1:d}".format(x, y))

    sl = Solution()
    time0 = time.time()

    result = sl.losingPlayer(x, y)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
