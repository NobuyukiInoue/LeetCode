import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # 34ms - 40ms
        seen = set()
        for i, ch in enumerate(password):
            if i > 0 and password[i] == password[i - 1]:
                return False
            if ch.isupper():
                seen.add("u")
            if ch.islower():
                seen.add("l")
            if ch.isdecimal():
                seen.add("n")
            if ch in "!@#$%^&*()-+":
                seen.add("s")
        return  len(password) > 7 and len(seen) == 4

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
    password = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("password = {0}".format(password))

    sl = Solution()
    time0 = time.time()

    result = sl.strongPasswordCheckerII(password)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
