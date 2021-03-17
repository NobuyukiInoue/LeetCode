package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func exclusiveTime(n int, logs []string) []int {
	// 8ms
	res := make([]int, n)
	stack := make([][]int, 0)
	for _, log := range logs {
		flds := strings.Split(log, ":")
		ID, _ := strconv.Atoi(flds[0])
		op := flds[1]
		time, _ := strconv.Atoi(flds[2])
		stackLen := len(stack)
		if op == "start" {
			if stackLen > 0 {
				res[stack[stackLen-1][0]] += time - stack[stackLen-1][1]
			}
			stack = append(stack, []int{ID, time})
		} else {
			prev := stack[stackLen-1]
			stack = stack[0 : stackLen-1]
			res[ID] += time - prev[1] + 1
			if len(stack) > 0 {
				stack[len(stack)-1][1] = time + 1
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	logs := strings.Split(flds[1], ",")
	fmt.Printf("n = %d\n", n)
	fmt.Printf("logs = %s\n", logs)

	timeStart := time.Now()

	result := exclusiveTime(n, logs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
