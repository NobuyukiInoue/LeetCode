package solution

import (
	"fmt"
	"strings"
	"time"
)

func addNegabinary(arr1 []int, arr2 []int) []int {
	// 0ms
	s := make([]int, 0)
	i, j := len(arr1) - 1, len(arr2) - 1
	c := 0
	for i >= 0 || j >= 0 || c != 0 {
		if i >= 0 {
			c += arr1[i]
			i--
		}
		if j >= 0 {
			c += arr2[j]
			j--
		}
		s = append(s, c & 1)
		c = -(c >> 1)
	}
	for len(s) > 0 && s[len(s)-1] == 0 {
		s = s[:len(s) - 1]
	}
	res := make([]int, len(s))
	i = 0;
	for i := 0; len(s) > 0; i++ {
		res[i] = s[len(s) - 1]
		s = s[:len(s) - 1]
	}
	if len(res) == 0 {
		return []int{0}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arr1 := StringToIntArray(flds[0])
	arr2 := StringToIntArray(flds[1])
	fmt.Printf("arr1 = %s\n", IntArrayToString(arr1))
	fmt.Printf("arr2 = %s\n", IntArrayToString(arr2))

	timeStart := time.Now()

	result := addNegabinary(arr1, arr2)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
