import collections
import os
import re
import sys
import time

class Solution:
#    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    def shortestCompletingWord(self, licensePlate, words):
        ans = ''
        for w in words:
            check = True
            temp = w.lower()
            for l in licensePlate:
                if l.isalpha():
                    if l.lower() in temp:
                        temp = temp.replace(l.lower(), '', 1)
                    else:
                        check = False
                        break
            if check and (len(w) < len(ans) or ans == ''):
                ans = w
        return ans

    def shortestCompletingWord2(self, licensePlate, words):
        regex = re.compile('[^a-zA-Z]')
        licensePlate = regex.sub('', licensePlate)
        counter = collections.Counter(licensePlate.lower())
        res = ''
        for word in words:
            if self.contains(counter, word):
                if res == '' or len(word) < len(res):
                    res = word
        return res

    def contains(self, counter1, w2):
        c2 = collections.Counter(w2)
        c2.subtract(counter1)
        return all(map(lambda x: x >= 0,c2.values()))    

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    licensePlate = flds[0]
    words = flds[1].split(",")
    print("licensePlate = {0}, words[] = {1}\n".format(licensePlate, words))

    sl = Solution()
    time0 = time.time()

    result = sl.shortestCompletingWord(licensePlate, words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
