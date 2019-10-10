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
            # print("words[i] = %s, result = %s" %(words[i], currentMorseCode))
            resultCodes[i] = currentMorseCode

        return len(list(set(resultCodes)))

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()


def loop_main(temp):
    words = temp.replace(" ","").replace("\"", "").replace("[","").replace("]","").rstrip().split(",")
    print("words[] = %s" %words)

    time0 = time.time()

    sl = Solution()
    result = sl.uniqueMorseRepresentations(words)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))


if __name__ == "__main__":
    main()
