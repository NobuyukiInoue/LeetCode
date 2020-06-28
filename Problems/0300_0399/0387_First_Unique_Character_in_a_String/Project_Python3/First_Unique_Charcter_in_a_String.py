# coding: utf-8

import os
import sys
import time
import copy

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = {e:index for index, e in enumerate(s)}
        
        for index, e in enumerate(s):
            if e in hash_table:
                if hash_table[e] == index:
                    return index
                del hash_table[e]
        return -1

    def firstUniqChar_old(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s) - 1

        checked = [False]*len(s)

        for i in range(len(s) - 1):
            if checked[i]:
                continue
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    checked[i] = True
                    checked[j] = True

        for i in range(len(s)):
            if checked[i] == False:
                return i
        
        return -1

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
    flds = temp.replace("\"","").rstrip()

    print("s = {0}".format(flds))

    sl = Solution()
    time0 = time.time()

    result = sl.firstUniqChar(flds)

    time1 = time.time()
    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
