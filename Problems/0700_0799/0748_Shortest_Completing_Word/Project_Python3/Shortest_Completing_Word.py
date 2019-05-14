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

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    licensePlate = flds[0]
    words = flds[1].split(",")
    print("licensePlate = %s, words[] = %s\n" %(licensePlate, words))

    time0 = time.time()

    sl = Solution()
    result = sl.shortestCompletingWord(licensePlate, words)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()