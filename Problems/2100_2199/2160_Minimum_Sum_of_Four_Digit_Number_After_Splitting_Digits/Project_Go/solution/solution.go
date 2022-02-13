package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func minimumSum(num int) int {
	// 0ms
	var temp []int
	for i := 0; i < 4; i++ {
		temp = append(temp, num%10)
		num /= 10
	}
	sort.Ints(temp)
	return 10*temp[0] + temp[2] + 10*temp[1] + temp[3]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	num, _ := strconv.Atoi(flds)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := minimumSum(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
