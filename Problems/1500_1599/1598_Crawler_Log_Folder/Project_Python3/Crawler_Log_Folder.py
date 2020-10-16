import os
import sys
import time

class Solution:
#   def minOperations(self, logs: List[str]) -> int:
    def minOperations(self, logs):
        # 36ms
        depth = 0
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1
            elif log != './':
                depth += 1
        return depth

    def minOperations2(self, logs):
        # 40ms
        stack = []
        for log in logs:
            if '.' not in log:
                stack.append(log)
            if log == '../' and stack:
                stack.pop()
        return len(stack)


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
    logs = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("logs = {0}".format(logs))

    sl = Solution()
    time0 = time.time()

    result = sl.minOperations(logs)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
