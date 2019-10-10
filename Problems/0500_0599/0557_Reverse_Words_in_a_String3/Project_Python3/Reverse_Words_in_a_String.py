# coding: utf-8

import os
import sys
import time

class Solution:
#    def reverseWords(self, s: str) -> str:
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])[::-1]

    def reverseWords_work(self, s):
        work_s = s.replace(",", " ")
        work_s = work_s.replace("  ", " ")
        words = work_s.split(" ")
        for i in range(len(words)):
            if i == 0:
                resultStr = words[i][::-1]
            else:
                resultStr += " " + words[i][::-1]
        return resultStr

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = %s" %s)

    time0 = time.time()

    sl = Solution()
    result = sl.reverseWords(s)

    time1 = time.time()
    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
