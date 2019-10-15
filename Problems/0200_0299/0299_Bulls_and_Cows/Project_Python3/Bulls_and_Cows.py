# coding: utf-8

import os
import sys
import time

import collections

class Solution:
#   def getHint(self, secret: str, guess: str) -> str:
    def getHint(self, secret, guess):
        # 44ms
        A = sum(a==b for a,b in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (A, sum(B.values()) - A)
    
    def getHint_bad(self, secret, guess):
        hit, blow = 0, 0
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                hit += 1
                secret = secret[:i] + secret[i + 1:]
                guess = guess[:i] + guess[i + 1:]
            else:
                i += 1
        secret = list(set(secret))
        guess = list(set(guess))
        for n in secret:
            if n in guess:
                blow += 1
        return str(hit) + "A" + str(blow) + "B"

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    str_args = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()
    flds = str_args.split(",")

    secret = flds[0]
    guess = flds[1]
    print("secret = {0}, guess = {1}".format(secret, guess))

    time0 = time.time()

    sl = Solution()
    result = sl.getHint(secret, guess)
    print("result = {0}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
