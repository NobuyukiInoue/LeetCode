package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execRandomPickIndex(cmds []string, args [][]int) []string {
	createdRandomPickIndex := false
	obj := Constructor(args[0])
	var res []string

	for i, cmd := range cmds {
		if cmd == "Solution" {
			createdRandomPickIndex = true
			res = append(res, "null")
		} else {
			if createdRandomPickIndex != true {
				fmt.Printf("RandomPickIndex was not created.\n")
				os.Exit(1)
			}
			if cmd == "pick" {
				res = append(res, strconv.Itoa(obj.Pick(args[i][0])))
				fmt.Printf("pick(%d) ... %s\n", args[i][0], res[len(res) - 1])
			}
		}
	}
	return res
}

func LoopMain(arg string) {
	temp := strings.Trim(arg, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)

	flds := strings.Split(temp, "],[[")
	cmds := strings.Split(strings.Replace(flds[0], "[[", "", -1), ",")

	flds1 := strings.Replace(flds[1], "]]]", "", -1)
	argtemp := strings.Split(flds1, "],[")
	args := make([][]int, len(argtemp))
	for i := 0; i < len(args); i++ {
		fld := strings.Replace(argtemp[i], "[", "", -1)
		fld = strings.Replace(fld, "]", "", -1)
		args[i] = StringToIntArray(fld)
	}

	fmt.Printf("cmds[] = %s\n", cmds)
	fmt.Printf("args[] = %s\n", IntIntArrayToString(args))

	timeStart := time.Now()

	res := execRandomPickIndex(cmds, args)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
