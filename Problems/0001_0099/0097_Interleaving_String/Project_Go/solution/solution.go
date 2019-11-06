package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isInterleave(s1 string, s2 string, s3 string) bool {
	// 0ms
	if len(s1) == 0 && len(s2) == 0 && len(s3) == 0 {
		return true
	}
	if len(s3) != len(s1)+len(s2) {
		return false
	}

	dp := make([][]bool, len(s1)+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]bool, len(s2)+1)
	}

	dp[0][0] = true
	for i := 1; i <= len(s1); i++ {
		if s3[i-1] == s1[i-1] {
			dp[i][0] = true
		} else {
			break
		}
	}
	for j := 1; j <= len(s2); j++ {
		if s3[j-1] == s2[j-1] {
			dp[0][j] = true
		} else {
			break
		}
	}
	for i := 1; i <= len(s1); i++ {
		for j := 1; j <= len(s2); j++ {
			if s3[i+j-1] == s1[i-1] {
				dp[i][j] = dp[i-1][j] || dp[i][j]
			}
			if s3[i+j-1] == s2[j-1] {
				dp[i][j] = dp[i][j-1] || dp[i][j]
			}
		}
	}

	return dp[len(s1)][len(s2)]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	s1 := flds[0]
	s2 := flds[1]
	s3 := flds[2]

	fmt.Printf("s1 = %s, s2 = %s, s3 = %s\n", s1, s2, s3)
	timeStart := time.Now()

	result := isInterleave(s1, s2, s3)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
