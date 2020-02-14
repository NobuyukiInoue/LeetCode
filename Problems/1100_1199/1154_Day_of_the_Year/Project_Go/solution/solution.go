package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func dayOfYear(date string) int {
	days := []int{0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365}
	flds := strings.Split(date, "-")
	year, _ := strconv.Atoi(flds[0])
	month, _ := strconv.Atoi(flds[1])
	day, _ := strconv.Atoi(flds[2])
	if month <= 2 {
		return days[month-1] + day
	} else {
		if !(year%100 == 0 && year%400 != 0) && year%4 == 0 {
			return days[month-1] + day + 1
		} else {
			return days[month-1] + day
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	date := strings.Replace(temp, "]", "", -1)

	fmt.Printf("date = %s\n", date)
	timeStart := time.Now()

	result := dayOfYear(date)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
