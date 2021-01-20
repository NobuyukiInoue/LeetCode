package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
	// 72ms
	jobs := make([][]int, len(difficulty))
	for i := 0; i < len(jobs); i++ {
		jobs[i] = []int { difficulty[i], profit[i] }
	}
	sort.Slice(jobs, func(i, j int) bool { return jobs[i][0] < jobs[j][0] })
	res, i, best, N := 0, 0, 0, len(jobs)
	sort.Sort(sort.IntSlice(worker))
	for _, ability := range(worker) {
		for i < N && ability >= jobs[i][0] {
			best = myMax(jobs[i][1], best)
			i++
		}
		res += best
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

	difficulty := StringToIntArray(flds[0])
	profit := StringToIntArray(flds[1])
	worker := StringToIntArray(flds[2])

	fmt.Printf("difficulty = %s\n", IntArrayToString(difficulty))
	fmt.Printf("profit = %s\n", IntArrayToString(profit))
	fmt.Printf("worker = %s\n", IntArrayToString(worker))

	timeStart := time.Now()

	result := maxProfitAssignment(difficulty, profit, worker)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
