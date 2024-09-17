package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func convertDateToBinary(date string) string {
	// 0ms
	flds := strings.Split(date, "-")
	ans := make([]string, len(flds))
	for i, fld := range flds {
		num, _ := strconv.Atoi(fld)
		ans[i] = strconv.FormatInt(int64(num), 2)
	}
	return strings.Join(ans, "-")
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	date := strings.Replace(temp, "]", "", -1)
	fmt.Printf("date = \"%s\"\n", date)

	timeStart := time.Now()

	result := convertDateToBinary(date)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
