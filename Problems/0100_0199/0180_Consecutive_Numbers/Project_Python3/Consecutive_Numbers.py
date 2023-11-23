import os
import sys
import time
from typing import List, Dict, Tuple

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # 50ms - 707ms
    return logs.groupby(["num",logs.id-logs.groupby("num").transform("cumcount")],as_index=0)["id"].count().query("id > 2")["num"].to_frame("ConsecutiveNums").drop_duplicates()

def consecutive_numbers2(logs: pd.DataFrame) -> pd.DataFrame:
    # 626ms - 727ms
    all_the_same = lambda lst: lst.nunique()==1
    logs['is_consecutive'] = logs['num']\
        .rolling(window=3, center=True, min_periods=3)\
        .apply(all_the_same)
    return logs.query("is_consecutive == 1.0")[["num"]]\
        .drop_duplicates()\
        .rename(columns={"num": "ConsecutiveNums"})

def consecutive_numbers3(logs: pd.DataFrame) -> pd.DataFrame:
    # 636ms - 740ms
    logs = logs.sort_values("id", ignore_index = 1)
    logs["row_nb_by_num"] = logs.groupby("num").num.rank(method = "first")
    logs["groups"] = logs["id"] - logs["row_nb_by_num"]
    group_size = logs.groupby(["groups","num"]).id.count().reset_index()
    return group_size.loc[group_size.id >= 3]["num"].drop_duplicates().to_frame("ConsecutiveNums")

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
    flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").rstrip()

    data = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print("data = {0}".format(data))

    logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})
    print("logs = \n{0}".format(logs))

    time0 = time.time()

    result = consecutive_numbers(logs)

    time1 = time.time()

    print("result = \n{0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
