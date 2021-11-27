import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        # 255ms
        for i in range(1, memory1 + memory2 + 2):
            if memory1 >= memory2:
                if memory1 < i:
                    return [i, memory1, memory2]
                memory1 -= i
            else:
                if memory2 < i:
                    return [i, memory1, memory2]
                memory2 -= i

    def memLeak2(self, memory1: int, memory2: int) -> List[int]:
        # 306ms
        i = 0
        while True:
            if memory1 >= memory2:
                if memory1 < i:
                    break
                memory1 -= i
            else:
                if memory2 < i:
                    break
                memory2 -= i
            i += 1
        return [i, memory1, memory2]

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
    flds = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    memory1, memory2 = int(flds[0]), int(flds[1])
    print("memory1 = {0:d}, memory2 = {1:d}".format(memory1, memory2))

    sl = Solution()
    time0 = time.time()

    result = sl.memLeak(memory1, memory2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
