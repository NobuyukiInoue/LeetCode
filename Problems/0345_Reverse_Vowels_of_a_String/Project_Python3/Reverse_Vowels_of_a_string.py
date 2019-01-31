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

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()


def loop_main(temp):
    var_str = temp.replace("\"","").rstrip()

    print("s = %s" %var_str)

    time0 = time.time()

    sl = Solution()
    result = sl.reverseVowels(var_str)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
