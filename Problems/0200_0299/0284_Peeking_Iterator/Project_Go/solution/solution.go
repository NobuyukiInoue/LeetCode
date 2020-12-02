package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execPeekingIterator(cmds []string, argstr []string) []string {
	createdPeekingIterator := false

	arg0 := strings.Replace(argstr[0], "[", "", -1)
	arg0 = strings.Replace(arg0, "]", "", -1)
	flds := StringToIntArray(arg0)
	obj := Constructor(&Iterator{flds, 0})
	var res []string

	for _, cmd := range cmds {
		if cmd == "PeekingIterator" {
			createdPeekingIterator = true
			res = append(res, "null")
		} else {
			if createdPeekingIterator != true {
				fmt.Printf("PeekingIterator was not created.\n")
				os.Exit(1)
			}
			if cmd == "peek" {
				temp := strconv.Itoa(obj.peek())
				res = append(res, temp)
				fmt.Printf("peek() ... %s\n", res[len(res)-1])
			}
			if cmd == "next" {
				temp := strconv.Itoa(obj.next())
				res = append(res, temp)
				fmt.Printf("next() ... %s\n", res[len(res)-1])
			}
			if cmd == "hasNext" {
				res = append(res, strconv.FormatBool(obj.hasNext()))
				fmt.Printf("addCar() ... %s\n", res[len(res)-1])
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
	argtemp := strings.Replace(flds[1], "]]]]", "", -1)
	argstr := strings.Split(argtemp, "],[")

	fmt.Printf("cmds[] = %s\n", cmds)
	fmt.Printf("argstr[] = %s\n", StringArrayToString(argstr))

	timeStart := time.Now()

	res := execPeekingIterator(cmds, argstr)

	timeEnd := time.Now()
	fmt.Printf("res =  [%s]\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
