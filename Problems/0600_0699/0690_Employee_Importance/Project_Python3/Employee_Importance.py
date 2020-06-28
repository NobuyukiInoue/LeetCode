# coding: utf-8

import os
import sys
import time

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = {}
        for e in employees:
            dic[e.id] = [e.importance]
            dic[e.id].append(e.subordinates)

        return self.get_recur(dic, id)

    def get_recur(self, dict_employees, target_id):
        res = 0
        res += dict_employees[target_id][0]
        if len(dict_employees[target_id][1]) == 0:
            return res
        for t in dict_employees[target_id][1]:
            res += self.get_recur(dict_employees, t)
        return res

def set_employee(data):
    flds = data.split(",[")
    id_and_importance = flds[0].split(",")

    id = int(id_and_importance[0])
    importance = int(id_and_importance[1])
    subordinates = []

    if len(flds[1]) > 0:
        subordinates_str = flds[1].split(",")
        for target in subordinates_str:
            subordinates.append(int(target))

    return Employee(id, importance, subordinates)

def employee2string(data):
    return "[{0:d}, {1:d}, [{2}]]".format(data.id, data.importance, data.subordinates)

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
    pos_id = temp.rfind(",")
    id = int(temp[pos_id + 1:].replace(" ", "").replace("]", ""))
    flds = temp[:pos_id].replace(" ", "").replace("[[[", "").replace("]]]", "").split("]],[")

    employees = []
    for target in flds:
        employees.append(set_employee(target))

    for i in range(len(employees)):
        print("employees[{0:d}] = {1}".format(i, employee2string(employees[i])))

    print("id = {0:d}".format(id))

    sl = Solution()
    time0 = time.time()

    result = sl.getImportance(employees, id)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
