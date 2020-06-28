import os
import sys
import time
import MyHashSet

def HashMain_test():
    hashSet = MyHashSet.MyHashSet()
    hashSet.add(1)
    hashSet.add(2)

    ret = hashSet.contains(1)    # returns true
    print(ret)

    ret = hashSet.contains(3)    # returns false (not found)
    print(ret)

    hashSet.add(2)
    ret = hashSet.contains(2)    # returns true
    print(ret)

    hashSet.remove(2)

    ret = hashSet.contains(2)    # returns false (already removed)
    print(ret)

def Hash_Loop(ope, para):
    if len(ope) <= 0 or len(para) <= 0:
        return
    
    if len(ope) != len(para):
        return

    for i in range(len(ope)):
        if ope[i] == "MyHashSet":
            Hash = MyHashSet.MyHashSet()
            print("MyHashSet()")

        if ope[i] == "add":
            Hash.add(int(para[i]))
            print("Hash.add({0:d})".format(int(para[i])))

        elif ope[i] == "remove":
            Hash.remove(int(para[i]))
            print("Hash.remove({0:d})".format(int(para[i])))

        elif ope[i] == "contains":
            print("Hash.contains({0:d}) = {1}".format(int(para[i]), Hash.contains(int(para[i]))))

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
    flds = temp.replace("\"","").replace("[[[","").replace("]]]","").rstrip().split("]],[[")

    ope = flds[0].split(",")
    para = flds[1].replace("[", "").replace("]", "").split(",")
    print("operations[] = {0}, para = {1}".format(ope, para))

    time0 = time.time()

    Hash_Loop(ope, para)

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
