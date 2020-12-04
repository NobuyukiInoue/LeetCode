package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execOrderedStream(cmds []string, argstr []string) [][]string {
	createdOrderedStream := false

	n, _ := strconv.Atoi(argstr[0])
	obj := Constructor(n)
	var res [][]string

	for i, cmd := range cmds {
		if cmd == "OrderedStream" {
			createdOrderedStream = true
			res = append(res, []string{"null"})
		} else {
			if createdOrderedStream != true {
				fmt.Printf("OrderedStream was not created.\n")
				os.Exit(1)
			}
			if cmd == "insert" {
				flds := strings.Split(argstr[i], ",")
				id, _ := strconv.Atoi(flds[0])
				value := flds[1]
				res = append(res, obj.Insert(id, value))
				fmt.Printf("insert(%d, %s) ... %s\n", id, value, res[len(res) - 1])
			}
		}
	}
	return res
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

	res := execOrderedStream(cmds, argstr)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", StringStringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
