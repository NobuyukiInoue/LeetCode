package solution

import (
	"fmt"
	"strings"
	"time"
)

func countPoints(rings string) int {
	// 0ms
	var rods [10]map[byte]int
	for i := 0; i < 10; i++ {
		rods[i] = map[byte]int{}
	}
	for i := 0; i < len(rings); i += 2 {
		rods[rings[i+1]-'0'][rings[i]] = 1
	}
	ans := 0
	for i := 0; i < 10; i++ {
		if len(rods[i]) == 3 {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	rings := strings.Replace(temp, "]", "", -1)
	fmt.Printf("rings = %s\n", rings)

	timeStart := time.Now()

	result := countPoints(rings)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
