package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumPopulation(logs [][]int) int {
	// 0ms
	var popChange [2050 - 1950 + 1]int
	for i := 0; i < len(logs); i++ {
		popChange[logs[i][0]-1950]++
		popChange[logs[i][1]-1950]--
	}

	maxPop, besti, lastiPop := -1, -1, 0
	for i := 0; i < len(popChange); i++ {
		currentiPop := lastiPop + popChange[i]
		if currentiPop > maxPop {
			maxPop = currentiPop
			besti = 1950 + i
		}
		lastiPop = currentiPop
	}
	return besti
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	logs := make([][]int, len(flds))
	for i := 0; i < len(logs); i++ {
		logs[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("logs = %s\n", IntIntArrayToString(logs))

	timeStart := time.Now()

	result := maximumPopulation(logs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
