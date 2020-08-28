package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func combinationSum3(k int, n int) [][]int {
	// 0ms
	results := [][]int{}
	curElem := []int{}
	combinationSum(k, n, 1, &curElem, &results)
	return results
}

func combinationSum(k int, n int, start int, curElem *[]int, results *[][]int) {
	if n == 0 && len(*curElem) == k {
		*results = append(*results, append([]int{}, *curElem...))
	}

	for i := start; i <= 9; i++ {
		*curElem = append(*curElem, i)
		combinationSum(k, n-i, i+1, curElem, results)
		*curElem = (*curElem)[:len(*curElem)-1]
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	k, _ := strconv.Atoi(flds[0])
	n, _ := strconv.Atoi(flds[1])

	timeStart := time.Now()

	result := combinationSum3(k, n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
