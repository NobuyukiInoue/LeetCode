package solution

import (
	"fmt"
	"strings"
	"time"
)

func longestCommonPrefix(strs []string) string {
	// 0ms
	var res string
	if len(strs) == 0 {
		res = ""
	} else {
		res = strs[0]
	}
	for i := 1; i < len(strs); i++ {
		for strings.Index(strs[i], res) != 0 {
			res = res[0 : len(res)-1]
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	strs := strings.Split(temp, ",")

	fmt.Printf("strs = %s\n", strs)
	timeStart := time.Now()

	result := longestCommonPrefix(strs)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
