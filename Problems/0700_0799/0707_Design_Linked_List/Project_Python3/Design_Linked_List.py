import os
import sys
import time
import mylinkedlist

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

def Hash_Loop(ope, para):
    if len(ope) <= 0 or len(para) <= 0:
        return
    
    if len(ope) != len(para):
        return

    for i in range(len(ope)):
        if ope[i] == "MyLinkedList":
            ml = mylinkedlist.MyLinkedList()
            print("MyLinkedList()")
            # print("lists = %s\n" %ml.print_LinkedList())
            print("lists = %s\n" %ml.coll)

        elif ope[i] == "get":
            result = ml.get(int(para[i]))
            print("get(%s) ... %d" %(para[i], result))
            # print("lists = %s\n" %ml.print_LinkedList())
            print("lists = %s\n" %ml.coll)

        elif ope[i] == "addAtHead":
            ml.addAtHead(int(para[i]))
            print("addAtHead(%s)" %para[i])
            # print("lists = %s\n" %ml.print_LinkedList())
            print("lists = %s\n" %ml.coll)

        elif ope[i] == "addAtTail":
            ml.addAtTail(int(para[i]))
            print("addAtTail(%s)" %para[i])
            # print("lists = %s\n" %ml.print_LinkedList())
            print("lists = %s\n" %ml.coll)

        elif ope[i] == "addAtIndex":
            flds = para[i].split(",")
            ml.addAtIndex(int(flds[0]), int(flds[1]))
            print("addAtIndex(%s)" %para[i])
            # print("lists = %s\n" %ml.print_LinkedList())
            print("lists = %s\n" %ml.coll)

        elif ope[i] == "deleteAtIndex":
            ml.deleteAtIndex(int(para[i]))
            print("deleteAtIndex(%s)" %para[i])
            # print("lists = %s\n" %ml.print_LinkedList())
            print("lists = %s\n" %ml.coll)

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
    para = str_args[1].replace("]]", "").split("],[")

    print("ope[] = %s" %ope)
    print("para[] = %s" %para)

    time0 = time.time()

    Hash_Loop(ope, para)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()