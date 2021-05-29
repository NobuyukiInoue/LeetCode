package solution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func execLRUCache(cmds []string, argstr []string) []string {
	createdLRUCache := false
	flds0, _ := strconv.Atoi(argstr[0])
	obj := Constructor(flds0)
	var res []string

	for i, cmd := range cmds {
		if cmd == "LRUCache" {
			createdLRUCache = true
			res = append(res, "null")
		} else {
			if createdLRUCache != true {
				fmt.Printf("LRUCache was not created.\n")
				os.Exit(1)
			}
			if cmd == "put" {
				flds := StringToIntArray(argstr[i])
				obj.Put(flds[0], flds[1])
				res = append(res, "null")
				fmt.Printf("put(%d, %d)\n", flds[0], flds[1])
			} else if cmd == "get" {
				flds := StringToIntArray(argstr[i])
				temp := obj.Get(flds[0])
				res = append(res, strconv.Itoa(temp))
				fmt.Printf("get(%d) ... %d\n", flds[0], temp)
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

	res := execLRUCache(cmds, argstr)

	timeEnd := time.Now()
	fmt.Printf("res =  %s\n", StringArrayToString(res))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
