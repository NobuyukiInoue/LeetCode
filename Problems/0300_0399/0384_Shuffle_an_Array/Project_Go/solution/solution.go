package solution

import (
	"fmt"
	"os"
	"strings"
	"time"
)

func solution2(cmds []string, args [][]int) [][]int {
	createdSolution := false

	obj := Constructor(args[0])
	var res [][]int

	for i, cmd := range cmds {
		if cmd == "Solution" {
			createdSolution = true
			res = append(res, args[i])
			fmt.Printf("Solution() ... [%s]\n", IntArrayToString(res[len(res)-1]))
		} else {
			if !createdSolution {
				fmt.Printf("Solution was not created.\n")
				os.Exit(1)
			}
			if cmd == "reset" {
				res = append(res, obj.Reset())
				fmt.Printf("reset()    ... [%s]\n", IntArrayToString(res[len(res)-1]))
			} else if cmd == "shuffle" {
				res = append(res, obj.Shuffle())
				fmt.Printf("shuffle()  ... [%s]\n", IntArrayToString(res[len(res)-1]))
			}
		}
	}
	return res
}

func LoopMain(v_args string) {
	temp := strings.Trim(v_args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)

	flds := strings.Split(temp, "],[[")
	cmds := strings.Split(strings.Replace(flds[0], "[[", "", -1), ",")
	argtemp := strings.Replace(flds[1], "]]]", "", -1)
	argstr := strings.Split(argtemp, "],[")

	args := make([][]int, len(cmds))
	for i := 0; i < len(argstr); i++ {
		temp := strings.Replace(argstr[i], "[", "", -1)
		temp = strings.Replace(temp, "]", "", -1)
		args[i] = StringToIntArray(temp)
	}
	fmt.Printf("cmds[] = %s\n", cmds)
	fmt.Printf("arg[] = %s\n", IntIntArrayToString(args))

	timeStart := time.Now()

	res := solution2(cmds, args)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", IntIntArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
