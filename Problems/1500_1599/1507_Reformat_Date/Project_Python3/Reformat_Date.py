import os
import sys
import time

class Solution:
#   def reformatDate(self, date: str) -> str:
    def reformatDate(self, date):
        # 40ms
        parts = date.split()

        day = int(parts[0][:-2])
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(parts[1]) + 1
        year = int(parts[2])

        return "{:04d}-{:02d}-{:02d}".format(year, month, day)

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
    date = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("date = {0}".format(date))

    sl = Solution()
    time0 = time.time()

    result = sl.reformatDate(date)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
