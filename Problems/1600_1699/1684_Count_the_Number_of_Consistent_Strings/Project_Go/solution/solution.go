package solution

import (
	"fmt"
	"strings"
	"time"
)

func countConsistentStrings(allowed string, words []string) int {
	// 32ms
	myMap := make(map[rune]bool, 26)
	count := 0

	for _, ch := range allowed {
		myMap[ch-'a'] = true
	}
	for _, word := range words {
		isConsistent := true
		for _, ch := range word {
			if myMap[ch-'a'] == false {
				isConsistent = false
				break
			}
		}
		if isConsistent == true {
			count++
		}
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	allowed := flds[0]
	words := strings.Split(flds[1], ",")
	fmt.Printf("allowed = %s\n", allowed)
	fmt.Printf("words = %s\n", words)

	timeStart := time.Now()

	result := countConsistentStrings(allowed, words)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
