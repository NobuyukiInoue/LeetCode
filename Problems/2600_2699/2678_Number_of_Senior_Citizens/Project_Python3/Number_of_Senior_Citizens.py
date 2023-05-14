import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # 57ms - 61ms
        return sum(int(detail[11:13]) > 60 for detail in details)

    def countSeniors_1liner2(self, details: List[str]) -> int:
        # 58ms - 62ms
        return sum(int(detail[-4:-2]) > 60 for detail in details)

    def countSeniors2(self, details: List[str]) -> int:
        # 61ms - 62ms
        ans = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                ans += 1
        return ans

    def countSeniors3(self, details: List[str]) -> int:
        # 48ms - 60ms
        ans = 0
        for detail in details:
            tail = detail[11:]
            tail = tail[:len(tail) - 2]
            if int(tail) > 60:
                ans += 1
        return ans

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
    details = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("details = {0}".format(details))
  
    sl = Solution()
    time0 = time.time()

    result = sl.countSeniors(details)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
