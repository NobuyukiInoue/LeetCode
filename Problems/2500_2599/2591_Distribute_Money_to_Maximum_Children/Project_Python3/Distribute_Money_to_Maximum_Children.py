import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # 47ms
        money -= children
        if money < 0:
            return -1
        if money // 7 == children and money % 7 == 0:
            return children
        if money // 7 == children - 1 and money % 7 == 3:
            return children - 2
        return min(children - 1, money // 7)

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    money = int(flds[0])
    children = int(flds[1])
    print("money = {0:d}, time = {1:d}".format(money, children))

    sl = Solution()
    time0 = time.time()

    result = sl.distMoney(money, children)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
