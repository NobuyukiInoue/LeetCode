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

    if (argc < 2):
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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    input = temp.replace("[","").replace("]","").rstrip()
    print("input = %s" %input)

    time0 = time.time()

    sl = Solution()
    result = sl.lengthLongestPath(input)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
