package solution

import (
	"fmt"
	"strings"
	"time"
)

func repeatedNTimes(A []int) int {
	ans := 0
	count := map[int]int{}
	for _, value := range A {
		if count[value] > 0 {
			return value
		} else {
			count[value] = 1
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	A := StringToIntArray(flds)
	fmt.Printf("A = [%s]\n", IntArrayToString(A))

	timeStart := time.Now()

	result := repeatedNTimes(A)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
