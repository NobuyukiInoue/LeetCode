import collections
import os
import sys
import time

class Solution:
    def frequencySort(self, s: str) -> str:
        # 36ms
        return ''.join(sorted(map(lambda x: x[0] * x[1], collections.Counter(s).items()), key=lambda x: len(x), reverse=True))

    def frequencySort1(self, s: str) -> str:
        # 36ms
        pairs = sorted(collections.Counter(s).items(), key=lambda x:x[1], reverse=True)
        res = ""
        for ch in pairs:
            res += ch[0]*ch[1]
        return res

    def frequencySort2(self, s):
        # 40ms
        pairs = sorted(collections.Counter(s).items(), key=lambda x: x[1], reverse=True)
        return ''.join([c * n for c, n in pairs])

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.frequencySort(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
