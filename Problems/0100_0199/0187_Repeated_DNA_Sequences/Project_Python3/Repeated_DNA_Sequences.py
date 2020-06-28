# coding: utf-8

import collections
import os
import re
import sys
import time

class Solution:
#   def findRepeatedDnaSequences(self, s: str) -> List[str]:
    def findRepeatedDnaSequences(self, s):
        # 60ms
        return [k for k,v in collections.Counter([s[x:x+10] for x in range(len(s)-9)]).items() if v > 1]

    def findRepeatedDnaSequences2(self, s):
        # 60ms
        dictionary = dict()
        for i in [s[x : x + 10] for x in range(len(s) - 9)]:
            dictionary[i] = dictionary.get(i, 0) + 1
        return [k for k, v in dictionary.items() if v > 1]

    def findRepeatedDnaSequences3(self, s):
        # 52ms
        r, record = set(), set()
        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            [record, r][substring in record].add(substring)
        return list(r)

    def findRepeatedDnaSequences_bad(self, s):
        resLength = 10
        res = []
        for i in range(len(s) - resLength + 1):
            subStr = s[i:i+resLength]
            if subStr in s[i+1:]:
                res.append(subStr)
        return res

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
    s = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    sl = Solution()
    time0 = time.time()

    result = sl.findRepeatedDnaSequences(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
