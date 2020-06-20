package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func selfDividingNumbers(left int, right int) []int {
	res := make([]int, 0)
	for i, n := left, 0; i <= right; i++ {
		for n = i; n > 0; n /= 10 {
			if n%10 == 0 || i%(n%10) != 0 {
				break
			}
		}
		if n == 0 {
			res = append(res, i)
		}
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	left, _ := strconv.Atoi(flds[0])
	right, _ := strconv.Atoi(flds[1])
	fmt.Printf("left = %d, right = %d\n", left, right)

	timeStart := time.Now()

	result := selfDividingNumbers(left, right)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
