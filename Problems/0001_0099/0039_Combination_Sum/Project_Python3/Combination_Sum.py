# coding: utf-8

import os
import sys
import time

class Solution:
#   def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinationSum(self, candidates, target):
        # 56ms
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    candidate = [int(num) for num in flds[0].split(",")]
    target = int(flds[1])

    print("candidate = {0}, target = {1:d}".format(candidate, target))
    time0 = time.time()

    sl = Solution()
    result = sl.combinationSum(candidate, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
