import math
import os
import sys
import time

class Solution:
#   def numUniqueEmails(self, emails: List[str]) -> int:
    def numUniqueEmails(self, emails):
        for i in range(len(emails)):
            emails[i]= ((emails[i].split('@')[0]).replace('.','')).split('+')[0] + '@'+ emails[i].split('@')[1]
        return(len(set(emails)))

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
    list = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    print("list = {0}".format(list))

    sl = Solution()
    time0 = time.time()

    result = sl.numUniqueEmails(list)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
