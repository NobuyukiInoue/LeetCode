import os
import sys
import time

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # 44ms
        workStr = s + "*" + s[::-1]
        cnt = [0]
        for i in range(1, len(workStr)):
            index = cnt[i - 1]
            while index > 0 and workStr[index] != workStr[i]:
                index = cnt[index - 1]
            cnt.append(index + (1 if workStr[index] == workStr[i] else 0))
        return s[cnt[-1]:][::-1] + s

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.shortestPalindrome(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
