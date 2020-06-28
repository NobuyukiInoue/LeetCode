# coding: utf-8

import os
import sys
import time
import copy

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: 
        """
    #    resultStr = copy.deepcopy(s)
        resultStr = list(s)
        target = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] in target:
                if s[j] in target:
                    resultStr[i] = s[j]
                    resultStr[j] = s[i]
                    i += 1
                j -= 1
                continue
            i += 1

        t = ""
        for i in range(len(s)):
            t += resultStr[i]
        return t

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
    s = temp.replace("\"","").rstrip()

    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.reverseVowels(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
