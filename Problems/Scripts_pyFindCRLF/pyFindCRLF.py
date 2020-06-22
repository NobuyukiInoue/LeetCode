# -*- coding: utf-8 -*-

import glob
import sys

def main():
    argv = sys.argv
    argc = len(argv)

    # 引数チェック
    if argc < 2:
        exit_msg(argv[0])
    target_path = argv[1]

    # ファイル一覧の取得
    files_list = glob.glob(target_path, recursive=True)

    """
    for filename in files_list:
        print(filename)
    """

    for filename in files_list:
        # ファイルの内容を読み込む
        f = open(filename, "rb")
        contents = f.readlines()
        f.close

        # target_commandの実行結果を取得する
        for i in range(len(contents)):
            contents_str = str(contents[i])
            if "\\r\\n" in contents_str:
                print("{0}    found CRLF.".format(filename))
                break

def exit_msg(argv0):
    """使用例を表示する"""
    print("Usage: python {0} <target_pattern>\n"
          "example)\n"
          "python {0} \"../*/*/Project_C/*.c\"\n"
          "python {0} \"../*/*/Project_C/lib/*.c\"\n"
          "python {0} \"../*/*/Project_C/include/*.h\"\n"
          "python {0} \"../*/*/Project_CS/*.cs\"\n"
          "python {0} \"../*/*/Project_Go/*.go\"\n"
          "python {0} \"../*/*/Project_Java/*.Java\"\n"
          "python {0} \"../*/*/Project_Python3/*.py\"\n"
          "python {0} \"../*/*/Project_Scala/*.scala\""
          .format(argv0))
    exit(0)

if __name__ == "__main__":
    main()
