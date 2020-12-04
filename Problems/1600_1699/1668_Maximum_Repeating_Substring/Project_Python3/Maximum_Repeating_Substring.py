import os
import sys
import time
import re

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # 28ms
        count = 0
        while True:
            if word*(count + 1) in sequence:
                count += 1
            else:
                return count

    def maxRepeating_bad(self, sequence: str, word: str) -> int:
        return sequence.count(word)

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
    flds = temp.replace(", ", ",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    sequence, word = flds[0], flds[1]

    print("sequence = {0}".format(sequence))
    print("word = {0}".format(word))

    sl = Solution()
    time0 = time.time()

    result = sl.maxRepeating(sequence, word)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
