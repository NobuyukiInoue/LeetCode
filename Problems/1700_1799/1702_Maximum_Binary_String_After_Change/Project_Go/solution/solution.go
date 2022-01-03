package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumBinaryString(binary string) string {
	// 88ms
	ones, zeros, n := 0, 0, len(binary)
	resStr := strings.Repeat("1", n)
	res := []rune(resStr)
	for i := 0; i < n; i++ {
		if binary[i] == '0' {
			zeros++
		} else if zeros == 0 {
			ones++
		}
	}
	if ones < n {
		res[ones+zeros-1] = '0'
	}
	return string(res)
}

func maximumBinaryString_stringJoin(binary string) string {
	// 163ms
	ones, zeros, n := 0, 0, len(binary)
	res := make([]string, n)
	for i := 0; i < n; i++ {
		res[i] = "1"
	}
	for i := 0; i < n; i++ {
		if binary[i] == '0' {
			zeros++
		} else if zeros == 0 {
			ones++
		}
	}
	if ones < n {
		res[ones+zeros-1] = "0"
	}
	return strings.Join(res, "")
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	binary := strings.Replace(temp, "]", "", -1)
	fmt.Printf("binary = \"%s\"\n", binary)

	timeStart := time.Now()

	result := maximumBinaryString(binary)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
