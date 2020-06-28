# coding: utf-8

import os
import sys
import time
import collections

class Solution:
#   def decodeString(self, s: str) -> str:
    def decodeString(self, s):
        # 32ms
        stack, times_stack = [], []
        idx, result = 0, ''
        while idx < len(s):
            if s[idx].isdigit():
                tmp = s[idx]
                idx += 1
                while idx < len(s) and s[idx].isdigit():
                    tmp += s[idx]
                    idx += 1
                times_stack.append(int(tmp))
                continue
            elif s[idx] == '[':
                stack.append(result)
                result = ''
            elif s[idx] == ']':
                times, previous = times_stack.pop(), stack.pop()
                result = previous + times * result
            else:
                result += s[idx]
            idx += 1
        return result

    def decodeString2(self, s):
        # 40ms
        """
        :type s: str
        :rtype: str
        """
        return self.unZip(s, 0)[0]

    def unZip(self, s, i):
        ss = ""
        while i < len(s):
            if s[i] in "123456789":
                j = i + 1
                while j < len(s) and s[j] in "0123456789":
                    j += 1
                n = int(s[i:j])                
                substr, k = self.unZip(s, j + 1)
                ss += n * substr
                i = k
                continue
            if s[i] == "]":
                return ss, i + 1
            ss += s[i]
            i += 1
        return ss, i

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
    s = temp.replace("[\"","").replace("\"]","").replace("\"","").replace(" ","").rstrip()
    print("s = {0}".format(s))
    sl = Solution()
    time0 = time.time()
    result = sl.decodeString(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
