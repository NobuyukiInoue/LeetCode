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
	/*
			line := make([]byte, 65536)
			for {
				n, err := fp.Read(line)
				if n == 0 {
					break
				}
				if err != nil {
					fmt.Println(err)
					break
				}

				trimedLine := strings.Trim(string(line[:n]), " ")
				trimedLine = strings.Trim(string(line[:n]), "\r")
				trimedLine = strings.Trim(string(line[:n]), "\n")
				fmt.Println(trimedLine)
				LoopMain(trimedLine)
		    }
	*/
	reader := bufio.NewReaderSize(fp, 65536)
	for {
		line, _, err := reader.ReadLine()
		fmt.Printf("line = %s\n", string(line))
		if err == io.EOF {
			break
		} else if err != nil {
			panic(err)
		}

		LoopMain(string(line))
	}
}

func Exists(name string) bool {
	_, err := os.Stat(name)
	return !os.IsNotExist(err)
}
