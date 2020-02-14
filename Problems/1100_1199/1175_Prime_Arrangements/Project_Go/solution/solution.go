package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func numPrimeArrangements(n int) int {
	// 0ms
	primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
	modulo := (int)(math.Pow(10, 9)) + 7
	result, primeCounter := 1, 0
	for i := 0; i < len(primes); i++ {
		if primes[i] <= n {
			primeCounter++
		} else {
			break
		}
	}
	for i := 2; i <= primeCounter; i++ {
		result = (result * i) % modulo
	}
	for i := 2; i <= n-primeCounter; i++ {
		result = (result * i) % modulo
	}

	return result
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

	result := numPrimeArrangements(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
