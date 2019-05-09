package main

import (
	"fmt"
	"strings"
	"time"
)

func repeatedStringMatch(A string, B string) int {
	as := A
	max := len(B)/len(A) + 3
	for rep := 1; rep < max; rep++ {
		if strings.Index(as, B) != -1 {
			return rep
		}
		as += A
	}
	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	A := flds[0]
	B := flds[1]

	fmt.Printf("A = %s\n", A)
	fmt.Printf("B = %s\n", B)

	timeStart := time.Now()

	result := repeatedStringMatch(A, B)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
