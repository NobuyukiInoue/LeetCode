import collections
import os
import sys
import time

class Solution:
#   def majorityElement(self, nums: List[int]) -> List[int]:
    def majorityElement(self, nums):
        # 120ms
        count = collections.Counter(nums)
        return [num for num in count if count[num] > (len(nums) // 3)]

    def majorityElement2(self, nums):
        # 124ms
        if len(nums) <= 1:
            return nums
        limit_times = len(nums) // 3
        dic = {}
        res = []
        for target in nums:
            if target not in dic.keys():
                dic[target] = 1
            else:
                dic[target] += 1
            if dic[target] > limit_times:
                if target not in res:
                    res.append(target)
        return res

    def majorityElement3(self, nums):
        # 128ms
        limit_times = len(nums) // 3
        dic = {}
        for target in nums:
            if target not in dic.keys():
                dic[target] = 1
            else:
                dic[target] += 1
        res = [k for k, v in dic.items() if v > limit_times]
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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    nums = [int(val) for val in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.majorityElement(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
