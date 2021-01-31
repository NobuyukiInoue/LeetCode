package solution

import (
	"fmt"
	"strings"
	"time"
)

func subarrayBitwiseORs(arr []int) int {
	// 460ms
	hash := map[int]struct{}{}
	curr := map[int]struct{}{}
	for _, v := range arr {
		next := map[int]struct{}{}
		for k := range curr {
			next[k|v] = struct{}{}
			hash[k|v] = struct{}{}
		}
		next[v] = struct{}{}
		hash[v] = struct{}{}
		curr = next
	}
	return len(hash)
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

	result := subarrayBitwiseORs(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
