# coding: utf-8

import os
import sys
import time
import collections

class Solution:
#   def removeInvalidParentheses(self, s: str) -> List[str]:
    def removeInvalidParentheses(self, s):
        # 36ms
        if not s:
            return [""]
        def remove(s, last_iterate_index, last_remove_index, parents):
            balance = 0
            for i in range(last_iterate_index, len(s)):
                if s[i] == parents[0]:
                    balance += 1
                elif s[i] == parents[1]:
                    balance -= 1
                if balance >= 0:
                    continue
                for j in range(last_remove_index, i + 1):
                    if s[j] == parents[1] and (j == last_remove_index or s[j-1] != parents[1]):
                        remove(s[:j] + s[j+1:], i, j, parents)
                return
            reversed_s = s[::-1]
            if parents[0] == '(':
                remove(reversed_s, 0, 0, parents[::-1])
            else:
                result.append(reversed_s)
        result = []
        remove(s, 0, 0, ['(', ')'])
        return result

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
    result = sl.removeInvalidParentheses(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
