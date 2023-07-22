package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func theMaximumAchievableX(num int, t int) int {
	// 8ms
	return num + 2*t
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	num, _ := strconv.Atoi(flds[0])
	t, _ := strconv.Atoi(flds[1])
	fmt.Printf("num = %d, t = %d\n", num, t)

	timeStart := time.Now()

	result := theMaximumAchievableX(num, t)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
