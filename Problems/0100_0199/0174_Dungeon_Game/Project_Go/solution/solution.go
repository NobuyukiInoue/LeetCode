package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func calculateMinimumHP(dungeon [][]int) int {
	// 4ms
	m := len(dungeon)
	n := len(dungeon[0])
	dp := make([][]int, m+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, n+1)
		for j := 0; j < len(dp[i]); j++ {
			dp[i][j] = math.MaxInt64
		}
	}

	dp[m][n-1], dp[m-1][n] = 1, 1
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			minHp := myMin(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
			if minHp <= 0 {
				dp[i][j] = 1
			} else {
				dp[i][j] = minHp
			}
		}
	}
	return dp[0][0]
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)
	dungeon_str := strings.Split(flds, "],[")

	dungeon := make([][]int, len(dungeon_str))
	for i := 0; i < len(dungeon_str); i++ {
		dungeon[i] = StringToIntArray(dungeon_str[i])
	}

	fmt.Printf("dungeon = %s\n", IntIntArrayToString(dungeon))
	timeStart := time.Now()

	result := calculateMinimumHP(dungeon)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
