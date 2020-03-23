package solution

import (
	"fmt"
	"strings"
	"time"
)

func sortString(s string) string {
	// 4ms
	ans := ""
	count := make([]int, 26)
	for _, ch := range s {
		count[ch-'a']++
	}

	for len(ans) < len(s) {
		add(count, &ans, true)
		add(count, &ans, false)
	}

	return ans
}

func add(count []int, ans *string, asc bool) {
	for i := 0; i < 26; i++ {
		var j int
		if asc {
			j = i
		} else {
			j = 25 - i
		}

		if count[j] > 0 {
			count[j]--
			*ans += (string)(j + 'a')
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = [%s]\n", s)
	timeStart := time.Now()

	result := sortString(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
