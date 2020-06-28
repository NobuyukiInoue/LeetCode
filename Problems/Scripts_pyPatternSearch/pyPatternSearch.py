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
    target_command = f.readlines()
    f.close

    enable_regularexpression = True
    if argc >= 3:
       if argv[2].upper() == "TRUE":
           enable_regularexpression = True
       else:
           enable_regularexpression = False

    print("input target path.\n"
          "\n"
          "Example)\n"
          "../*/*/Project_Python3/*.py\n")

    target_path = input("target path[../*/*/Project_Python3/*.py] : ")
    if target_path == "":
        target_path = "../*/*/Project_Python3/*.py"
   
    # ファイル一覧の取得
    files_list = glob.glob(target_path)

    """
    for filename in files_list:
        print(filename)
    """

    for filename in files_list:
        # ファイルの内容を読み込む
        f = open(filename, "rt", encoding="utf8")
        contents = f.readlines()
        f.close

        # target_commandの実行結果を取得する
        if enable_regularexpression:
            result = get_contents_target_regular_pattern(contents, target_command)
        else:
            result = get_contents_target_perfect_pattern(contents, target_command)

        # target_commandの実行結果を表示する
        if result:
            print(filename)
            for i in range(result[0], result[1] + 1):
                print("{0:05d}: {1}".format(i, contents[i]), end="")

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

def get_contents_target_perfect_pattern(contents, target_command):
    """ target_commandと一致する行を検索する（完全一致）"""
    for i in range(len(contents)):
        src_i, dst_i = i, 0
        hit = True
        while src_i < len(contents) and dst_i < len(target_command):
            if contents[src_i] != target_command[dst_i]:
                hit = False
                break
            src_i += 1
            dst_i += 1
        if hit == True:
            if src_i < len(contents):
                return (i, src_i)
    return None


def get_contents_target_regular_pattern(contents, target_command):
    """ target_commandと一致する行を検索する（正規表現）"""
    for i in range(len(contents)):
        src_i, dst_i = i, 0
        hit = True
        while src_i < len(contents) and dst_i < len(target_command):
            if target_command[dst_i] == "\n":
                if contents[src_i] != target_command[dst_i]:
                    hit = False
                    break
            else:
                res = re.search(target_command[dst_i].replace("\n", ""), contents[src_i])
                if res == None:
                    hit = False
                    break
                elif res.regs[0][0] > 0:
                    hit = False
                    break
            src_i += 1
            dst_i += 1
        if hit == True:
            if src_i < len(contents):
                return (i, src_i)
    return None

if __name__ == "__main__":
    main()
