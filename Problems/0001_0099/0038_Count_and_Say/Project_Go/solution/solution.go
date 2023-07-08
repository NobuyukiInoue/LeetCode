package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countAndSay(n int) string {
	// 5ms - 15ms
	if n == 1 {
		return "1"
	}
	res := countAndSay(n - 1)
	ans, left, right := "", 0, 0
	for right < len(res) {
		counter := 0
		for right < len(res) && res[left] == res[right] {
			counter++
			right++
		}
		ans += strconv.Itoa(counter) + string(res[left])
		left = right
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := countAndSay(n)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
