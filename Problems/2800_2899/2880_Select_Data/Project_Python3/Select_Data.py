import os
import sys
import time
from typing import List, Dict, Tuple

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # return students.loc[students["student_id"] == 101, ["name", "age"]]
    # return students.loc[students["student_id"] == 101, "name" :]
    # 434ms - 449ms
    return students[students['student_id'] == 101][['name', 'age']]

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
    print("args = ")
    for line in lines:
        print(line, end="")
    print()

    loop_main(lines)

def loop_main(lines):
    column_names = lines[0].replace(" ", "").split("|")[1:-1]
    data = [lines[i].replace(" ", "").replace("\n", "").split("|")[1:-1] for i in range(2, len(lines))]
    students = pd.DataFrame(data, columns=column_names)
    print("students = \n{0}\n".format(students))

    time0 = time.time()

    result = selectData(students)

    time1 = time.time()

    print("result = \n{0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
