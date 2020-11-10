package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getMaximumGenerated(n int) int {
	// 0ms
	if n < 1 {
		return 0
	}

	nums := make([]int, n + 1)
	nums[0], nums[1] = 0, 1
	max_num := 1
	for i := 1; i <= n; i++ {
		if (2 * i <= n){
			nums[2*i] = nums[i];
			max_num = myMax(max_num, nums[2*i])
		}  
		if(((2 * i) + 1) <= n){
			nums[(2*i)+1] = nums[i] + nums[i + 1];
			max_num = myMax(max_num, nums[(2*i) + 1])
		}
	}
	return max_num
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := getMaximumGenerated(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
