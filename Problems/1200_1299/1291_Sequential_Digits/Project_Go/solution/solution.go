package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func sequentialDigits(low int, high int) []int {
	// 0ms
	res := make([]int, 0)
	total := make([]int, 0)
	lo, fact, prev := 12,11, 12

	for i := 9; i > 0; i-- {
		total = append(total, lo)
		for lo%10 != 9 {
			lo += fact
			total = append(total, lo)
		}
		fact = fact*10 + 1
		lo = prev + fact
		prev = lo
	}

	for _, val := range(total) {
		if val > high {
			break
		}
		if val >= low && val <= high {
			res = append(res, val)
		}
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	flds := strings.Split(temp, "],[")

	low, _  := strconv.Atoi(flds[0]);
	high, _ := strconv.Atoi(flds[1]);
	fmt.Printf("low = %d, hight = %d\n", low, high)

	timeStart := time.Now()

	result := sequentialDigits(low, high)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
