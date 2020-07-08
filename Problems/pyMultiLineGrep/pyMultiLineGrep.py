# -*- coding: utf-8 -*-

import glob
import os
import re
import sys

def main():
    argv = sys.argv
    argc = len(argv)

    # 引数チェック
    if argc < 2:
        exit_msg(argv[0])

    pattern_file = ""
    if argc >= 2:
        pattern_file = argv[1]

    if not os.path.exists(pattern_file):
        print("{0} not found.".format(pattern_file))
        exit_msg(argv[0])

    f = open(pattern_file, "rt", encoding="ascii")
    target_pattern = f.readlines()
    f.close

    """print patten_file contents"""
    print(pattern_file)
    print("----------------------------------------")
    for i in range(len(target_pattern)):
        print("{0:05d}: {1}".format(i, target_pattern[i]), end="")
    print("----------------------------------------\n")

    enable_regularexpression = True
    if argc >= 3:
       if argv[2].upper() == "TRUE":
           enable_regularexpression = True
       else:
           enable_regularexpression = False

    default_target, default_file = load_default_targetPath("./default.ini")
    target_path = input("target Parrent Directory[{0}] : ".format(default_target))
    if target_path == "":
        target_path = default_target

    target_file = input("target File Pattern[{0}] : ".format(default_file))
    if target_file == "":
        target_file = default_file

    # ファイル一覧の取得
    """
    files_list = glob.glob(target_path)
    files_list.sort()
    """
    files_list = find_all_matched_files(target_path, target_file)
    """
    for filename in files_list:
        print(filename)
    """

    for filename in files_list:
        # ファイルの内容を読み込む
        f = open(filename, "rt", encoding="utf8")
        contents = f.readlines()
        f.close

        # target_patternの実行結果を取得する
        if enable_regularexpression:
            result = get_line_target_regular_pattern(contents, target_pattern)
        else:
            result = get_line_target_perfect_pattern(contents, target_pattern)

        # target_patternの実行結果を表示する
        if len(result) > 0:
            print(filename)
            for i in range(len(result)):
                for j in range(result[i][0], result[i][1]):
                    print("{0:05d}: {1}".format(j, contents[j]), end="")
                print()

def exit_msg(argv0):
    """使用例を表示する"""
    print("Usage: python {0} <target pattern file> [enable regular expression]\n"
          "\n"
          "example)\n"
          "python {0} pattern1.txt\n"
          "python {0} pattern2.txt\n"
          "python {0} pattern5.txt false\n"
          "python {0} pattern6.txt false\n"
          .format(argv0))
    exit(0)

def load_default_targetPath(default_ini_file):
    targetPath, pattern = ".", "*"

    if not os.path.exists(default_ini_file):
        return (targetPath, pattern)

    # ファイルの内容を読み込む
    f = open(default_ini_file, "rt", encoding="utf8")
    contents = f.readlines()
    f.close

    for line in contents:
        pos = line.find("#")
        if pos == 0:
            continue
        elif pos > 0:
            line = line[:pos]
        if "targetPath=" in line:
            flds = line.rstrip().split("=")
            if len(flds) >= 2:
                targetPath = flds[1].replace("\"", "")
        elif "pattern=" in line:
            flds = line.rstrip().split("=")
            if len(flds) >= 2:
                pattern = flds[1].replace("\"", "")
    return (targetPath, pattern)

def find_all_matched_files(directory, patternStr):
    """ 指定したdirectory以下のpatternStrにマッチするファイルのパスを列挙する"""
    pattern = patternStr.replace("*", ".*").replace(".", "\.") + "$"
    fileList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            res = re.search(pattern, file)
            if res != None:
                fileList.append(os.path.join(root, file))
    fileList.sort()
    return fileList

def get_line_target_perfect_pattern(contents, target_pattern):
    """ target_patternと一致する行を検索する（完全一致）"""
    result = []
    for i in range(len(contents)):
        src_i, dst_i = i, 0
        hit = True
        while src_i < len(contents) and dst_i < len(target_pattern):
            if contents[src_i] != target_pattern[dst_i]:
                hit = False
                break
            src_i += 1
            dst_i += 1
        if hit == True:
            if src_i - i == len(target_pattern):
                result.append((i, src_i))
    return result


def get_line_target_regular_pattern(contents, target_pattern):
    """ target_patternと一致する行を検索する（正規表現）"""
    result = []
    for i in range(len(contents)):
        src_i, dst_i = i, 0
        hit = True
        while src_i < len(contents) and dst_i < len(target_pattern):
            if target_pattern[dst_i] == "\n":
                if contents[src_i] != target_pattern[dst_i]:
                    hit = False
                    break
            else:
                res = re.search(target_pattern[dst_i].replace("\n", ""), contents[src_i])
                if res == None:
                    hit = False
                    break
                elif res.regs[0][0] > 0:
                    hit = False
                    break
            src_i += 1
            dst_i += 1
        if hit == True:
            if src_i - i == len(target_pattern):
                result.append((i, src_i))
    return result

if __name__ == "__main__":
    main()
