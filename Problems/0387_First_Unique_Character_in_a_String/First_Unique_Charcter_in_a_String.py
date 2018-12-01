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
    result = sl.firstUniqChar(var_str)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
