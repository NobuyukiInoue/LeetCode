import os
import sys
import time
import NumMatrix

def NumMatrix_Loop(ope, para):
    if len(ope) <= 0 or len(para) <= 0:
        return
    
    if len(ope) != len(para):
        return

    for i in range(len(ope)):
        if ope[i] == "NumMatrix":
            nm = NumMatrix.NumMatrix(para[i])
            print("NumMatrix()")

        if ope[i] == "sumRegion":
            sum = nm.sumRegion(para[i][0], para[i][1], para[i][2], para[i][3])
            print("NumMatrix.sumRegion(%d, %d, %d, %d) = %d" %(para[i][0], para[i][1], para[i][2], para[i][3], sum))

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
    str_args = temp.replace("\"", "").rstrip().split("],[[[[")
    ope = str_args[0].replace("\"", "").replace("[", "").replace("]", "").split(",")

    if len(str_args) > 1:
        params = str_args[1].split("]]],[")
#       print("operations[] = %s, params = %s" %(ope, params))

        matrix_str = params[0].split("],[")
#       print("matrix_str = %s" %matrix_str)

        matrix = [[int(col) for col in row.split(",")] for row in matrix_str]
        data2 = [[int(col) for col in row.split(",")] for row in params[1].replace("]]]", "").split("],[")]

        para = [matrix] + data2
    else:
        para = [[]]

    print("operations[] = %s, para = %s" %(ope, para))
    print("matrix = ")
    for row in para[0]:
        print("%s" %row)

    time0 = time.time()

    NumMatrix_Loop(ope, para)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
