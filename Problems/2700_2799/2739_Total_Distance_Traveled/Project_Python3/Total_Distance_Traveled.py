import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # 65ms - 74ms
        return (mainTank + min((mainTank - 1)//4, additionalTank))*10

    def distanceTraveled2(self, mainTank: int, additionalTank: int) -> int:
        # 79ms - 86ms
        ans = 0
        while mainTank >= 5:
            mainTank -= 5
            ans += 50
            if additionalTank >= 1:
                additionalTank -= 1
                mainTank += 1
        return ans + mainTank*10

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

    mainTank, additionalTank = int(flds[0]), int(flds[1])
    print("mainTank = {0:d}, additionalTank = {1:d}".format(mainTank, additionalTank))

    sl = Solution()
    time0 = time.time()

    result = sl.distanceTraveled(mainTank, additionalTank)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
