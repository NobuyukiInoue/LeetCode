# coding: utf-8

import os
import sys
import time
import collections

class Solution:
#   def maxNumberOfBalloons(self, text: str) -> int:
    def maxNumberOfBalloons(self, text):
        # 24ms
        return (lambda x: min(x[i]//(1 + (i in 'lo')) for i in 'balon'))(collections.Counter(text))

    def maxNumberOfBalloons2(self, text):
        # 40ms
        cnt = collections.Counter(text)
        cntBalloon = collections.Counter('balloon')
        return min([cnt[c] // cntBalloon[c] for c in cntBalloon])

    def maxNumberOfBalloons3(self, text):
        # 44ms
        balloon_dict = [0] * 26
        
        for char in text:
            balloon_dict[ord(char) - ord('a')] += 1
            
        return min(balloon_dict[ord('b') - ord('a')], balloon_dict[ord('a') - ord('a')],
                  balloon_dict[ord('l') - ord('a')] // 2, balloon_dict[ord('o') - ord('a')] // 2,
                  balloon_dict[ord('n') - ord('a')])

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
    text = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    print("text = {0}".format(text))
    time0 = time.time()

    sl = Solution()
    result = sl.maxNumberOfBalloons(text)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
