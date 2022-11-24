package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execExamRoom(cmds []string, args []string) []string {
	n, _ := strconv.Atoi(args[0])
	examRoom := Constructor(n)
	createdExamRoom := false
	var res []string

	for i, cmd := range cmds {
		if cmd == "ExamRoom" {
			createdExamRoom = true

		} else {
			if !createdExamRoom {
				fmt.Printf("ExamRoom was not created.\n")
				os.Exit(1)
			}

			if cmd == "seat" {
				result := examRoom.Seat()
				fmt.Printf("seat()    ... %d\n", result)
				res = append(res, strconv.Itoa(result))

			} else if cmd == "leave" {
				val, _ := strconv.Atoi(args[i])
				examRoom.Leave(val)
				fmt.Printf("leave(%s) ... null\n", args[i])
				res = append(res, "null")
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)

	flds := strings.Split(temp, "],[[")

	flds[0] = strings.Replace(flds[0], "[[", "", -1)
	cmds := strings.Split(flds[0], ",")

	flds[1] = strings.Replace(flds[1], "]]]", "", -1)
	vals := strings.Split(flds[1], "],[")

	fmt.Printf("cmds[] = [%s]\n", StringArrayToString(cmds))
	fmt.Printf("vals[] = [%s]\n", StringArrayToString(vals))

	timeStart := time.Now()

	execExamRoom(cmds, vals)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
