package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execParkingSystem(cmds []string, argstr []string) []string {
	createdParkingSystem := false

	flds := StringToIntArray(argstr[0])
	obj := Constructor(flds[0], flds[1], flds[2])
	var res []string

	for i, cmd := range cmds {
		if cmd == "ParkingSystem" {
			createdParkingSystem = true
			res = append(res, "null")
		} else {
			if createdParkingSystem != true {
				fmt.Printf("ParkingSystem was not created.\n")
				os.Exit(1)
			}
			if cmd == "addCar" {
				value, _ := strconv.Atoi(argstr[i])
				res = append(res, strconv.FormatBool(obj.AddCar(value)))
				fmt.Printf("addCar(%d) ... %s\n", value, res[len(res) - 1])
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

	res := execParkingSystem(cmds, argstr)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
