package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func fizzBuzz(n int) []string {
	// 112ms
	results := []string{}
	for i := 1; i <= n; i++ {
		switch {
		case i%15 == 0:
			results = append(results, "FizzBuzz")
		case i%3 == 0:
			results = append(results, "Fizz")
		case i%5 == 0:
			results = append(results, "Buzz")
		default:
			results = append(results, strconv.Itoa(i))
		}
	}
	return results
}

func fizzBuzz2(n int) []string {
	// 120ms
	results := make([]string, n)
	for i := 1; i <= n; i++ {
		if i%3 == 0 && i%5 == 0 {
			results[i-1] = "FizzBuzz"
		} else if i%3 == 0 {
			results[i-1] = "Fizz"
		} else if i%5 == 0 {
			results[i-1] = "Buzz"
		} else {
			results[i-1] = strconv.Itoa(i)
		}
	}

	return results
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)

	fmt.Printf("n = [%d]\n", n)
	timeStart := time.Now()

	result := fizzBuzz(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
