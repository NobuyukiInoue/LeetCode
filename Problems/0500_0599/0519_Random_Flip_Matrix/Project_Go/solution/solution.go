package solution

import (
	"fmt"
	"os"
	"strings"
	"time"
)

func execRandomFlipMatrix(cmds []string, args [][]int) []string {
	createdRandomFlipMatrix := false
	obj := Constructor(args[0][0], args[0][1])
	var res []string

	for _, cmd := range cmds {
		if cmd == "Solution" {
			createdRandomFlipMatrix = true
			res = append(res, "null")
		} else {
			if createdRandomFlipMatrix != true {
				fmt.Printf("createdRandomFlipMatrix was not created.\n")
				os.Exit(1)
			} else if cmd == "flip" {
				res = append(res, IntArrayToString(obj.Flip()))
				fmt.Printf("flip() ... [%s]\n", res[len(res)-1])
			} else if cmd == "reset" {
				obj.Reset()
				res = append(res, "null")
				fmt.Printf("reset() ... %s\n", res[len(res)-1])
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

	res := execRandomFlipMatrix(cmds, args)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
