package solution

import (
	"fmt"
	"strings"
	"time"
)

func sumArray(A []int) int {
	sum := 0
	for _, v := range A {
		sum = sum + v
	}
	return sum
}
func fairCandySwap(A []int, B []int) []int {
	sumA := sumArray(A)
	sum := sumA + sumArray(B)
	var mp = make(map[int]int)
	var ans []int
	for k, v := range B {
		mp[v] = k
	}

	for _, v := range A {
		need := sum/2 - (sumA - v)

		if _, ok := mp[need]; ok {
			ans = append(ans, v, need)
			break
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	A := StringToIntArray(flds[0])
	B := StringToIntArray(flds[1])

	fmt.Printf("A = [%s]\n", IntArrayToString(A))
	fmt.Printf("B = [%s]\n", IntArrayToString(B))

	timeStart := time.Now()

	result := fairCandySwap(A, B)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
