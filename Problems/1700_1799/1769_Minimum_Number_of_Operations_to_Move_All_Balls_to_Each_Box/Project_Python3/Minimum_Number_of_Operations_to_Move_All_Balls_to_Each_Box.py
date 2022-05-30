import itertools
import operator
import os
import sys
import time
from typing import List, Dict, Tuple
from unittest.case import _BaseTestCaseContext

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # 70ms - 105ms
        total, move_count = 0, 0
        res = []
        for i, box in enumerate(boxes):
            res.append(move_count)
            if box == '1':
                total += 1
            move_count += total
        total, move_count = 0, 0
        for i in range(len(boxes) -1, -1, -1):
            res[i] += move_count
            if boxes[i] == '1':
                total += 1
            move_count += total
        return res

    def minOperations_accumulate(self, boxes: str) -> List[int]:
        # 63ms - 121ms
        A = list(map(int, boxes))
        B = list(itertools.accumulate(A))
        return list(itertools.accumulate(B[:-1], lambda z,x: z + 2*x - B[-1], initial=sum(itertools.starmap(operator.mul, enumerate(A)))))

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
    boxes = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("boxes = \"{0}\"".format(boxes))

    sl = Solution()
    time0 = time.time()

    result = sl.minOperations(boxes)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
