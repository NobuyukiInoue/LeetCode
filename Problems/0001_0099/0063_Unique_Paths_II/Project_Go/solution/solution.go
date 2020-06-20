package solution

import (
	"fmt"
	"strings"
	"time"
)

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	// 0ms
	if obstacleGrid == nil {
		return 0
	}

	m := len(obstacleGrid)
	n := len(obstacleGrid[0])
	obstacleGrid[0][0] = 1 - obstacleGrid[0][0]

	for i := 1; i < n; i++ {
		if obstacleGrid[0][i] == 0 {
			obstacleGrid[0][i] = obstacleGrid[0][i-1]
		} else {
			obstacleGrid[0][i] = 0
		}
	}

	for i := 1; i < m; i++ {
		if obstacleGrid[i][0] == 0 {
			obstacleGrid[i][0] = obstacleGrid[i-1][0]
		} else {
			obstacleGrid[i][0] = 0
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if obstacleGrid[i][j] == 0 {
				obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
			} else {
				obstacleGrid[i][j] = 0
			}
		}
	}
	return obstacleGrid[m-1][n-1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	obstacleGrid := make([][]int, len(flds))
	for i := 0; i < len(obstacleGrid); i++ {
		obstacleGrid[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("obstacleGrid = %s\n", IntIntArrayToGridString(obstacleGrid))

	timeStart := time.Now()

	result := uniquePathsWithObstacles(obstacleGrid)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
