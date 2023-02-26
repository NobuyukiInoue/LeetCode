package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minMaxDifference(num int) int {
	// 2ms
	num_str := strconv.Itoa(num)
	i := 0
	for num_str[i] == '9' && i < len(num_str)-1 {
		i++
	}
	max, _ := strconv.Atoi(strings.Replace(num_str, string(num_str[i]), "9", -1))
	min, _ := strconv.Atoi(strings.Replace(num_str, string(num_str[0]), "0", -1))
	return max - min
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	num, _ := strconv.Atoi(flds)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := minMaxDifference(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
