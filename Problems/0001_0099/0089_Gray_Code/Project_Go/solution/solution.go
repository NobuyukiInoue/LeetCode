package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func grayCode(n int) []int {
	// 0ms
	if n < 0 {
		return nil
	}

	res := []int{0}
	if n == 0 {
		return res
	}

	for i := 0; i < n; i++ {
		for j := len(res) - 1; j >= 0; j-- {
			res = append(res, res[j]|(1<<uint(i)))
		}
	}

	return res
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

	result := grayCode(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
