package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execStockSpanner(cmds []string, argstr []string) []string {
	createdStockSpanner := false

	obj := Constructor()
	var res []string

	for i, cmd := range cmds {
		if cmd == "StockSpanner" {
			createdStockSpanner = true
			res = append(res, "null")
		} else {
			if createdStockSpanner != true {
				fmt.Printf("StockSpanner was not created.\n")
				os.Exit(1)
			}
			if cmd == "next" {
				value, _ := strconv.Atoi(argstr[i])
				nextRes := strconv.Itoa(obj.Next(value))
				res = append(res, nextRes)
				fmt.Printf("next(%d) ... %s\n", value, nextRes)
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

	res := execStockSpanner(cmds, argstr)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
