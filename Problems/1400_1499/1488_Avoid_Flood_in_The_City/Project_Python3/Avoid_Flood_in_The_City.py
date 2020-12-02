# coding: utf-8

import bisect
import os
import sys
import time

class Solution:
#   def avoidFlood(self, rains: List[int]) -> List[int]:
    def avoidFlood(self, rains: [int]) -> [int]:
        # 1156ms
        q = []
        ans = []
        hashmap = {}
        for i in range(len(rains)):
            if rains[i] == 0:
                q.append(i)
                ans.append(1)
            else:
                if rains[i] in hashmap:
                    if len(q) == 0:
                        ans = []
                        break
                    else:
                        index = hashmap[rains[i]]
                        pos = bisect.bisect_right(q, index)
                        if pos < len(q):
                            ans[q[pos]] = rains[i]
                            q.pop(pos)
                        else:
                            ans = []
                            break
                hashmap[rains[i]] = i
                ans.append(-1)
        return ans

    def avoidFlood2(self, rains: [int]) -> [int]:
        # 1176ms
        if rains == []:
            return []
        N = len(rains)
        dry = []
        last_rain = {}
        ans = [1]*N
        for i in range(N):
            lake = rains[i]
            if lake == 0:
                dry.append(i)
            else:
                if lake in last_rain:
                    last_rain_day = last_rain[lake]
                    dry_id = bisect.bisect(dry, last_rain_day)
                    if dry_id == len(dry):
                        return []
                    use_dry = dry.pop(dry_id)
                    ans[use_dry] = lake
                last_rain[lake] = i
                ans[i] = -1
        return ans

    def avoidFlood_bad(self, rains: [int]) -> [int]:
        # Time Limit Exceeded.
        ans = [0]*len(rains)
        flood_lakes = []
        for i in range(len(rains)):
        #   print("rains[{0:d}] = {1:d}".format(i, rains[i]))
            if rains[i] > 0:
                if rains[i] in flood_lakes:
                    return []
                flood_lakes.append(rains[i])
                ans[i] = -1
            elif rains[i] == 0:
                isNotFind = True
                for j in range(i + 1, len(rains)):
                    if rains[j] > 0:
                        if rains[j] in flood_lakes:
                            pos = flood_lakes.index(rains[j])
                            flood_lakes = flood_lakes[:pos] + flood_lakes[pos + 1:]
                            ans[i] = rains[j]
                            isNotFind = False
                            break
                if isNotFind:
                    ans[i] = 1
    #   print("flood_lakes = {0}".format(flood_lakes))
        return ans

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    rains = [int(n) for n in flds.split(",")]
    print("rains = {0}".format(rains))

    sl = Solution()

    time0 = time.time()

    result = sl.avoidFlood(rains)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
