package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func canBeEqual(target []int, arr []int) bool {
	// 8ms
	sort.Sort(sort.IntSlice(target))
	sort.Sort(sort.IntSlice(arr))
	for i := 0; i < len(target); i++ {
		if target[i] != arr[i] {
			return false
		}
	}
	return true
}

func canBeEqual2(target []int, arr []int) bool {
	// 8ms
	tmp := make(map[int]int)
	for _, t := range target {
		tmp[t]++
	}
	for _, a := range arr {
		tmp[a]--
	}
	for _, t := range tmp {
		if t != 0 {
			return false
		}
	}
	return true
}

func strArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	resultStr := data[0]
	for i := 1; i < len(data); i++ {
		resultStr += ", " + data[i]
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	target := StringToIntArray(flds[0])
	arr := StringToIntArray(flds[1])
	fmt.Printf("target = [%s], arr = [%s]\n", IntArrayToString(target), IntArrayToString(arr))

	timeStart := time.Now()

	result := canBeEqual(target, arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
