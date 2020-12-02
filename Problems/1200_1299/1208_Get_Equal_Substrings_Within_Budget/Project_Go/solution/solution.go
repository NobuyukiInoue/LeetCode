package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func equalSubstring(s string, t string, maxCost int) int {
	// 0ms
	i, j := 0, 0
	sLength := len(s)
	for j = 0; j < sLength; j++ {
		maxCost -= myAbs(int(s[j]) - int(t[j]))
		if maxCost < 0 {
			maxCost += myAbs(int(s[i]) - int(t[i]))
			i++
		}
	}
	return j - i
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := flds[0]
	t := flds[1]
	maxCost, _ := strconv.Atoi(flds[2])
	fmt.Printf("s = %s, t = %s, maxCost = %d\n", s, t, maxCost)

	timeStart := time.Now()

	result := equalSubstring(s, t, maxCost)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
