package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func closetTarget(words []string, target string, startIndex int) int {
	// 4ms - 14ms
	n := len(words)
	ans := math.MaxInt64
	for i, _ := range words {
		if words[i] == target {
			dist := myAbs(i - startIndex)
			oppDist := n - dist
			ans = myMin(ans, myMin(dist, oppDist))
		}
	}
	if ans == math.MaxInt64 {
		return -1
	}
	return ans
}

func myAbs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	words := strings.Split(flds[0], ",")
	target := flds[1]
	startIndex, _ := strconv.Atoi(flds[2])
	fmt.Printf("words = %s, target = %s, startIndex = %d\n", StringArrayToString(words), target, startIndex)

	timeStart := time.Now()

	result := closetTarget(words, target, startIndex)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
