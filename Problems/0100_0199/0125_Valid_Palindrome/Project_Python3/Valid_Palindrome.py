import os
import re
import sys
import time

class Solution:
#    def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s):
        check = "".join(re.findall("[a-zA-Z0-9]*", s)).lower()
        return check == check[::-1]

#    def isPalindrome(self, s: str) -> bool:
    def isPalindrome_work(self, s):
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < len(s):
            while (ord(s[i]) < ord("a") or ord(s[i]) > ord("z")) and i < len(s) - 1:
                if ord("0") <= ord(s[i]) and ord(s[i]) <= ord("9"):
                    break
                i += 1
            while (ord(s[j]) < ord("a") or ord(s[j]) > ord("z")) and j > 0:
                if ord("0") <= ord(s[j]) and ord(s[j]) <= ord("9"):
                    break
                j -= 1
            if i >= j:
                break
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = %s" %s)

    time0 = time.time()

    sl = Solution()
    result = sl.isPalindrome(s)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
