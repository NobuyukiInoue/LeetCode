package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execCircularQueue(cmds []string, argstr []string) []string {
	createdCircularQueue := false

	num, _ := strconv.Atoi(argstr[0])
	obj := Constructor(num)
	var ans []string

	for i, cmd := range cmds {
		if cmd == "MyCircularQueue" {
			createdCircularQueue = true
			ans = append(ans, "null")
		} else {
			if createdCircularQueue != true {
				fmt.Printf("MyCircularQueue was not created.\n")
				os.Exit(1)
			} else if cmd == "enQueue" {
				num, _ := strconv.Atoi(argstr[i])
				res := obj.EnQueue(num)
				fmt.Printf("circlularQueue.enQueue(%s) ... %s\n", argstr[i], strconv.FormatBool(res))
				ans = append(ans, strconv.FormatBool(res))
			} else if cmd == "deQueue" {
				res := obj.DeQueue()
				fmt.Printf("circlularQueue.deQueue() ... %s\n", strconv.FormatBool(res))
				ans = append(ans, strconv.FormatBool(res))
			} else if cmd == "Front" {
				res := obj.Front()
				fmt.Printf("circlularQueue.Front() ... %d\n", res)
				ans = append(ans, strconv.Itoa(res))
			} else if cmd == "Rear" {
				res := obj.Rear()
				fmt.Printf("circlularQueue.Rear() ... %d\n", res)
				ans = append(ans, strconv.Itoa(res))
			} else if cmd == "isEmpty" {
				res := obj.IsEmpty()
				fmt.Printf("circlularQueue.isEmpty() ... %s\n", strconv.FormatBool(res))
				ans = append(ans, strconv.FormatBool(res))
			} else if cmd == "isFull" {
				res := obj.IsFull()
				fmt.Printf("circlularQueue.isFull() ... %s\n", strconv.FormatBool(res))
				ans = append(ans, strconv.FormatBool(res))
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)

	flds := strings.Split(temp, "],[[")
	cmds := strings.Split(strings.Replace(flds[0], "[[", "", -1), ",")
	argtemp := strings.Replace(flds[1], "]]]", "", -1)
	argstr := strings.Split(argtemp, "],[")

	fmt.Printf("cmds[] = %s\n", cmds)
	fmt.Printf("argstr[] = %s\n", StringArrayToString(argstr))

	timeStart := time.Now()

	res := execCircularQueue(cmds, argstr)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
