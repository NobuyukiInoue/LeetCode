package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func splitNum(num int) int {
	// 0ms - 2ms
	ca := make([]int, 0)
	for num > 0 {
		ca = append(ca, num%10)
		num /= 10
	}
	sort.Ints(ca)
	arr := []int{0, 0}
	for i := 0; i < len(ca); i++ {
		arr[i%2] *= 10
		arr[i%2] += ca[i]
	}
	return arr[0] + arr[1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	num, _ := strconv.Atoi(flds)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := splitNum(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
