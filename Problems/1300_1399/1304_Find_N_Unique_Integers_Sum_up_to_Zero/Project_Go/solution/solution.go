package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func sumZero(n int) []int {
	// 0ms
	sum := make([]int, 0, n)
	if n%2 == 1 {
		sum = append(sum, 0)
		n--
	}
	for i := 1; i < n/2+1; i++ {
		sum = append(sum, +1*i)
		sum = append(sum, -1*i)
	}
	return sum
}

func sumZero2(n int) []int {
	// 8ms
	A := make([]int, n)
	for i := 0; i < n; i++ {
		A[i] = i*2 - n + 1
	}
	return A
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := sumZero(n)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
