package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func halvesAreAlike(s string) bool {
	// 0ms
	vowls := "aeiouAEIOU"
	mid := len(s) / 2
	cnt := 0
	for i := 0; i < mid; i++ {
		for j, _ := range vowls {
			if s[i] == vowls[j] {
				cnt++
			}
		}
	}
	for i := mid; i < len(s); i++ {
		for j, _ := range vowls {
			if s[i] == vowls[j] {
				cnt--
			}
		}
	}
	return cnt == 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := halvesAreAlike(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
