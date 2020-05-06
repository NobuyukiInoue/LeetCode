import os
import sys
import time

class Solution:
#   def reformat(self, s: str) -> str:
    def reformat(self, s):
        # 32ms
        ans_array = [None] * len(s)
        nums = []
        letters = []
        
        for ch in s: 
            if ch.isdigit(): 
                nums.append(ch)
            else: 
                letters.append(ch)
        
        if abs(len(nums) - len(letters)) > 1: 
            return ""
        
        if len(nums) > len(letters):
            ans_array[::2] = nums
            ans_array[1::2] = letters
        else: 
            ans_array[::2] = letters
            ans_array[1::2] = nums
        return ''.join(ans_array)

    def reformat2(self, s):
        # 48ms
        if not s:
            return ""
        string, digits = [], []
        for i in s:
            if i.isdigit():
                digits.append(i)
            else:
                string.append(i)

        if abs(len(string) - len(digits)) > 1:
            return ""

        if len(string) < len(digits):
            string, digits = digits, string

        res = ""
        for i in range(len(digits)):
            res += "".join(string[i] + digits[i])

        return res + string[-1] if len(string) != len(digits) else res

    def reformat_work(self, s):
        # 48ms
        letters, nums = [], []
        for ch in s:
            if 0x30 <= ord(ch) and ord(ch) <= 0x39:
                nums.append(ch)
            else:
                letters.append(ch)

        len_letters, len_nums = len(letters), len(nums)

        if abs(len_letters - len_nums) > 1:
            return ""

        i, res = 0, ""
        if len_letters < len_nums:
            for i in range(len_letters):
                res += nums[i] + letters[i]
                i += 1
            res += nums[-1]
        elif len_nums < len_letters:
            for i in range(len_nums):
                res += letters[i] + nums[i]
                i += 1
            res += letters[-1]
        else:
            for i in range(len_letters):
                res += nums[i] + letters[i]
                i += 1

        return res

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    time0 = time.time()

    sl = Solution()
    result = sl.reformat(s)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
