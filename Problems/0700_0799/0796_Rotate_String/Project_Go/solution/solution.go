package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func rotateString(A string, B string) bool {
	if A == B {
		return true
	}
	for i := 0; i < len(A); i++ {
		if B == string(A[i+1:])+string(A[0:i+1]) {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	words := strings.Split(temp, "],[")
	A := words[0]
	B := words[1]

	fmt.Printf("A = %s, B = %s\n", A, B)

	timeStart := time.Now()

	result := rotateString(A, B)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
