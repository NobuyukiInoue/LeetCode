package solution

import (
	"fmt"
	"strings"
	"time"
)

func rowAndMaximumOnes(mat [][]int) []int {
	// 125ms - 131ms
	idx, max_count := 0, 0
	for i, _ := range mat {
		cnt := 0
		for j, _ := range mat[i] {
			if mat[i][j] == 1 {
				cnt++
			}
		}
		if cnt > max_count {
			idx, max_count = i, cnt
		}
	}
	return []int{idx, max_count}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	mat := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		mat[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("mat = %s\n", IntIntArrayToGridString(mat))

	timeStart := time.Now()

	result := rowAndMaximumOnes(mat)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
