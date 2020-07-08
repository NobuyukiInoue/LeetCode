import math
import os
import sys
import time

class Solution:
#   def reorderLogFiles(self, logs: List[str]) -> List[str]:
    def reorderLogFiles(self, logs):
        str_list = [x for x in logs if not str.isdigit(x.split()[1])]
        num_list = [x for x in logs if str.isdigit(x.split()[1])]
        order_str = sorted(str_list, key=lambda x: " ".join(x.split()[1:]))
        return order_str + num_list

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

    result = sl.reorderLogFiles(logs)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
