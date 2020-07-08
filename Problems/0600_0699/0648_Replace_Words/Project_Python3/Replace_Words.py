import collections
import os
import sys
import time

class Solution:
#   def replaceWords(self, dict: List[str], sentence: str) -> str:
    def replaceWords(self, dict, sentence):
        # 56ms
    	D, s = {}, sentence.split()
    	for d in dict:
    		if d[0] in D: D[d[0]].append([d,len(d)])
    		else: D[d[0]] = [[d,len(d)]]
    	for i in D: D[i].sort(key = lambda x: x[1])
    	for i,j in enumerate(s):
    		f, t = j[0], len(j)
    		if f not in D: continue
    		for a,b in D[f]:
    			if b > t: break
    			if a == j[:b]:
    				s[i] = a
    				break
    	return " ".join(s)

    def replaceWords2(self, dict, sentence):
        # 192ms
        rootset = set(dict)
        words = sentence.split()
        for i in range(len(words)):
            for pos in range(1, len(words[i])):
                if words[i][:pos] in rootset:
                    words[i] = words[i][:pos]
        return ' '.join(words)

    def replaceWords3(self, dict, sentence):
        # 200ms
        rootset = set(dict)
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word
        return " ".join(map(replace, sentence.split()))

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
    flds = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    dict = flds[0].split(",")
    sentence = flds[1]

    print("dict = {0}".format(dict))
    print("sentence = {0}".format(sentence))

    sl = Solution()
    time0 = time.time()
    result = sl.replaceWords(dict, sentence)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
