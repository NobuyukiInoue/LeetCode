import os
import re
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # 48ms
        return sum([1 if "+" in op else -1 for op in operations])
        """
        ops = []
        for op in operations:
            if "+" in op:
                ops.append(1)
            else:
                ops.append(-1)
        return sum(ops)
        """

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
    operations = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("operations = {0}".format(operations))

    sl = Solution()
    time0 = time.time()

    result = sl.finalValueAfterOperations(operations)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
