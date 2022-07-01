# My Submissions of LeetCode Problems.

* LeetCode ProblemSet

<https://leetcode.com/problemset/all/>

# How to Build and Run

Examples of How to Build and Run for 0001_Two_Sum Projects

## Project for Python3

### Change Directory
```
$ cd Problems/0001_0099/0001_Two_Sum/Project_Python3
```

### Run

```
$ python Two_Sum.py ../testdata.txt
```

## Project for C


### Change Directory

```
$ cd Problems/0001_0099/0001_Two_Sum/Project_C
```

### Build(no debug info)

* Windows (Minimalist GNU for Windows)

```  
> mingw32-make.exe all
```


* macOS or Linux (gcc)

```
$ make all
```

### Build(with debug info)

* Windows (Minimalist GNU for Windows)

```
> mingw32-make.exe debug
```

* macOS or Linux (gcc)

```
$ make debug
```

### Run

* Windows

```
> ./main.exe ../testdata.txt
```

* macOS

```
$ ./main_for_mac ../testdata.txt
```

* Linux

```
$ ./main_for_linux ../testdata.txt
```



## Project for C Sharp (.NET Core 2.0 or Later)


### Change Directory

```
$ cd Problems/0001_0099/0001_Two_Sum/Project_CS
```

### Run(dotnet) [Windows/macOS/Linux]

```
> dotnet run ../testdata.txt
```

### Run(PowerShell) [Windows/macOS/Linux]

```
powershell.exe

> main.ps1 TwoSum.cs ../testdata.txt
```

## Project for Java


### Change Directory

```
$ cd Problems/0001_0099/0001_Two_Sum/Project_Java
```

### Build

* Windows

```
> del *.class
> mingw32-make all
```

* macOS/Linux

```
$ make all
```


### Run

```
$ java Main ../testdata.txt
```

## Project for Scala


### Change Directory

```
$ cd Problems/0001_0099/0001_Two_Sum/Project_Scala
```

### Build


* Windows

```
> del *.class
> mingw32-make all
```

* macOS/Linux

```
$ make all
```

### Run

```
$ scala Main ../testdata.txt
```

## Project for Golang


### Change Directory

```
$ cd Problems/0001_0099/0001_Two_Sum/Project_Go
```

### Run

```
$ go run main.go ../testdata.txt
```

## Project for Elixir

### Change Directory

```
$ cd Problems/0001_0099/0001_Two_Sum/Project_Elixir
```

### Run

```
$ mix escript.build
$ ./main ../testdata.txt
```

# Get list of Projects

## MS-Windows(PowerShell)

```
> cd LeetCode
> Get-ChildItem -Directory -Recurse Project_Python3 | Select-String ":\\"
   ...
> Get-ChildItem -Directory -Recurse Project_C | Select-String ":\\"
   ...
> Get-ChildItem -Directory -Recurse Project_CS | Select-String ":\\"
   ...
> Get-ChildItem -Directory -Recurse Project_Java | Select-String ":\\"
   ...
> Get-ChildItem -Directory -Recurse Project_Scala | Select-String ":\\"
   ...
> Get-ChildItem -Directory -Recurse Project_Go | Select-String ":\\"
   ...
> Get-ChildItem -Directory -Recurse Project_Elixir | Select-String ":\\"
   ...
```

## macOS/Linux(bash)

```
$ cd LeetCode
$ find Problems -type d | grep "Project_Python3$" | sort
   ...
$ find Problems -type d | grep "Project_C$" | sort
   ...
$ find Problems -type d | grep "Project_CS$" | sort
   ...
$ find Problems -type d | grep "Project_Java$" | sort
   ...
$ find Problems -type d | grep "Project_Scala$" | sort
   ...
$ find Problems -type d | grep "Project_Go$" | sort
   ...
$ find Problems -type d | grep "Project_Elixir$" | sort
   ...
```
