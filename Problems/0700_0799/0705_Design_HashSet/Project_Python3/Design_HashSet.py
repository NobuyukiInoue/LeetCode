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
            print("Hash.add(%d)" %(int(para[i])))

        elif ope[i] == "remove":
            Hash.remove(int(para[i]))
            print("Hash.remove(%d)" %(int(para[i])))

        elif ope[i] == "contains":
            print("Hash.contains(%d) = %s" %(int(para[i]), Hash.contains(int(para[i]))))

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
    str_args = temp.replace("\"","").replace("[[[","").replace("]]]","").rstrip().split("]],[[")
    ope = str_args[0].split(",")
    para = str_args[1].replace("[", "").replace("]", "").split(",")

    print("operations[] = %s, para = %s" %(ope, para))

    time0 = time.time()

    Hash_Loop(ope, para)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
