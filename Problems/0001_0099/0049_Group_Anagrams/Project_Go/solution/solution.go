package solution

import (
	"fmt"
	"strings"
	"time"
)

func groupAnagrams(strs []string) [][]string {
	// 16ms
	cache := make(map[[26]byte]int)
	result := make([][]string, 0)
	for i := range strs {
		list := [26]byte{}
		for j := range strs[i] {
			list[strs[i][j]-'a']++
		}
		if idx, ok := cache[list]; ok {
			result[idx] = append(result[idx], strs[i])
		} else {
			result = append(result, []string{strs[i]})
			cache[list] = len(result) - 1
		}
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	strs := strings.Split(temp, ",")

	fmt.Printf("strs = %s\n", strs)
	timeStart := time.Now()

	result := groupAnagrams(strs)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
