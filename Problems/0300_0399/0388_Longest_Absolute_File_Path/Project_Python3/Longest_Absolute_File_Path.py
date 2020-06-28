import os
import sys
import time

class Solution:
#   def lengthLongestPath(self, input: str) -> int:
    def lengthLongestPath(self, input):
        # 32 - 44ms
        path, stack, max_length = input.split('\n'), [], 0
        for p in path:
            level = p.count('\t')
            if level == 0:
                stack = []
                stack.append(len(p) + 1)
            elif level >= len(stack):
                stack.append(len(p) + stack[level-1] -level + 1)
            else:
                stack = stack[:level]
                stack.append(stack[level-1] - level + len(p) + 1)
            if '.' in p:
                max_length = max(max_length, stack[level] - 1)
        return max_length

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
    input = temp.replace("[","").replace("]","").rstrip()
    print("input = {0}".format(input))

    sl = Solution()
    time0 = time.time()

    result = sl.lengthLongestPath(input)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
