import os
import sys
import time

class Solution:
#   def maxLength(self, arr: List[str]) -> int:
    def maxLength(self, arr):
        # 96ms
        B, A = [set()], [set(a) for a in arr if len(set(a)) == len(a)]
        for a in A: B += [a|c for c in B if not a&c]
        return max(len(a) for a in B)

    def maxLength2(self, arr):
        # 96ms
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)

    def maxLength3(self, arr):
        # 160ms
        arr_len = len(arr)
        self.max_length = 0
        self.max_str = ""

        for i in range(arr_len):
            if not self.isUnique(arr[i]):
                continue
            if len(arr[i]) > self.max_length:
                self.max_length = len(arr[i])
            self.helper(arr, arr_len, i, arr[i])

        print(self.max_str)
        return self.max_length

    def helper(self, arr, arr_len, i, targetStr):
        targetStr_work = targetStr
        for j in range(i + 1, arr_len):
            prev_targetStr = targetStr_work
            targetStr_work += arr[j]
            if self.isUnique(targetStr_work):
                if len(targetStr_work) > self.max_length:
                    self.max_length = len(targetStr_work)
                    self.max_str = targetStr_work
                self.helper(arr, arr_len, j, targetStr_work)
                targetStr_work = prev_targetStr
            else:
                targetStr_work = prev_targetStr

    def isUnique(self, targetStr):
        lst = {}
        for ch in targetStr:
            if not ch in lst.keys():
                lst[ch] = 1
            else:
                return False
        return True


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
    arr = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    print("arr = {0}".format(arr))

    sl = Solution()
    time0 = time.time()
    result = sl.maxLength(arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
