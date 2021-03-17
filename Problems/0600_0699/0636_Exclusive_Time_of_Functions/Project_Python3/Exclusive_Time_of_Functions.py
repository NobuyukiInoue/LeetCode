import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # 68ms
        time_dict = collections.defaultdict(int)
        stack = []
        for log in logs:
            func_id, status, timestamp = log.split(':')
            if status=='start' or not stack:
                stack.append(log.split(':'))
            else:
                used_period = 0
                while stack and len(stack[-1]) == 2:
                    item = stack.pop()
                    used_period += item[1] - item[0] + 1
                start_entry = stack.pop()
                end_stamp = int(timestamp)
                start_stamp = int(start_entry[-1])
                delta =  end_stamp - start_stamp  + 1 - used_period
                time_dict[func_id] += delta
                stack.append((start_stamp, end_stamp))
        return [time_dict[str(k)] for k in range(n)]

    def exclusiveTime2(self, n: int, logs: List[str]) -> List[int]:
        # 72ms
        res = [0]*n
        stack = []
        for log in logs:
            ID, op, time = log.split(':')
            ID = int(ID)
            time = int(time)
            if op == 'start':
                if stack:
                    res[stack[-1][0]] += time-stack[-1][1]
                stack.append([ID, time])
            else:
                prev = stack.pop()
                res[ID] += time-prev[1] + 1
                if stack:
                    stack[-1][1] = time+1
        return res

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
    flds = temp.replace(", ", ",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    n = int(flds[0])
    logs = flds[1].split(",")

    print("n = {0}".format(n))
    print("logs = {0}".format(logs))

    sl = Solution()
    time0 = time.time()

    result = sl.exclusiveTime(n, logs)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
