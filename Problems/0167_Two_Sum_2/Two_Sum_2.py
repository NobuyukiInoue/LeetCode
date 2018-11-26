# coding: utf-8

import os
import sys
import time


class Solution:
    def twoSum0(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        resultNumbers = [0]*2
        for i in range(len(numbers)):
            if i > 1 and numbers[i] == numbers[i - 1]:
                continue
            resultNumbers[0] = i + 1
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    resultNumbers[1] = j + 1
                    return resultNumbers
                else:
                    if numbers[j] == numbers[j] - 1:
                        break
                    if numbers[i] + numbers[j] > target:
                        break
                    if target > 0 and numbers[j] > target:
                        break

        return resultNumbers

    # two-pointer
    def twoSum1(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
    
    # dictionary           
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
    
    # binary search        
    def twoSum3(self, numbers, target):
    #    for i in xrange(len(numbers)):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1


def array_str_to_int(numbersStr):
    numbers = [0]*len(numbersStr)
    for i in range(len(numbersStr)):
        numbers[i] = int(numbersStr[i])
    return numbers


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
        print("argv[1] = %s" %temp)
        loop_main(temp)


def loop_main(temp):
    flds = temp.split(", ")
    numbersStr = flds[0].replace("[","").replace("]","").split(",")
    numbers = array_str_to_int(numbersStr)
    target = int(flds[1])

    time0 = time.time()

    sl = Solution()
#   result = sl.twoSum(numbers, target)
    result = sl.twoSum3(numbers, target)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
