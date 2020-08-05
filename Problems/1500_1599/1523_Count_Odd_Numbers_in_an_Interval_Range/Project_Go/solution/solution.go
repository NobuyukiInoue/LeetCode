package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countOdds(low int, high int) int {
	// 0ms
	return (high+1)/2 - low/2
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	low, _ := strconv.Atoi(flds[0])
	high, _ := strconv.Atoi(flds[1])

	timeStart := time.Now()

	result := countOdds(low, high)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
