package solution

import (
	"fmt"
	"strings"
	"time"
)

func partitionLabels(S string) []int {
	// 0ms
	res := make([]int, 0)

	rightMostPos := make([]int, 26)
	for i := 0; i < len(rightMostPos); i++ {
		rightMostPos[i] = -1
	}
	for i := 0; i < len(S); i++ {
		rightMostPos[S[i]-'a'] = i
	}

	currRight, count := -1, 0
	for i := 0; i < len(S); i++ {
		count++
		currRight = myMax(currRight, rightMostPos[S[i]-'a'])
		if i == currRight {
			res = append(res, count)
			count = 0
		}
	}

	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	S := strings.Replace(temp, "]", "", -1)
	fmt.Printf("S = %s\n", S)

	timeStart := time.Now()

	result := partitionLabels(S)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
