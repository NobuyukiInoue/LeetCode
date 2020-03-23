package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func daysBetweenDates(date1 string, date2 string) int {
	// 0ms
	time1, _ := time.Parse("2006-01-02", date1)
	time2, _ := time.Parse("2006-01-02", date2)
	return int(math.Abs(time2.Sub(time1).Hours() / 24.0))
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	date1, date2 := flds[0], flds[1]

	fmt.Printf("date1 = %s, date2 = %s\n", date1, date2)
	timeStart := time.Now()

	result := daysBetweenDates(date1, date2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
