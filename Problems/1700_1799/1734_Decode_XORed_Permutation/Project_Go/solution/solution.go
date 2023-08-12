package solution

import (
	"fmt"
	"strings"
	"time"
)

func decode(encoded []int) []int {
	// 132ms - 140ms
	n, a := len(encoded)+1, 0
	res := make([]int, n)
	for i := 0; i <= n; i++ {
		a ^= i
		if i < n && i%2 == 1 {
			a ^= encoded[i]
		}
	}
	res[0] = a
	for i := 0; i < n-1; i++ {
		res[i+1] = res[i] ^ encoded[i]
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	encoded := StringToIntArray(flds)
	fmt.Printf("encoded = [%s]\n", IntArrayToString(encoded))

	timeStart := time.Now()

	result := decode(encoded)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
