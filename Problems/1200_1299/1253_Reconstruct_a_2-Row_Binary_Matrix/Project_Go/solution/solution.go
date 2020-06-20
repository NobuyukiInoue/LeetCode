package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func reconstructMatrix(upper int, lower int, colsum []int) [][]int {
	// 4796ms
	cols := len(colsum)
	data := make([][]int, 2)
	for i := 0; i < len(data); i++ {
		data[i] = make([]int, cols)
	}
	for i := 0; i < cols; i++ {
		if colsum[i] == 2 {
			data[0][i], data[1][i] = 1, 1
			upper--
			lower--
		} else if colsum[i] == 1 {
			if upper > lower {
				data[0][i] = 1
				upper--
			} else {
				data[1][i] = 1
				lower--
			}
		}
	}

	if upper != 0 || lower != 0 {
		return nil
	}
	return data
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, ",[")

	s := strings.Replace(flds[0], "[", "", -1)
	fld0 := strings.Split(s, ",")
	upper, _ := strconv.Atoi(fld0[0])
	lower, _ := strconv.Atoi(fld0[1])
	fmt.Printf("upper = %d, lower = %d\n", upper, lower)

	colsum := StringToIntArray(flds[1])
	fmt.Printf("colsum = [%s]\n", IntArrayToString(colsum))

	timeStart := time.Now()

	result := reconstructMatrix(upper, lower, colsum)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
