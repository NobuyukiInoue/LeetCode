import os
import sys
import time
import mylinkedlist2

def Hash_Loop(ope, para):
    if len(ope) <= 0 or len(para) <= 0:
        return
    
    if len(ope) != len(para):
        return

    for i in range(len(ope)):
        if ope[i] == "MyLinkedList":
            ml = mylinkedlist.MyLinkedList()
            print("MyLinkedList()")
            # print("lists = {0}\n".format(ml.print_LinkedList()))
            print("lists = {0}\n".format(ml.coll))

        elif ope[i] == "get":
            result = ml.get(int(para[i]))
            print("get({0}) ... {1:d}".format(para[i], result))
            # print("lists = {0}\n".format(ml.print_LinkedList()))
            print("lists = {0}\n".format(ml.coll))

        elif ope[i] == "addAtHead":
            ml.addAtHead(int(para[i]))
            print("addAtHead({0})".format(para[i]))
            # print("lists = {0}\n".format(ml.print_LinkedList()))
            print("lists = {0}\n".format(ml.coll))

        elif ope[i] == "addAtTail":
            ml.addAtTail(int(para[i]))
            print("addAtTail({0})".format(para[i]))
            # print("lists = {0}\n".format(ml.print_LinkedList()))
            print("lists = {0}\n".format(ml.coll))

        elif ope[i] == "addAtIndex":
            flds = para[i].split(",")
            ml.addAtIndex(int(flds[0]), int(flds[1]))
            print("addAtIndex({0})".format(para[i]))
            # print("lists = {0}\n".format(ml.print_LinkedList()))
            print("lists = {0}\n".format(ml.coll))

        elif ope[i] == "deleteAtIndex":
            ml.deleteAtIndex(int(para[i]))
            print("deleteAtIndex({0})".format(para[i]))
            # print("lists = {0}\n".format(ml.print_LinkedList()))
            print("lists = {0}\n".format(ml.coll))

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
    str_args = temp.replace("\"","").replace("[[[","").replace("]]]","").rstrip().split("]],[[")
    ope = str_args[0].split(",")
    para = str_args[1].replace("]]", "").split("],[")

    print("ope[] = {0}".format(ope))
    print("para[] = {0}".format(para))

    time0 = time.time()

    Hash_Loop(ope, para)

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
