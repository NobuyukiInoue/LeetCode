package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

/*
func calc() {
	obj := Constructor()

	obj.Push(1)
	fmt.Printf("push(1)\n")

	obj.Push(2)
	fmt.Printf("push(2)\n")

	param_2 := obj.Pop()
	fmt.Printf("pop() ... %d\n", param_2)

	param_3 := obj.Top()
	fmt.Printf("top() ... %d\n", param_3)

	param_4 := obj.Empty()
	fmt.Printf("empty() ... %s\n", strconv.FormatBool(param_4))
}
*/

func calc(cmds []string, argvals []string) {
	obj := Constructor()
	createdMyStack := false

	for i, cmd := range cmds {
		if cmd == "MyStack" {
			createdMyStack = true
		} else {
			if createdMyStack != true {
				fmt.Printf("MyStack was not created.\n")
				os.Exit(1)
			}

			val, _ := strconv.Atoi(argvals[i])

			if cmd == "push" {
				obj.Push(val)
				fmt.Printf("Execute Push()\n")
			} else if cmd == "pop" {
				result := obj.Pop()
				fmt.Printf("Pop() ... %d\n", result)
			} else if cmd == "top" {
				result := obj.Top()
				fmt.Printf("Top() ... %d\n", result)
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

	flds := strings.Split(temp, "],[[")

	flds[0] = strings.Replace(flds[0], "[[", "", -1)
	cmds := strings.Split(flds[0], ",")

	flds[1] = strings.Replace(flds[1], "[", "", -1)
	flds[1] = strings.Replace(flds[1], "]", "", -1)
	argvals := strings.Split(flds[1], ",")

//	fmt.Printf("cmds[] = %s\n", cmds)
//	fmt.Printf("argvals[] = %s\n", argvals)
	fmt.Printf("cmds[] = [%s]\n", StringArrayToString(cmds))
	fmt.Printf("argvals[] = [%s]\n", StringArrayToString(argvals))

	timeStart := time.Now()

	calc(cmds, argvals)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
