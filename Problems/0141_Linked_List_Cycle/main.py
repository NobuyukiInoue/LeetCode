import os
import subprocess
import sys

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 3):
        print("Usage: python %s <exec_source.py> <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)
        
    if not os.path.exists(argv[2]):
        print("%s not found..." %argv[2])
        exit(0)

    testDataFile = open(argv[2], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        try:
            exec_line = ['python', argv[1], temp]
            # ex = shell.Exec(exec_line)
            print("exec_line = %s" %exec_line)
            result = subprocess.run(exec_line)

            '''
            result = subprocess.run(exec_line, \
                shell=True, check=True, \
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, \
                universal_newlines=True)
            for result_stdout in result.stdout.splitlines():
                print('>>> ' + result_stdout)
            '''

        except subprocess.CalledProcessError:
            print('Exec Error...', file=sys.stderr)


if __name__ == "__main__":
    main()
