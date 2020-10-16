import os
import sys
import time

class Solution:
#   def modifyString(self, s: str) -> str:
    def modifyString(self, s: str) -> str:
        # 24ms
        newString = ""
        s = list(s)
        prev = None
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        while len(s) > 0:
            nextVal = s[1] if len(s) > 1 else None
            if s[0] == "?":
                for letter in alphabet:
                    if letter != prev and letter != nextVal:
                        newString += letter
                        break
            else:
                newString += s[0]
                
            prev = newString[-1]
            s.pop(0)
            
        return newString

    def modifyString2(self, s):
        # 32ms
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?": 
                for c in "abc": 
                    if (i == 0 or s[i-1] != c) and (i+1 == len(s) or s[i+1] != c): 
                        s[i] = c
                        break 
        return "".join(s)

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

    result = sl.modifyString(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
