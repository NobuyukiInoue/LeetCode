import os
import sys
import time


class ParkingSystem:
    # 136ms

    def __init__(self, big: int, medium: int, small: int):
        self.slot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.slot[carType - 1] -= 1
        return self.slot[carType - 1] >= 0


class ParkingSystem2:
    # 120ms

    def __init__(self, big: int, medium: int, small: int):
        self.count = [0]*4
        self.count[1] = big
        self.count[2] = medium
        self.count[3] = small

    def addCar(self, carType: int) -> bool:
        if self.count[carType] > 0:
            self.count[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

class Solution:
    def main(self, cmds, args):
        res = []
        for i in range(len(cmds)):
            if cmds[i] == "ParkingSystem":
                parkingsystem = ParkingSystem(args[i][0], args[i][1], args[i][2])
                res.append(None)
                print("Exec ParkingSystem().")
            else:
                if parkingsystem is None:
                    print("parkingsystem not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "addCar":
                    res.append(parkingsystem.addCar(args[i]))
                    print("addCar({0}) ... {1}".format(args[i], res[-1]))
                else:
                    print("error... {0}".format(cmds[i]))
                    exit(1)
        return res

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
    flds = temp.replace("\"","").replace(", ",",").rstrip().split("],[[")
    cmds = flds[0].replace("[", "").replace("]", "").split(",")
    args = flds[1].replace("]]]","").split("],[")
    args[0] = [int(_) for _ in args[0].split(",")]
    for i in range(1, len(args)):
        args[i] = int(args[i])

    print("cmds[] = {0}".format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution()
    time0 = time.time()
    result = sl.main(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
