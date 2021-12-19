package solution

import (
	"fmt"
	"strings"
	"time"
)

func findEvenNumbers(digits []int) []int {
	// 0ms
	var digCnt [10]int
	for _, digit := range digits {
		digCnt[digit]++
	}
	var res []int
	for i := 1; i < 10; i++ {
		for j := 0; j < 10 && digCnt[i] > 0; j++ {
			for k := 0; k < 10; k += 2 {
				if i == j && digCnt[j] <= 1 {
					break
				} else if digCnt[j] == 0 {
					break
				}
				var kJEq, kIEq int
				if k == j {
					kJEq = 1
				} else {
					kJEq = 0
				}
				if k == i {
					kIEq = 1
				} else {
					kIEq = 0
				}
				if digCnt[k] > (kJEq + kIEq) {
					num := i*100 + j*10 + k
					res = append(res, num)
				}
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	digits := StringToIntArray(flds)
	fmt.Printf("digits = [%s]\n", IntArrayToString(digits))

	timeStart := time.Now()

	result := findEvenNumbers(digits)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
