# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 71ms
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))
    
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
    flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").rstrip().split("],[")

    seats = [int(n) for n in flds[0].split(",")]
    students = [int(n) for n in flds[1].split(",")]
    print("seats = {0}, students = {1}".format(seats, students))

    sl = Solution()
    time0 = time.time()

    result = sl.minMovesToSeat(seats, students)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
