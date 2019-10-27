# coding: utf-8

import os
import sys
import time
import collections

class Solution:
#   def removeDuplicateLetters(self, s: str) -> str:
    def removeDuplicateLetters(self, s):
        # 40ms
        d = {}
        count = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
            count[c] = count.get(c, 0) + 1
        stack = []
        cache = set()
        for c in s:
            if c not in cache:
                while stack and stack[-1] > c and count[stack[-1]] > 0:
                    cache.discard(stack.pop())
                stack.append(c)
                cache.add(c)
            count[c] -= 1
        return "".join(stack)

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
    s = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    print("s = {0}".format(s))
    time0 = time.time()

    sl = Solution()
    result = sl.removeDuplicateLetters(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
