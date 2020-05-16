package solution

import (
	"fmt"
	"strings"
	"time"
)

func numDistinct(s string, t string) int {
	// 0ms
	arr := make([][]int, 256)
	for i := 0; i < len(arr); i++ {
		arr[i] = make([]int, len(t)+1)
	}

	cnt := make([]int, len(t)+1)
	cnt[0] = 1
	for i := 0; i < len(t); i++ {
		c := t[i]
		arr[c][arr[c][0]+1] = i + 1
		arr[c][0]++
	}
	for i := 0; i < len(s); i++ {
		if arr[s[i]][0] != 0 {
			for j := arr[s[i]][0]; j > 0; j-- {
				cnt[arr[s[i]][j]] += cnt[arr[s[i]][j]-1]
			}
		}
	}
	return cnt[len(t)]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	words := strings.Split(temp, "],[")
	s, t := words[0], words[1]
	fmt.Printf("s = %s, t = %s\n", s, t)

	timeStart := time.Now()

	result := numDistinct(s, t)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
