package solution

import (
	"fmt"
	"strings"
	"time"
)

func findMinimumOperations(s1 string, s2 string, s3 string) int {
	// 0ms
	min_length := myMin(myMin(len(s1), len(s2)), len(s3))
	total_length := len(s1) + len(s2) + len(s3)
	if s1[0] != s2[0] || s2[0] != s3[0] || s3[0] != s1[0] {
		return -1
	}
	for i := 0; i < min_length; i++ {
		if s1[i] == s2[i] && s2[i] == s3[i] && s3[i] == s1[i] {
			total_length -= 3
		} else {
			break
		}
	}
	return total_length
}

func myMin(a, b int) int {
	if a <= b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	s1, s2, s3 := flds[0], flds[1], flds[2]
	fmt.Printf("s1 = %s, s2 = %s, s3 = %s\n", s1, s2, s3)

	timeStart := time.Now()

	result := findMinimumOperations(s1, s2, s3)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
