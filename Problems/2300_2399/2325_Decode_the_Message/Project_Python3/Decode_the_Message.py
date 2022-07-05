# coding: utf-8

import collections
import os
import sys
import time
from typing import Collection, List, Dict, Tuple

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # 33ms - 80ms
        dic = collections.defaultdict()
        i = 0
        for _, ch in enumerate(key):
            if ch != " " and not ch in dic:
                dic[ch] = chr(ord('a') + i)
                i += 1
        res = []
        for _, ch in enumerate(message):
            if ch == " ":
                res.append(" ")
            else:
                res.append(dic[ch])
        return "".join(res)

    def decodeMessage_4liner(self, key: str, message: str) -> str:
        # 49ms - 83ms 
        k = dict()
        for c in key:
            if c != ' ' and c not in k: k[c] = len(k)                
        return ''.join([' ' if c == ' ' else chr(k[c] + ord('a')) for c in message])

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
    flds = temp.replace("\"","").replace(", ", ",").replace("[","").replace("]","").rstrip().split(",")
    key, message = flds[0], flds[1]
    print("key = \"{0}\", message = \"{1}\"".format(key, message))
  
    sl = Solution()
    time0 = time.time()

    result = sl.decodeMessage(key, message)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
