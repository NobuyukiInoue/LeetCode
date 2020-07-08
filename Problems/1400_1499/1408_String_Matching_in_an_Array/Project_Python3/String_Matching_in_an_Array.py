import os
import sys
import time

class Solution:
#   def stringMatching(self, words: List[str]) -> List[str]:
    def stringMatching(self, words):
        # 40ms
        if not words:
            return None

        words.sort(key=lambda w: len(w))
        res = set()

        for i, word in enumerate(words):
            for pw in words[i+1:]:
                if word in pw:
                    res.add(word)
        return list(res)

    def stringMatching2(self, words):
        # 48ms
        ans = []
        for w in words:
            for sub in words:
                if w != sub and w.find(sub) != -1:
                    ans.append(sub)
        return list(set(ans))

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
    words = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    print("words = {0}".format(words))

    sl = Solution()
    time0 = time.time()
    result = sl.stringMatching(words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
