package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func arrayRankTransform(arr []int) []int {
	// Time Limit Exceeded
	if len(arr) <= 0 {
		return arr
	}

	sorted_arr := make([]int, len(arr))
	copy(sorted_arr[:], arr[:])
	sort.Sort(sort.IntSlice(sorted_arr))

	mp := make(map[int]int)
	rank := 1
	mp[sorted_arr[0]] = rank
	for i := 1; i < len(sorted_arr); i++ {
		if sorted_arr[i-1] != sorted_arr[i] {
			rank++
		}
		mp[sorted_arr[i]] = rank
	}

	ranks := make([]int, len(arr))
	for i := 0; i < len(arr); i++ {
		ranks[i] = mp[arr[i]]
	}

	return ranks
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

	result := arrayRankTransform(arr)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
