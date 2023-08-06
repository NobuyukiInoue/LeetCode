package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numberOfEmployeesWhoMetTarget(hours []int, target int) int {
	// 3ms - 6ms
	ans := 0
	for _, h := range hours {
		if h >= target {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	hours := StringToIntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])
	fmt.Printf("hours = [%s], target = %d\n", IntArrayToString(hours), target)

	timeStart := time.Now()

	result := numberOfEmployeesWhoMetTarget(hours, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
