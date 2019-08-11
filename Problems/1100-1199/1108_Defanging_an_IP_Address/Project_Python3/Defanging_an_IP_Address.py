# coding: utf-8

import os
import sys
import time

class Solution:
#   def defangIPaddr(self, address: str) -> str:
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    address = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    print("address = {0}".format(address))
    time0 = time.time()

    sl = Solution()
    result = sl.defangIPaddr(address)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
