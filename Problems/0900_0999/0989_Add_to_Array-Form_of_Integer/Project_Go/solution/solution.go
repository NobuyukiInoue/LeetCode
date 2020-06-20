package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func addToArrayForm(A []int, K int) []int {
	var res []int
	for i := len(A) - 1; i >= 0; i-- {
		res = append(res, (A[i]+K)%10)
		K = (A[i] + K) / 10
	}

	for K > 0 {
		res = append(res, K%10)
		K /= 10
	}

	for i := 0; i < len(res)/2; i++ {
		tmp := res[i]
		res[i] = res[len(res)-1-i]
		res[len(res)-1-i] = tmp
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	A := StringToIntArray(flds[0])
	K, _ := strconv.Atoi(flds[1])
	fmt.Printf("A = [%s]\n", IntArrayToString(A))
	fmt.Printf("K = %d\n", K)

	timeStart := time.Now()

	result := addToArrayForm(A, K)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
