package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func haveConflict(event1 []string, event2 []string) bool {
	// 0ms
	return event1[0] <= event2[1] && event2[0] <= event1[1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	event1 := strings.Split(flds[0], ",")
	event2 := strings.Split(flds[1], ",")
	fmt.Printf("event1 = %s, event2 = %s\n", event1, event2)

	timeStart := time.Now()

	result := haveConflict(event1, event2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
