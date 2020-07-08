# pyMultiLineGrep

Multi Line Grep by python3.

## Usage

```
$ python .\pyMultiLineGrep.py <target pattern file> [enable regular expression(default...True)]
```

## Execution example

```
$ cat .\sample\pattern1d.txt

.*main.*
```

```
$ python ./pyMultiLineGrep.py ./sample/pattern1d.txt
.\sample\pattern1d.txt
----------------------------------------
00000:
00001: .*main.*
----------------------------------------
input target path.

Example)
../*/*/Project_Python3/*.py

target path[../*/*/Project_Python3/*.py] : ../0001_0099/*/Project_C/*.c

../0001_0099\0001_Two_Sum\Project_C\main.c
00012:
00013: int loop_main(char* arg);

00034:
00035: int loop_main(char* arg)

00073:
00074: int main(int argc, char* argv[])

../0001_0099\0002_Add_Two_Number\Project_C\main.c
00014:
00015: int loop_main(char* arg);

00054:
00055: int loop_main(char* arg)

00104:
00105: int main(int argc, char* argv[])

../0001_0099\0003_Longest_Substring_Without_Repeating_Characters\Project_C\main.c
00012:
00013: int loop_main(char* arg);

00035:
00036: int loop_main(char* arg)

00063:
00064: int main(int argc, char* argv[])
...
...
```

```
$ python.exe .\pyMultiLineGrep.py .\sample\pattern6.txt false
.\sample\pattern6.txt
----------------------------------------
00000:     for temp in lines:
00001:         temp = temp.strip()
00002:         if temp == "":
00003:             continue
00004:         print("argv[1] = {0}".format(temp))
00005:         loop_main(temp)
00006:     #   print("Hit Return to continue...")
00007:     #   input()
00008:
----------------------------------------

input target path.

Example)
../*/*/Project_Python3/*.py

target path[../*/*/Project_Python3/*.py] : ../0001_0099/*/Project_Python3/*.py

../0001_0099\0001_Two_Sum\Project_Python3\Two_Sum.py
00050:     for temp in lines:
00051:         temp = temp.strip()
00052:         if temp == "":
00053:             continue
00054:         print("argv[1] = {0}".format(temp))
00055:         loop_main(temp)
00056:     #   print("Hit Return to continue...")
00057:     #   input()
00058:

../0001_0099\0002_Add_Two_Number\Project_Python3\Add_Two_Number.py
00069:     for temp in lines:
00070:         temp = temp.strip()
00071:         if temp == "":
00072:             continue
00073:         print("args = {0}".format(temp))
00074:         loop_main(temp)
00075:     #   print("Hit Return to continue...")
00076:     #   input()
00077:
...
...
```

## Licence

[MIT](https://github.com/NobuyukiInoue/pyMultiLineGrep/blob/master/LICENSE)


## Author

[Nobuyuki Inoue](https://github.com/NobuyukiInoue/)
