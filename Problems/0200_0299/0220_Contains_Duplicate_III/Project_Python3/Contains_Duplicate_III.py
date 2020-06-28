# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # 56ms
        if k == 0 or (t == 0 and len(nums) == len(set(nums))): 
            return False
        myList = collections.deque(maxlen = k + 1)
        myDict = collections.defaultdict(int)
        i = 0
        while i < len(nums):
            v = nums[i]
            thisMin = v - t
            thisMax = v + t
            if len(myList) > 0 and not (min(myList) > thisMax or max(myList) < thisMin):
                for key in myDict.keys():
                    if myDict[key] != -1 and key >= thisMin and key <= thisMax:
                        return True
            myDict[v] = i
            myList.append(v)
            if len(myList) > k:
                remove = myList.popleft()
                myDict[remove] = -1
            i += 1
        return False

    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        # Time Limit Exceeded
        nums_length = len(nums)
        for i in range(nums_length):
            end_i = min(nums_length, i + 1 + k)
            for j in range(i + 1, end_i):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

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
    str_args = temp.replace(" ","").replace("\"","").replace("[[","").rstrip()
    flds = str_args.split("],")

    fld1 = flds[1].replace("]","").split(",")
    k, t = int(fld1[0]), int(fld1[1])
    print("k = {0:d}, t = {1:d}".format(k, t))

    nums = [int(data) for data in flds[0].split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.containsNearbyAlmostDuplicate(nums, k, t)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
