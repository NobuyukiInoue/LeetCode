package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func divisorSubstrings(num int, k int) int {
	// 3ms
	str_num := strconv.Itoa(num)
	ans := 0
	for i := 0; i < len(str_num)-k+1; i++ {
		temp, _ := strconv.Atoi(str_num[i : i+k])
		if temp != 0 && num%temp == 0 {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	num, k := nums[0], nums[1]
	fmt.Printf("num = %d, k = %d\n", num, k)

	timeStart := time.Now()

	result := divisorSubstrings(num, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
