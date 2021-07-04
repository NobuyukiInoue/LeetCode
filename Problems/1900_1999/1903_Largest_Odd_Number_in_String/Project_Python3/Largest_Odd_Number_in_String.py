import os
import re
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def largestOddNumber(self, num: str) -> str:
        # 36ms
        n = len(num)
        for i in range(n-1,-1,-1):
            if int(num[i]) % 2:
                return num[:i+1]
        return ""

    def largestOddNumber2(self, num: str) -> str:
        # 60ms
        return re.sub('(^|[13579])[24680]*$', r'\1', num)

        
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
    num = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("num = {0}".format(num))

    sl = Solution()
    time0 = time.time()

    result = sl.largestOddNumber(num)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
