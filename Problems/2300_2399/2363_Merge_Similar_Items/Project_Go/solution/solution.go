package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func mergeSimilarItems(items1 [][]int, items2 [][]int) [][]int {
	// 35ms - 37ms
	records := make(map[int]int)
	for _, item := range items1 {
		records[item[0]] += item[1]
	}
	for _, item := range items2 {
		records[item[0]] += item[1]
	}
	ans := make([][]int, 0, len(records))
	for k, v := range records {
		t := []int{k, v}
		ans = append(ans, t)
	}
	sort.Slice(ans, func(i, j int) bool { return ans[i][0] < ans[j][0] })
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "]],[[")

	flds0 := strings.Split(flds[0], "],[")
	items1 := make([][]int, len(flds0))
	for i := 0; i < len(flds0); i++ {
		items1[i] = StringToIntArray(flds0[i])
	}
	fmt.Printf("items1 = %s\n", IntIntArrayToGridString(items1))

	flds1 := strings.Split(flds[1], "],[")
	items2 := make([][]int, len(flds1))
	for i := 0; i < len(flds1); i++ {
		items2[i] = StringToIntArray(flds1[i])
	}
	fmt.Printf("items2 = %s\n", IntIntArrayToGridString(items2))

	timeStart := time.Now()

	result := mergeSimilarItems(items1, items2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
