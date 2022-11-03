# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # 55ms - 58ms
        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, len(month)):
            month[i] = month[i - 1] + month[i]
        alice_a = month[int(arriveAlice[:2]) - 1] + int(arriveAlice[3:])
        alice_l = month[int(leaveAlice[:2]) - 1] + int(leaveAlice[3:])
        bob_a = month[int(arriveBob[:2]) - 1] + int(arriveBob[3:])
        bob_l = month[int(leaveBob[:2]) - 1] + int(leaveBob[3:])
        return max(min(alice_l, bob_l) - max(alice_a, bob_a) + 1, 0)

    def countDaysTogether_4liner(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # 55ms - 65ms
        D = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def helper(days):
            return int(days[-2:]) + sum(D[:int(days[:2]) - 1])
        return max(0, helper(min(leaveAlice, leaveBob)) - helper(max(arriveAlice, arriveBob)) + 1)

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
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    arriveAlice, leaveAlice, arriveBob, leaveBob = flds[0], flds[1], flds[2], flds[3]
    print("arriveAlice = {0}, leaveAlice = {1}, arriveBob = {2}, leaveBob = {3}".format(arriveAlice, leaveAlice, arriveBob, leaveBob))
  
    sl = Solution()
    time0 = time.time()

    result = sl.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
