import os
import sys
import time

class Solution:
#   def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
    def busyStudent(self, startTime, endTime, queryTime):
        # 40ms
        return sum([1 if startTime[i] <= queryTime <= endTime[i] else 0 for i in range(len(startTime))])

    def busyStudent2(self, startTime, endTime, queryTime):
        # 44ms
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                count += 1
        return count

    def busyStudent3(self, startTime, endTime, queryTime):
        # 52ms
        count = len(startTime)
        for i in range(len(startTime)):
            if queryTime < startTime[i] or queryTime > endTime[i]:
                count -= 1
        return count

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    startTime = [int(val) for val in str_args[0].split(",")]
    endTime = [int(val) for val in str_args[1].split(",")]
    queryTime = int(str_args[2])
    print("startTime[] = {0}, endTime = {1}, queryTime = {2}".format(startTime, endTime, queryTime))

    sl = Solution()
    time0 = time.time()
    result = sl.busyStudent(startTime, endTime, queryTime)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
