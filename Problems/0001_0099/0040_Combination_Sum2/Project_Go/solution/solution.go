package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func combinationSum2(candidates []int, target int) [][]int {
	// 0ms
	var res [][]int
	var temp []int
	sort.Ints(candidates)
	helper(candidates, temp, target, 0, &res)
	return res
}

func helper(candidates, temp []int, target, sum int, res *[][]int) {
	prev := -1
	for i, candidate := range candidates {
		if prev != -1 && candidate == prev {
			continue
		} else {
			if sum+candidate == target {
				resTemp := make([]int, len(temp)+1)
				copy(resTemp, append(temp, candidate))
				*res = append(*res, resTemp)
				break
			} else if sum+candidate < target {
				helper(candidates[i+1:], append(temp, candidate), target, sum+candidate, res)
				prev = candidate
			} else {
				break
			}
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	candidates := StringToIntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])

	fmt.Printf("candidates = [%s], target = %d\n", IntArrayToString(candidates), target)

	timeStart := time.Now()

	result := combinationSum2(candidates, target)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
