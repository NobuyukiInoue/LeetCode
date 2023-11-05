import os
import sys
import time
from typing import List, Dict, Tuple

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # 467ms - 627ms
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    result_coumn_title = "getNthHighestSalary({0:d})".format(N)
    if N > len(sorted_salaries):
        return pd.DataFrame({result_coumn_title: [None]})
    nth_highest = sorted_salaries.iloc[N - 1]
    return pd.DataFrame({result_coumn_title: [nth_highest]})

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

    data = [lines[i].replace(" ", "").replace("\n", "").split("|")[1:-1] for i in range(2, len(lines) - 1)]
    for i, _ in enumerate(data):
        data[i][0] = int(data[i][0])
        data[i][1] = int(data[i][1])

    employee = pd.DataFrame(data, columns=column_names)
    N = int(lines[-1]) 
    print("employee = \n{0}\nN = {1:d}\n".format(employee, N))

    time0 = time.time()

    result = nth_highest_salary(employee, N)

    time1 = time.time()

    print("result = \n{0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
