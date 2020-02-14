package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

var days = []string{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}

func dayOfTheWeek(day int, month int, year int) string {
	// 0ms
	if month < 3 {
		month += 12
		year -= 1
	}
	c := year / 100
	year = year % 100
	w := (c/4 - 2*c + year + year/4 + 13*(month+1)/5 + day - 1) % 7
	return days[(w+7)%7]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	day, _ := strconv.Atoi(flds[0])
	month, _ := strconv.Atoi(flds[1])
	year, _ := strconv.Atoi(flds[2])

	fmt.Printf("day = %d, month = %d, year = %d\n", day, month, year)
	timeStart := time.Now()

	result := dayOfTheWeek(day, month, year)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
