package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getRow(rowIndex int) []int {
	result := make([][]int, rowIndex+1)
	for i := 0; i < rowIndex+1; i++ {
		result[i] = make([]int, i+1)
		for j := 0; j < i+1; j++ {
			if j == 0 || j == i {
				result[i][j] = 1
			} else {
				result[i][j] = result[i-1][j-1] + result[i-1][j]
			}
		}
	}
	return result[rowIndex]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	rowIndex, _ := strconv.Atoi(flds)
	fmt.Printf("rowIndex = %d\n", rowIndex)

	timeStart := time.Now()

	result := getRow(rowIndex)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
