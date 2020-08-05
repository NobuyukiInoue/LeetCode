import os
import sys
import time

class Solution:
#   def diffWaysToCompute(self, input: str) -> List[int]:
    def diffWaysToCompute(self, input):
        # 36ms
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.calc(j, k, input[i]))
        return res

    def calc(self, m, n, ope):
        if ope == "+":
            return m + n
        elif ope == "-":
            return m - n
        elif ope == "*":
            return m * n

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
    input = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("input = {0}".format(input))

    sl = Solution()
    time0 = time.time()

    result = sl.diffWaysToCompute(input)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
