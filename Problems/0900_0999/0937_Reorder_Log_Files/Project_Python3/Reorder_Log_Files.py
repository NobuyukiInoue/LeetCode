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
    logs = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    print("logs = %s" %logs)

    time0 = time.time()

    sl = Solution()
    result = sl.reorderLogFiles(logs)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
