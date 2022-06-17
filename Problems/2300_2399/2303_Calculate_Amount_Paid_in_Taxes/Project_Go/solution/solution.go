package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func calculateTax(brackets [][]int, income int) float64 {
	// 7ms
	tax, prev := 0.0, 0
	for _, bracket := range brackets {
		if income >= bracket[0] {
			tax += float64((bracket[0]-prev)*bracket[1]) / 100.0
			prev = bracket[0]
		} else {
			tax += float64((income-prev)*bracket[1]) / 100.0
			return tax
		}
	}
	return tax
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	flds0 := strings.Split(flds[0], "],[")
	flds1 := strings.Replace(flds[1], "]", "", -1)
	brackets := make([][]int, len(flds0))
	for i := 0; i < len(flds0); i++ {
		brackets[i] = StringToIntArray(flds0[i])
	}
	income, _ := strconv.Atoi(flds1)
	fmt.Printf("brackets = [%s], income = %d\n", IntIntArrayToString(brackets), income)

	timeStart := time.Now()

	result := calculateTax(brackets, income)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
