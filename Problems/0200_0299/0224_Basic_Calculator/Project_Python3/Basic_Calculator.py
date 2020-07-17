import os
import sys
import time

class Solution:
#   def calculate(self, s: str) -> int:
    def calculate(self, s):
        # 140ms
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop()*int(s[start:i])
                continue
            if c in "+-(":
            #   signs += signs[-1]*(1, -1)[c == '-'],
                if c == '-':
                    signs.append(-signs[-1])
                else:
                    signs.append(signs[-1])
            elif c == ")":
                signs.pop()
            i += 1
        return total

    def calculate2(self, s):
        # 156ms
        def evaluation(s):
            nonlocal i
            curSign, curResult = 1, 0
            while i < len(s):
                if s[i] == ' ': 
                    i += 1
                    continue
                elif s[i] == '+':
                    curSign = 1
                elif s[i] == '-':
                    curSign = -1
                elif s[i] == '(':
                    i += 1
                    curResult += curSign * evaluation(s)
                    curSign = 1
                elif s[i] == ')':
                    return curResult
                else:  # s[i] is digit.
                    curNum = int(s[i])
                    while i + 1 < len(s) and s[i + 1].isdigit():
                        curNum = curNum * 10 + int(s[i + 1])
                        i += 1
                    curResult += curNum * curSign
                    curSign = 1
                i += 1
            return curResult
        i = 0
        return evaluation(s)

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("path = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.calculate(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
