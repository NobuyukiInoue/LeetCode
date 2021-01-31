package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func canReorderDoubled(arr []int) bool {
	// 84ms
	dic := map[int]int{}

	for _, a := range arr {
		dic[a]++
	}

	keys := make([]int, len(dic))
	i := 0
	for k, _ := range dic {
		keys[i] = k
		i++
	}

	sort.Sort(sort.IntSlice(keys))

	for _, k := range keys {
		if dic[k] != 0 && dic[2*k] != 0 {
			if dic[k] > dic[2*k] {
				dic[k] -= dic[2*k]
				dic[2*k] = 0
			} else {
				dic[2*k] -= dic[k]
				dic[k] = 0
			}
		}
	}

	for _, v := range dic {
		if v != 0 {
			return false
		}
	}
	return true
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

	result := canReorderDoubled(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
