package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Usage)\n" +
			"go run " + os.Args[0] + " <testdataFile>\n")
		return
	}

	if Exists(os.Args[1]) == false {
		fmt.Printf(os.Args[1] + " not found.\n")
		return
	}

	fp, err := os.Open(os.Args[1])
	if os.IsNotExist(err) {
		fmt.Println("file does not exist")
		return
	}

	// 読み込み
	reader := bufio.NewReaderSize(fp, 65536)
	for {
		line, _, err := reader.ReadLine()
		if err == io.EOF {
			break
		} else if err != nil {
			panic(err)
		}

		if len(line) == 0 {
			continue
		}

		fmt.Printf("line = %s\n", string(line))
		LoopMain(string(line))
	}
}

func Exists(name string) bool {
	_, err := os.Stat(name)
	return !os.IsNotExist(err)
}
