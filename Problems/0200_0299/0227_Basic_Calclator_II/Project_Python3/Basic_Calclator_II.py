import math
import os
import sys
import time

class Solution:
#   def calculate(self, s: str) -> int:
    def calculate(self, s):
        # 72ms - 116ms
        num, presign, stack=0, "+", []
        for i in s + '+':
            if i.isdigit():
                num = num*10 + int(i)
            elif i in '+-*/':
                if presign == '+':
                    stack.append(num)
                elif presign == '-':
                    stack.append(-num)
                elif presign == '*':
                    stack.append(stack.pop()*num)
                elif presign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                presign = i
                num = 0
        return sum(stack)

    def calculate_work(self, s):
        # 244ms
        s = s.replace(" ", "")
        vals, opes = [], []
        i, pos_s = 0, 0
        while i < len(s):
            if s[i] in "+-*/":
                vals.append(int(s[pos_s:i]))
                opes.append(s[i])
                pos_s = i + 1
            i += 1
        vals.append(int(s[pos_s:]))

        i = 0
        while i < len(opes):
            if opes[i] == "*":
                vals[i] = vals[i] * vals[i + 1]
                vals = vals[:i + 1] + vals[i + 2:]
                opes = opes[:i] + opes[i + 1:]
            elif opes[i] == "/":
                vals[i] = vals[i] // vals[i + 1]
                vals = vals[:i + 1] + vals[i + 2:]
                opes = opes[:i] + opes[i + 1:]
            else:
                i += 1

        res = vals[0]
        for i in range(len(opes)):
            if opes[i] == "+":
                res += vals[i + 1]
            elif opes[i] == "-":
                res -= vals[i + 1]

        return res

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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()
    result = sl.calculate(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
