package solution

import (
	"fmt"
	"strings"
	"time"
)

func findRepeatedDnaSequences(s string) []string {
	// 20ms
	ans := make([]string, 0)
	if len(s) < 10 {
		return ans
	}

	cache := make(map[string]int)
	for i := 0; i <= len(s)-10; i++ {
		curr := string(s[i : i+10])
		if cache[curr] == 1 {
			ans = append(ans, curr)
		}
		cache[curr] += 1
	}
	return ans
}

func findRepeatedDnaSequences2(s string) []string {
	// 20ms
	seen := make(map[string]int, 0)
	res := make(map[string]int, 0)
	for i := 0; i < len(s)-9; i++ {
		subStr := s[i : i+10]
		_, exists := seen[subStr]
		if exists {
			res[subStr] = 1
			seen[subStr]++
		} else {
			seen[subStr] = 1
		}
	}

	resultArray := make([]string, 0)
	for k, _ := range res {
		resultArray = append(resultArray, k)
	}

	return resultArray
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = [%s]\n", s)
	timeStart := time.Now()

	result := findRepeatedDnaSequences(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
