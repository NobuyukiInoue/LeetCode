package solution

import (
	"fmt"
	"strings"
	"time"
)

func averageWaitingTime(customers [][]int) float64 {
	// 228ms
	wait, cur := 0, 0
	for _, customer := range(customers) {
		if cur > customer[0] {
			cur += customer[1]
		} else {
			cur = customer[0] + customer[1]
		}
		wait += cur - customer[0]
	}
	return float64(wait)/float64(len(customers))
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	customers := make([][]int, len(flds))
	for i := 0; i < len(customers); i++ {
		customers[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("customers = %s\n", IntIntArrayToString(customers))

	timeStart := time.Now()

	result := averageWaitingTime(customers)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
