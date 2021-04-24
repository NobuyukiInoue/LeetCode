package solution

import (
	"fmt"
    "strconv"
	"strings"
	"time"
)

func largestSumOfAverages(A []int, K int) float64 {
    // 4ms
    N := len(A)
    memo := make([][]float64, N + 1)
    for i := 0; i < len(memo); i++ {
        memo[i] = make([]float64, N + 1)
    }
    cur := 0.0
    for i := 0; i < N; i++ {
        cur += float64(A[i])
        memo[i + 1][1] = float64(cur)/float64(i + 1)
    }
    return search(N, K, A, memo)
}

func search(n int, k int, A []int, memo [][]float64) float64 {
    if memo[n][k] > 0 {
        return memo[n][k]
    }
    if n < k {
        return 0
    }

    cur := 0.0
    for i := n - 1; i > 0; i-- {
        cur += float64(A[i])
        memo[n][k] = myMax(memo[n][k], search(i, k - 1, A, memo) + float64(cur)/float64(n - i))
    }
    return memo[n][k]
}

func myMax(i float64, j float64) float64 {
	if i >= j {
		return i
	}
	return j
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

    A := StringToIntArray(flds[0])
	K, _ := strconv.Atoi(flds[1])
	fmt.Printf("A = %s, K = %d\n", IntArrayToString(A), K)

	timeStart := time.Now()

	result := largestSumOfAverages(A, K)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
