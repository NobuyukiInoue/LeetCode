import os
import sys
import time

class Solution:
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)

    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans

class Solution_work:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        self.set_all_words(words)

        # delete duplicate records.
        self.words_list = list(set(self.words_list))
        print("words_list[] = {0}".format(self.words_list))

        result = []

        # set word_list[] min length.
        words_list_min = sys.maxsize
        for target in self.words_list:
            if words_list_min > len(target):
                words_list_min = len(target)

        # min_words_list_len = min(len(target) in for target in range(words_list))
        for i in range(len(s)):
            if len(s) - i < words_list_min:
                break
            for n in range(len(self.words_list)):
                if s[i] != self.words_list[n][0]:
                    break
                if s[i:i + len(self.words_list[n])] == self.words_list[n]:
                    result.append(i)

        return result

    def set_all_words(self, words):
        self.words_list = []
        for i in range(len(words)):
            self.set_sub_words(words, [i])
        return

    def set_sub_words(self, words, exclude_no):
        if len(exclude_no) == len(words):
            resultStr = ""
            for n in exclude_no:
                resultStr += words[n]
            self.words_list.append(resultStr)
            return

        for i in range(len(words)):
            if i in exclude_no:
                continue
            if len(exclude_no) < len(words):
                self.set_sub_words(words, exclude_no + [i])
        return

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
    s = flds[0]
    words = flds[1].split(",")
    print("s = {0}, words[] = {1}".format(s, words))

    sl = Solution()
    time0 = time.time()

    result = sl.findSubstring(s, words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
