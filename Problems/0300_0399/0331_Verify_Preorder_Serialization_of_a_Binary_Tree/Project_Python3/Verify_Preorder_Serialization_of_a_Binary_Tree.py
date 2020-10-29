import os
import sys
import time

class Solution:
#   def isValidSerialization(self, preorder: str) -> bool:
    def isValidSerialization(self, preorder):
        # 20ms
        need = 1
        for val in preorder.split(','):
            if not need:
                return False
            need -= ' #'.find(val)
        return not need

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
    preorder = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("preorder = {0}".format(preorder))

    sl = Solution()
    time0 = time.time()

    result = sl.isValidSerialization(preorder)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
