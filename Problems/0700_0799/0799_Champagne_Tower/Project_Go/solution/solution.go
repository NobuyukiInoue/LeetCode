package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func champagneTower2(poured int, query_row int, query_glass int) float64 {
	// 0ms
	oldRow := make([]float64, 1)
	oldRow[0] = float64(poured)
	for i := 0; i < query_row; i++ {
		newRow := make([]float64, myIntMin(i+2, query_glass+1))
		for j := 0; j < len(oldRow)-1; j++ {
			if oldRow[j] > 1 {
				newRow[j] += (oldRow[j] - 1) / 2.0
				newRow[j+1] += (oldRow[j] - 1) / 2.0
			}
		}
		if oldRow[len(oldRow)-1] > 1 {
			newRow[len(newRow)-1] += (oldRow[len(oldRow)-1] - 1) / 2.0
			if len(oldRow) < len(newRow) {
				newRow[len(newRow)-2] += (oldRow[len(oldRow)-1] - 1) / 2.0
			}
		}
		oldRow = newRow
	}
	return myFloat64Min(oldRow[len(oldRow)-1], 1)
}

func champagneTower(poured int, query_row int, query_glass int) float64 {
	// 0ms
	res := make([]float64, query_row+2)
	res[0] = float64(poured)
	for row := 1; row <= query_row; row++ {
		for i := row; i >= 0; i-- {
			res[i] = myFloat64Max(0.0, (res[i]-1)/2)
			res[i+1] += res[i]
		}
	}
	return myFloat64Min(res[query_glass], 1.0)
}

func myIntMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func myFloat64Min(a float64, b float64) float64 {
	if a < b {
		return a
	}
	return b
}

func myFloat64Max(a float64, b float64) float64 {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	poured, _ := strconv.Atoi(flds[0])
	query_row, _ := strconv.Atoi(flds[1])
	query_glass, _ := strconv.Atoi(flds[2])
	fmt.Printf("poured = %d, query_row = %d, query_glass = %d\n", poured, query_row, query_glass)

	timeStart := time.Now()

	result := champagneTower(poured, query_row, query_glass)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
