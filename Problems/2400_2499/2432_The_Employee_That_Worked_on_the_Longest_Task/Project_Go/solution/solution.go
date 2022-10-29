package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hardestWorker(n int, logs [][]int) int {
	// 37ms - 94ms
	best_id, best_time, start_time := 0, 0, 0
	for _, log := range logs {
		time := log[1] - start_time
		if time > best_time || (time == best_time && best_id > log[0]) {
			best_id = log[0]
			best_time = time
		}
		start_time = log[1]
	}
	return best_id
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "],[[")

	n, _ := strconv.Atoi(strings.Replace(flds[0], "[[", "", -1))

	flds1 := strings.Split(flds[1], "],[")
	logs := make([][]int, len(flds1))
	for i, _ := range flds1 {
		logs[i] = StringToIntArray(flds1[i])
	}

	fmt.Printf("n = %d, logs = [%s]\n", n, IntIntArrayToString(logs))

	timeStart := time.Now()

	result := hardestWorker(n, logs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
