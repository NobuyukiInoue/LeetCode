import os
import sys
import time

class Solution:
    def simplifyPath(self, path: str) -> str:
        # 24ms
        stack = []
        for fld in path.split("/"):
            if fld == "" or fld == ".":
                continue
            elif fld == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(fld)
        res = "/"
        for st in stack:
            res += st + "/"
        if len(res) > 1:
            return res[:-1]
        else:
            return res

    def simplifyPath2(self, path: str) -> str:
        # 28ms
        stack = []
        for fld in path.split("/"):
            if fld == "" or fld == ".":
                continue
            elif fld == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(fld)
        return "/" + "/".join(stack)


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
    path = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("path = {0}".format(path))

    sl = Solution()
    time0 = time.time()

    result = sl.simplifyPath(path)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
