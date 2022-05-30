package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func digitCount(num string) bool {
	// 0ms
	var cnt [10]int
	for _, n := range num {
		cnt[n-'0']++
	}
	for i, _ := range num {
		if cnt[i] != int(num[i]-'0') {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	num := strings.Replace(temp, "]", "", -1)
	fmt.Printf("num = %s\n", num)

	timeStart := time.Now()

	result := digitCount(num)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
