package solution

import (
	"fmt"
	"strings"
	"time"
)

func minCut(s string) int {
	// 8ms
	n := len(s)
	cut := make([]int, n)
	pal := make([][]bool, n)
	for i := 0; i < n; i++ {
		pal[i] = make([]bool, n)
		min := i
		for j := 0; j <= i; j++ {
			if s[j] == s[i] && (j+1 > i-1 || pal[j+1][i-1]) {
				pal[j][i] = true
				if j == 0 {
					min = 0
				} else {
					min = myMin(min, cut[j-1]+1)

				}
			}
		}
		cut[i] = min
	}
	return cut[n-1]
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := minCut(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
