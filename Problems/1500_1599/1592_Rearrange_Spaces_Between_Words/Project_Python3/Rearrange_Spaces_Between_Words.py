import os
import sys
import time

class Solution:
#   def reorderSpaces(self, text: str) -> str:
    def reorderSpaces(self, text):
        # 32ms
        words = text.split()
        cnt = len(words)
        spaces = text.count(' ')
        gap = 0 if cnt == 1 else spaces // (cnt - 1)
        trailing_spaces = spaces if gap == 0 else spaces % (cnt - 1)
        return (' ' * gap).join(words) + ' ' * trailing_spaces

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
    text = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("text = {0}".format(text))

    sl = Solution()
    time0 = time.time()

    result = sl.reorderSpaces(text)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
