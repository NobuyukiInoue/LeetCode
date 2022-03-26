import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        # 20ms
        ts = 60*int(loginTime[:2]) + int(loginTime[-2:])
        tf = 60*int(logoutTime[:2]) + int(logoutTime[-2:])
        if 0 <= tf - ts < 15:
            return 0
        return tf//15 - (ts + 14)//15 + (ts > tf)*96

    def numberOfRounds_use_map(self, loginTime: str, logoutTime: str) -> int:
        # 53ms
        if logoutTime < loginTime:
            return self.numberOfRounds(loginTime, '24:00') + self.numberOfRounds('00:00', logoutTime)
        sHH, sMM = map(int, loginTime.split(':'))
        fHH, fMM = map(int, logoutTime.split(':'))
        start = sHH * 60 + sMM
        finish = fHH * 60 + fMM
        return max(0, finish // 15 - (start // 15 + (start % 15 > 0)))

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
    loginTime, logoutTime = flds[0], flds[1]
    print("loginTime = {0}, logoutTime = {1}".format(loginTime, logoutTime))

    sl = Solution()
    time0 = time.time()

    result = sl.numberOfRounds(loginTime, logoutTime)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
