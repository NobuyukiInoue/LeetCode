# coding: utf-8

import collections
import os
import sys
import time

class Solution:
    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)

    def isAnagram_work(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == None or t == None:
            return False

        if len(s) != len(t):
            return False

        dic_s = {}
        dic_t = {}

        for char_s, char_t in zip(s, t):
            if not char_s in dic_s:
                dic_s[char_s] = 1
            else:
                dic_s[char_s] += 1

            if not char_t in dic_t:
                dic_t[char_t] = 1
            else:
                dic_t[char_t] += 1

        if dic_s == dic_t:
            return True
        else:
            return False

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    words = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip().split(",")
    if len(words) >= 2:
        s, t = words[0], words[1]
    else:
        s, t = None, None

    time0 = time.time()
    sl = Solution()
    result = sl.isAnagram(s, t)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
