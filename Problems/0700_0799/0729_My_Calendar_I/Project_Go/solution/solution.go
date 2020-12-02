package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execMyCalendar(cmds []string, argstr []string) []string {
	createdMyCalendar := false

	obj := Constructor()
	var res []string

	for i, cmd := range cmds {
		if cmd == "MyCalendar" {
			createdMyCalendar = true
			res = append(res, "null")
		} else {
			if createdMyCalendar != true {
				fmt.Printf("MyCalendar was not created.\n")
				os.Exit(1)
			}
			if cmd == "book" {
				flds := StringToIntArray(argstr[i])
				res = append(res, strconv.FormatBool(obj.Book(flds[0], flds[1])))
				fmt.Printf("book(%d, %d) ... %s\n", flds[0], flds[1], res[len(res) - 1])
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

	res := execMyCalendar(cmds, argstr)

	timeEnd := time.Now()
	fmt.Printf("res =  [%s]\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
