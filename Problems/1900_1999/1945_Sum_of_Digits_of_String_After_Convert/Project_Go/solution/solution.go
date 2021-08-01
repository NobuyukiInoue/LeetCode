package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getLucky(s string, k int) int {
	// 2ms
	workStr := ""
	for _, ch := range s {
		workStr += strconv.Itoa(int(ch - 'a' + 1))
	}
	ans := 0
	for i := 0; i < k; i++ {
		ans = 0
		for _, ch := range workStr {
			ans += int(ch - '0')
		}
		workStr = strconv.Itoa(ans)
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("s = \"%s\", k = %d\n", s, k)

	timeStart := time.Now()

	result := getLucky(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
