# coding: utf-8

import os
import re
import sys
import time

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if not s or not t:
            return True

        dic = {}
        dic2 = {}
        count = 0
        count2 = 0
        
        for a,b in zip(s,t):
            if not a in dic:
                dic[a] = count
                count += 1
            if not b in dic2:
                dic2[b] = count2
                count2 +=1

        for a,b in zip(s,t):
            if not dic[a] == dic2[b]:
                return False
        return True

    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        if s == t:
            return True

        dupchar = []
        for i in range(0, len(s) - 1):
            if i in dupchar:
                continue
            for j in range(i + 1, len(s)):
                if j in dupchar:
                    continue
                if s[i] == s[j]:
                    if t[i] == t[j]:
                        dupchar.append(i)
                        dupchar.append(j)
                    else:
                        return False
                elif t[i] == t[j]:
                    return False
        return True

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
    temp_wrk = temp.rstrip()
    temp_wrk = re.sub('^\[\[', "", temp_wrk)
    temp_wrk = re.sub('\]\]$', "", temp_wrk)
    temp_wrk = re.sub('^\"', "", temp_wrk)
    temp_wrk = re.sub('\"$', "", temp_wrk)
    words = temp_wrk.split("\"],[\"")

    s, t = words[0], words[1]

    time0 = time.time()

    sl = Solution()
    result = sl.isIsomorphic(s, t)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
