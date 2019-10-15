package solution

import (
	"fmt"
	"strings"
	"time"
)

func findRestaurant(list1 []string, list2 []string) []string {
	dic := make(map[string]int)
	for i, key := range list1 {
		_, ok := dic[key]
		if ok == false {
			dic[key] = i
		}
	}

	minVal := 10000
	result := make([]string, 0)

	for j, key := range list2 {
		value, ok := dic[key]
		if ok == true {
			if j+value < minVal {
				minVal = j + value
				result = []string{key}
			} else if j+value == minVal {
				result = append(result, key)
			}
		}
	}

	return result
}

func IntMin(a int, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func StringArray2string(arr []string) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "[" + arr[0]
	for i := 1; i < len(arr); i++ {
		resultStr += "," + arr[i]
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	list1 := strings.Split(flds[0], ",")
	list2 := strings.Split(flds[1], ",")
	fmt.Printf("list1 = %s\n", StringArray2string(list1))
	fmt.Printf("list2 = %s\n", StringArray2string(list2))

	timeStart := time.Now()

	result := findRestaurant(list1, list2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", StringArray2string(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
