import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # 4594ms
        temp = []
        for d in divisors:
            tmp = {d:0}
            for n in nums:
                if n%d==0:
                    tmp[d] += 1
            temp.append(tmp)
        temp_list = [(list(d.keys())[0], list(d.values())[0]) for d in temp]
        sorted_templist = sorted(temp_list, key=lambda x:(-x[1], x[0]))
        return sorted_templist[0][0]

    def maxDivScore_2liner1(self, nums: List[int], divisors: List[int]) -> int:
        # 5380ms
        score = [sum(1 for num in nums if num % div == 0) for div in divisors]
        return min(divisors[i] for i in range(len(score)) if score[i] == max(score))

    def maxDivScore_2liner2(self, nums: List[int], divisors: List[int]) -> int:
        # 6562ms
        scores = [-sum(num % d == 0 for num in nums) for d in divisors]
        return sorted(zip(scores, divisors))[0][1]

    def maxDivScore_3(self, nums: List[int], divisors: List[int]) -> int:
        # 6400ms - 6402ms
        max_cnt, ans = -1, -1
        for _, divisor in enumerate(divisors):
            cnt = 0
            for _, num in enumerate(nums):
                if num % divisor == 0:
                    cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
                ans = divisor
            elif cnt == max_cnt:
                ans = min(ans, divisor)
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(col) for col in flds[0].split(",")]
    divisors = [int(col) for col in flds[1].split(",")]
    print("nums = {0}, divisors = {1}".format(nums, divisors))

    sl = Solution()
    time0 = time.time()

    result = sl.maxDivScore(nums, divisors)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
