package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func areSimilar(mat [][]int, k int) bool {
	// 4ms
	n := len(mat[0])
	for _, row := range mat {
		for i := 0; i < n; i++ {
			if row[i] != row[(i+k)%n] {
				return false
			}
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	flds0 := strings.Split(flds[0], "],[")
	mat := make([][]int, len(flds0))
	for i, _ := range flds0 {
		mat[i] = StringToIntArray(flds0[i])
	}

	flds1 := strings.Replace(flds[1], "]]", "", -1)
	k, _ := strconv.Atoi(flds1)

	fmt.Printf("mat = %s, k = %d\n", IntIntArrayToString(mat), k)

	timeStart := time.Now()

	result := areSimilar(mat, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
