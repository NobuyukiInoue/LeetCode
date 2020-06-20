package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkIfExist2(arr []int) bool {
	// 4ms
	lst := make(map[int]bool, 0)
	for _, num := range arr {
		if num%2 == 0 {
			if _, ok := lst[num/2]; ok {
				return true
			}
		}
		if _, ok := lst[num*2]; ok {
			return true
		}
		lst[num] = true
	}
	return false
}

func checkIfExist(arr []int) bool {
	// 4ms
	lst := make([]int, 0)
	for _, num := range arr {
		if contains(lst, num*2) || num%2 == 0 && contains(lst, num/2) {
			return true
		}
		lst = append(lst, num)
	}
	return false
}

func contains(lst []int, num int) bool {
	for _, v := range lst {
		if v == num {
			return true
		}
	}
	return false
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

	result := checkIfExist(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
