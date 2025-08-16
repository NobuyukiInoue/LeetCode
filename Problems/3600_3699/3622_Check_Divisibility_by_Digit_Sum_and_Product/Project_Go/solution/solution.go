package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkDivisibility(n int) bool {
	v_prd, v_sum, temp_n := 1, 0, n
	for temp_n > 0 {
		m := temp_n % 10
		v_prd *= m
		v_sum += m
		temp_n /= 10
	}
	return n%(v_prd+v_sum) == 0
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

	result := checkDivisibility(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
