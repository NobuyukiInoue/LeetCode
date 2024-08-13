package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execNeighborSum(cmds []string, argstr []string) []string {
	createdNeighborSum := false
	args0str := strings.Split(argstr[0], "],[")
	args0 := make([][]int, len(args0str))
	for i := 0; i < len(args0str); i++ {
		args0[i] = StringToIntArray(args0str[i])
	}

	obj := Constructor(args0)
	var res []string

	for i, cmd := range cmds {
		if cmd == "NeighborSum" {
			createdNeighborSum = true
			res = append(res, "null")
		} else {
			if createdNeighborSum != true {
				fmt.Printf("NeighborSum was not created.\n")
				os.Exit(1)
			} else if cmd == "adjacentSum" {
				value, _ := strconv.Atoi(argstr[i])
				res = append(res, strconv.Itoa(obj.AdjacentSum(value)))
				fmt.Printf("adjacentSum(%s) ... %s\n", argstr[i], res[len(res)-1])
			} else if cmd == "diagonalSum" {
				value, _ := strconv.Atoi(argstr[i])
				res = append(res, strconv.Itoa(obj.DiagonalSum(value)))
				fmt.Printf("diagonalSum(%s) ... %s\n", argstr[i], res[len(res)-1])
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	flds := strings.Split(temp, "],[[[[")

	flds0 := strings.Replace(flds[0], "[", "", -1)
	flds0 = strings.Replace(flds0, "]", "", -1)
	cmds := strings.Split(flds0, ",")

	argstr := make([]string, len(cmds))

	flds1 := strings.Replace(flds[1], "[[", "", -1)
	flds1 = strings.Replace(flds1, "]]]]", "", -1)
	flds11 := strings.Split(flds1, "]]],[")
	argstr[0] = flds11[0]
	flds12 := strings.Split(flds11[1], "],[")
	for i := 1; i < len(argstr); i++ {
		argstr[i] = flds12[i-1]
	}

	fmt.Printf("cmds[] = %s\n", cmds)
	fmt.Printf("argstr[] = %s\n", StringArrayToString(argstr))

	timeStart := time.Now()

	res := execNeighborSum(cmds, argstr)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
