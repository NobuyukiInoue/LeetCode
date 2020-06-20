package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxRotateFunction(A []int) int {
	// 8ms
	total := 0
	res := 0
	for i, a := range A {
		total += a
		res += i * a
	}
	temp := res
	for _, a := range A {
		if temp-total+a*len(A) > res {
			res = temp - total + a*len(A)
		}
		temp = temp - total + a*len(A)
	}
	return res
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

	result := maxRotateFunction(A)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
