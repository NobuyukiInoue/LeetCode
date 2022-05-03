package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func intersection(nums [][]int) []int {
	// 12ms
	countMap := make(map[int]int)
	inEachArray := make([]int, 0)
	for _, num := range nums {
		for _, x := range num {
			countMap[x]++
			if countMap[x] == len(nums) {
				inEachArray = append(inEachArray, x)
			}
		}
	}
	sort.Sort(sort.IntSlice(inEachArray))
	return inEachArray
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	nums := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		nums[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("nums = %s\n", IntIntArrayToString(nums))

	timeStart := time.Now()

	result := intersection(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
