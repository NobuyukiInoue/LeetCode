package solution

import (
	"fmt"
	"strings"
	"time"
)

func longestCommonSubsequence(text1 string, text2 string) int {
	// 4ms
	len1, len2 := len(text1), len(text2)

	matrix := make([][]int, len1+1)
	for i := 0; i < len1+1; i++ {
		matrix[i] = make([]int, len2+1)
	}

	for i := 0; i < len1; i++ {
		for j := 0; j < len2; j++ {
			if text1[i] == text2[j] {
				matrix[i+1][j+1] = matrix[i][j] + 1
			} else {
				matrix[i+1][j+1] = myMax(matrix[i+1][j], matrix[i][j+1])
			}
		}
	}

	return matrix[len1][len2]
}

func myMax(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	text1 := flds[0]
	text2 := flds[1]

	fmt.Printf("text1 = %s, text2 = %s\n", text1, text2)
	timeStart := time.Now()

	result := longestCommonSubsequence(text1, text2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
