import os
import sys
import time

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # 28ms
        x, y = 0, 0
        pos = [(x, y)]
        for ch in path:
            if ch == "N":
                x += 1
            elif ch == "E":
                y += 1
            elif ch == "W":
                y -= 1
            elif ch == "S":
                x -= 1
            if (x, y) in pos:
                return True
            pos.append((x, y))
        return False

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

    result = sl.isPathCrossing(path)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
