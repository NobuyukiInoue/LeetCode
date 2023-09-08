package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countSymmetricIntegers(low int, high int) int {
	// 24ms - 29ms
	ans := 0
	for num := low; num <= high; num++ {
		s_num := strconv.Itoa(num)
		total, len_s := byte(0), len(s_num)
		for i := 0; i < len_s/2; i++ {
			total += s_num[i] - s_num[len_s-i-1]
		}
		if len_s%2 == 0 && total == 0 {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	low, _ := strconv.Atoi(flds[0])
	high, _ := strconv.Atoi(flds[1])
	fmt.Printf("low = %d, high = %d\n", low, high)

	timeStart := time.Now()

	result := countSymmetricIntegers(low, high)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
