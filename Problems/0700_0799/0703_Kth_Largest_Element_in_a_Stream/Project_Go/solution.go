package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func calc(cmds []string, argvals []string) {
	flds := strings.Split(strings.Replace(argvals[0], "]", "", -1), ",[")
	k, _ := strconv.Atoi(flds[0])
	var nums []int
	if len(flds) < 2 {
		nums = make([]int, 0)
	} else {
		if flds[1] == "" {
			nums = make([]int, 0)
		} else {
			numsStr := strings.Split(flds[1], ",")
			nums = make([]int, len(numsStr))
			for i, _ := range numsStr {
				nums[i], _ = strconv.Atoi(numsStr[i])
			}
		}
	}

	obj := Constructor(k, nums)
	createdKthLargest := false

	for i, cmd := range cmds {
		if cmd == "KthLargest" {
			createdKthLargest = true
		} else {
			if createdKthLargest != true {
				fmt.Printf("KthLargest was not created.\n")
				os.Exit(1)
			}

			val, _ := strconv.Atoi(argvals[i])

			if cmd == "add" {
				result := obj.Add(val)
				fmt.Printf("Add(%d) ... %d\n", val, result)
			}
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)

	flds := strings.Split(temp, "],[[")

	cmds := strings.Split(strings.Replace(flds[0], "[[", "", -1), ",")
	argvals := strings.Split(flds[1], "],[")

	fmt.Printf("cmds[] = %s\n", cmds)
	fmt.Printf("argvals[] = %s\n", argvals)

	timeStart := time.Now()

	calc(cmds, argvals)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
