import collections
import os
import sys
import time

class Solution:
#   def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 68ms
        i = 0
        for j in range(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            if maxCost < 0:
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1

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
    s, t, maxCost = flds[0], flds[1], int(flds[2])
    print("s = {0}, t = {1}, maxCost = {2:d}".format(s, t, maxCost))

    sl = Solution()
    time0 = time.time()

    result = sl.equalSubstring(s, t, maxCost)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
