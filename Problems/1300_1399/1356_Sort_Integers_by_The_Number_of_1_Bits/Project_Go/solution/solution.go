package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func sortByBits(arr []int) []int {
	// 4ms
	sort.Sort(sort.IntSlice(arr))

	arrLength := len(arr)
	maxBits, temp := 0, arr[arrLength-1]

	for temp > 0 {
		temp >>= 1
		maxBits += 1
	}
	table := make([][]int, maxBits)
	for i := 0; i < maxBits; i++ {
		table[i] = make([]int, 0)
	}

	for i := 0; i < arrLength; i++ {
		table[countBits(arr[i])] = append(table[countBits(arr[i])], arr[i])
	}

	res := make([]int, 0)
	for i := 0; i < len(table); i++ {
		if len(table[i]) > 0 {
			res = append(res, table[i]...)
		}
	}

	return res
}

func sortByBits2(arr []int) []int {
	// 8ms
	sort.Slice(arr, func(i, j int) bool {
		iCount, jCount := countBits(arr[i]), countBits(arr[j])
		if iCount == jCount {
			return arr[i] < arr[j]
		}
		return iCount < jCount
	})
	return arr
}

func countBits(num int) int {
	count := 0
	for ; num > 0; num >>= 1 {
		if num%2 == 1 {
			count++
		}
	}
	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := StringToIntArray(flds)
	fmt.Printf("arr = [%s]\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := sortByBits(arr)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
