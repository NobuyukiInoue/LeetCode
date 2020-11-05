import collections
import os
import sys
import time

class Solution:
#   def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
    def alertNames(self, keyName, keyTime):
        # 728ms
        name_to_time = collections.defaultdict(list)
        for name, hour_minutes in zip(keyName, keyTime):
            hour, minutes = map(int, hour_minutes.split(":"))
            times = hour*60 + minutes
            name_to_time[name].append(times)

        res = []
        for name, time_list in name_to_time.items():
            time_list.sort()
            for i, time in enumerate(time_list):
                if i >= 2 and time - time_list[i - 2] <= 60:
                    res.append(name)
                    break
        return sorted(res)

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
    flds = temp.replace("\"","").replace(", ",",").rstrip().split("],[")
    keyName = flds[0].replace("[[", "").split(",")
    keyTime = flds[1].replace("]]", "").split(",")

    print("keyName = {0}".format(keyName))
    print("keyTime = {0}".format(keyTime))

    sl = Solution()
    time0 = time.time()

    result = sl.alertNames(keyName, keyTime)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
