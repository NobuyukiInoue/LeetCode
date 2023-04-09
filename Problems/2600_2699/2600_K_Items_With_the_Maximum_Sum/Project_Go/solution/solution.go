package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func kItemsWithMaximumSum(numOnes int, numZeros int, numNegOnes int, k int) int {
	// 3ms - 7ms
	return myMin(k, numOnes) - myMax(0, k-numZeros-numOnes)
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	numOnes, _ := strconv.Atoi(flds[0])
	numZeros, _ := strconv.Atoi(flds[1])
	numNegOnes, _ := strconv.Atoi(flds[2])
	k, _ := strconv.Atoi(flds[3])
	fmt.Printf("numOnes = %d, numZeros = %d, numNegOnes = %d, k = %d", numOnes, numZeros, numNegOnes, k)

	timeStart := time.Now()

	result := kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
