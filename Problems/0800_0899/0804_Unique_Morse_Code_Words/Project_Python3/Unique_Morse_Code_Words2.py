import os
import sys
import time

class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        dic = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
               ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
               "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        resultCodes = [""]*len(words)
        for i in range(len(words)):
            currentMorseCode = ""
            for j in range(len(words[i])):
                currentMorseCode += dic[ord(words[i][j]) - ord("a")]
            # print("words[i] = {0}, result = {1}".format(words[i], currentMorseCode))
            resultCodes[i] = currentMorseCode

        return len(list(set(resultCodes)))

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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    words = temp.replace(" ","").replace("\"", "").replace("[","").replace("]","").rstrip().split(",")
    print("words[] = {0}".format(words))

    sl = Solution()
    time0 = time.time()

    result = sl.uniqueMorseRepresentations(words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))



if __name__ == "__main__":
    main()
