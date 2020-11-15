package solution

import (
	"fmt"
	"strings"
	"time"
)

func findLongestChain(pairs [][]int) int {
	// 28ms
	if pairs == nil {
		return 0
	}
	pairsLength := len(pairs)
	if pairsLength < 2 {
		return pairsLength
	}

	qsort(pairs, 0, pairsLength - 1)

	cur := pairs[0][1]
	res := 1

	for i := 1; i < pairsLength; i++ {
		if pairs[i][0] > cur {
			res++
			cur = pairs[i][1]
		}
	}
	return res
}

func qsort(pairs [][]int, begin int, end int) {
	if begin >= end {
		return
	}
	key := pairs[begin][1]
	keyPair := pairs[begin]

	i, j := begin, end
	for i < j {
		for i < j && key <= pairs[j][1] {
			j--
		}
		pairs[i] = pairs[j]
		for i < j && key >= pairs[i][1] {
			i++
		}
		pairs[j] = pairs[i]
	}
	pairs[i] = keyPair
	qsort(pairs, begin, i - 1)
	qsort(pairs, i + 1, end)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_pairs := strings.Split(flds, "],[")
	pairs := make([][]int, len(str_pairs))
	for i := 0; i < len(str_pairs); i++ {
		pairs[i] = StringToIntArray(str_pairs[i])
	}
	fmt.Printf("pairs = %s\n", IntIntArrayToString(pairs))

	timeStart := time.Now()

	result := findLongestChain(pairs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
