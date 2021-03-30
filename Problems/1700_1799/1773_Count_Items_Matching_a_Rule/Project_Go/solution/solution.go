package solution

import (
	"fmt"
	"strings"
	"time"
)

func countMatches(items [][]string, ruleKey string, ruleValue string) int {
	// 32ms
	res, col := 0, 0
	switch ruleKey {
	case "type":
		col = 0
		break
	case "color":
		col = 1
		break
	case "name":
		col = 2
		break
	}

	for _, item := range(items) {
		if ruleValue == item[col] {
			res++
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	flds0 := strings.Split(flds[0], "],[")
	items := make([][]string, len(flds0))
	for i := 0; i < len(flds0); i++ {
		items[i] = strings.Split(flds0[i], ",")
	}
	fmt.Printf("items = %s\n", items)

	flds1 := strings.Split(strings.Replace(flds[1], "]]", "", -1), "],[")
	ruleKey, ruleValue := flds1[0], flds1[1]
	fmt.Printf("ruleKey = %s, ruleValue = %s\n", ruleKey, ruleValue)

	timeStart := time.Now()

	result := countMatches(items, ruleKey, ruleValue)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
