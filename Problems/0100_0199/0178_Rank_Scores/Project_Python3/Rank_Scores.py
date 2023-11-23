import os
import sys
import time
from typing import List, Dict, Tuple

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # 420ms - 443ms
    score_df = pd.DataFrame(scores["score"])
    score_df["rank"] = score_df["score"].rank(method="dense", ascending=False)
    score_order = score_df.sort_values("score", ascending=False)
    return score_order

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

    data = [[col for col in data.split(",")] for data in flds.split("],[")]
    print("data = {0}".format(data))

    scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})
    print("scores = \n{0}".format(scores))

    time0 = time.time()

    result = order_scores(scores)

    time1 = time.time()

    print("result = \n{0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
