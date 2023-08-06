package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func findLeastNumOfUniqueInts(arr []int, k int) int {
	// 87ms - 88ms
	cnts := make(map[int]int, 0)
	for _, v := range arr {
		cnts[v]++
	}
	sorted_cnts := make([]int, 0)
	for _, v := range cnts {
		sorted_cnts = append(sorted_cnts, v)
	}
	sort.Sort(sort.IntSlice(sorted_cnts))
	removed_cnts := 0
	for _, v := range sorted_cnts {
		if k-v < 0 {
			break
		}
		k -= v
		removed_cnts++
	}
	return len(sorted_cnts) - removed_cnts
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arr := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("arr = [%s], k = %d\n", IntArrayToString(arr), k)

	timeStart := time.Now()

	result := findLeastNumOfUniqueInts(arr, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
