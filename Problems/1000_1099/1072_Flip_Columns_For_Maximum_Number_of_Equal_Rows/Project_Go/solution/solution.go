package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxEqualRowsAfterFlips(matrix [][]int) int {
	// 348ms
	myMap := map[string]int{}

	for _, row := range matrix {
		str1 := ""
		str2 := ""
		for _, col := range row {
			str1 += string(col)
			str2 += string(1 - col)
		}
		myMap[str1]++
		myMap[str2]++
	}

	res := 0
	for _, v := range myMap {
		res = myMax(res, v)
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
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	matrix := make([][]int, len(flds))
	for i := 0; i < len(matrix); i++ {
		matrix[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("matrix = %s\n", IntIntArrayToString(matrix))

	timeStart := time.Now()

	result := maxEqualRowsAfterFlips(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
