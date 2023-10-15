package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func lastVisitedIntegers(words []string) []int {
	// 3ms
	st, count, ans := make([]int, 0), 0, make([]int, 0)
	for _, word := range words {
		if word == "prev" {
			count++
			if count <= len(st) {
				ans = append(ans, st[len(st)-count])
			} else {
				ans = append(ans, -1)
			}
		} else {
			v, _ := strconv.Atoi(word)
			st = append(st, v)
			count = 0
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")
	fmt.Printf("words = [%s]\n", StringArrayToString(words))

	timeStart := time.Now()

	result := lastVisitedIntegers(words)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
