package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func randomizeset(cmds []string, args [][]int) []string {
	createdRandomizeset := false

	obj := Constructor()
	var res []string

	for i, cmd := range cmds {
		if cmd == "RandomizedSet" {
			createdRandomizeset = true
			res = append(res, "nil")
			fmt.Printf("RandomizedSet() ... %s\n", res[len(res)-1])
		} else {
			if !createdRandomizeset {
				fmt.Printf("Solution was not created.\n")
				os.Exit(1)
			}
			if cmd == "insert" {
				res = append(res, strconv.FormatBool(obj.Insert(args[i][0])))
				fmt.Printf("Insert(%d) ... %s\n", args[i][0], res[len(res)-1])
			} else if cmd == "remove" {
				res = append(res, strconv.FormatBool(obj.Remove(args[i][0])))
				fmt.Printf("Remove(%d) ... %s\n", args[i][0], res[len(res)-1])
			} else if cmd == "getRandom" {
				res = append(res, strconv.Itoa(obj.GetRandom()))
				fmt.Printf("GetRandome() ... %s\n", res[len(res)-1])
			} else {
				res = append(res, "error")
				fmt.Printf("cmds[%s] is not define.\n", cmds[i])
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
		if argstr[i] != "" {
			temp := strings.Replace(argstr[i], "[", "", -1)
			temp = strings.Replace(temp, "]", "", -1)
			temp_val, _ := strconv.Atoi(temp)
			args[i] = []int{temp_val}
		}
	}
	fmt.Printf("cmds[] = %s\n", cmds)
	fmt.Printf("arg[] = %s\n", IntIntArrayToString(args))

	timeStart := time.Now()

	res := randomizeset(cmds, args)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
