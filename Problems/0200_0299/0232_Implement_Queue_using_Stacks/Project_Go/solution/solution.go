package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func calc(cmds []string, argvals []string) {
	obj := Constructor()
	createdMyQueue := false

	for i, cmd := range cmds {
		if cmd == "MyQueue" {
			createdMyQueue = true
		} else {
			if createdMyQueue != true {
				fmt.Printf("MyQueue was not created.\n")
				os.Exit(1)
			}

			val, _ := strconv.Atoi(argvals[i])

			if cmd == "push" {
				obj.Push(val)
				fmt.Printf("Execute Push()\n")
			} else if cmd == "pop" {
				result := obj.Pop()
				fmt.Printf("Pop() ... %d\n", result)
			} else if cmd == "peek" {
				result := obj.Peek()
				fmt.Printf("Peek() ... %d\n", result)
			} else if cmd == "empty" {
				result := obj.Empty()
				fmt.Printf("Empty() ... %s\n", strconv.FormatBool(result))
			}
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],]")
	cmds := strings.Split(flds[0], ",")
	argtemp := strings.Replace(flds[1], "[", "", -1)
	argtemp = strings.Replace(argtemp, "]", "", -1)
	argvals := strings.Split(argtemp, ",")

	fmt.Printf("cmds[] = %s\n", cmds)
	fmt.Printf("argvals[] = %s\n", argvals)

	timeStart := time.Now()

	calc(cmds, argvals)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
