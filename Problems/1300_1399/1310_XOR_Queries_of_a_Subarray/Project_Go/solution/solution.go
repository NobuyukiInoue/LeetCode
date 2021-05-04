package solution

import (
	"fmt"
	"strings"
	"time"
)

func xorQueries(arr []int, queries [][]int) []int {
	// 60ms
	xor := make([]int, len(arr)+1)
	for i, _ := range arr {
		xor[i+1] = xor[i] ^ arr[i]
	}

	res := make([]int, 0)
	for _, q := range queries {
		l, r := q[0], q[1]
		res = append(res, xor[l]^xor[r+1])
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "],[[")

	arr := StringToIntArray(strings.Replace(flds[0], "[[", "", -1))
	flds1 := strings.Split(flds[1], "],[")
	queries := make([][]int, len(flds1))
	for i := 0; i < len(queries); i++ {
		queries[i] = StringToIntArray(flds1[i])
	}
	fmt.Printf("arr = [%s], queries = %s\n", IntArrayToString(arr), IntIntArrayToString(queries))

	timeStart := time.Now()

	result := xorQueries(arr, queries)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
