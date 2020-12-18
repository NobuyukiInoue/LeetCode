package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxScore(cardPoints []int, k int) int {
	// 52ms
	res, sum, slideSum := 0, 0, 0
	n := len(cardPoints)

	for i := 0; i < n; i++ {
		sum += cardPoints[i]
	}
	for i := 0; i < n-k; i++ {
		slideSum += (cardPoints[i])
	}
	res = sum - slideSum
	for i := n - k; i < n; i++ {
		slideSum += cardPoints[i] - cardPoints[i-(n-k)]
		res = myMax(res, sum-slideSum)
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	cardPoints := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("cardPoints = [%s], k = %d\n", IntArrayToString(cardPoints), k)

	timeStart := time.Now()

	result := maxScore(cardPoints, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
