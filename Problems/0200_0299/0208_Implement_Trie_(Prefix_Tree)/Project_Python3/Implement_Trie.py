import os
import sys
import time
import Trie

def Implement_Trie_Loop(ope, params):
    if len(ope) <= 0 or len(params) <= 0:
        return
    
    if len(ope) != len(params):
        return

    for i in range(len(ope)):
        if ope[i] == "Trie":
            trie = Trie.Trie()
            print("Trie()")

        elif ope[i] == "insert":
            trie.insert(params[i])
            print("Trie.insert({0})".format(params[i]))

        elif ope[i] == "search":
            res = trie.search(params[i])
            print("Trie.search({0}) ... {1}".format(params[i], res))

        elif ope[i] == "startsWith":
            res = trie.startsWith(params[i])
            print("Trie.startsWith({0}) ... {1}".format(params[i], res))

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
    str_args = temp.replace(" ", "").replace("\"", "").rstrip().split("],[[")
    ope = str_args[0].replace("\"", "").replace("[", "").replace("]", "").split(",")

    if len(str_args) > 1:
        params = str_args[1].replace("]]]", "").split("],[")

    else:
        params = [[]]

    print("ope[] = {0}, params = {1}".format(ope, params))

    time0 = time.time()

    Implement_Trie_Loop(ope, params)

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
