package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countPrimeSetBits(L int, R int) int {
	checkArray := make([]bool, 33)
	checkArray[2], checkArray[3], checkArray[5] = true, true, true
	checkArray[7], checkArray[11], checkArray[13] = true, true, true
	checkArray[17], checkArray[19], checkArray[23] = true, true, true
	checkArray[29], checkArray[31] = true, true
	toReturn := 0
	for i := L; i <= R; i++ {
		bitsSet, temp := 0, i
		for temp != 0 {
			if temp%2 == 1 {
				bitsSet++
			}
			temp >>= 1
		}
		if checkArray[bitsSet] {
			toReturn++
		}
	}
	return toReturn
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	L, _ := strconv.Atoi(flds[0])
	R, _ := strconv.Atoi(flds[1])

	fmt.Printf("L = %d, R = %d\n", L, R)

	timeStart := time.Now()

	result := countPrimeSetBits(L, R)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
