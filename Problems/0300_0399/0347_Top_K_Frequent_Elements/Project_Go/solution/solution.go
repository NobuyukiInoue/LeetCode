package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func topKFrequent(nums []int, k int) []int {
	// 12ms
	var rst []int

	numsMap := map[int]int{}
	for _, v := range nums {
		numsMap[v]++
	}

	numsMapSort := map[int][]int{}
	maxTmp := make([]int, len(nums)+1)
	for k, v := range numsMap {
		numsMapSort[v] = append(numsMapSort[v], k)
		maxTmp[v] = 1
	}

	for i := len(maxTmp) - 1; i >= 0; i-- {
		if maxTmp[i] != 0 {
			for _, vv := range numsMapSort[i] {
				if k == 0 {
					return rst
				}
				rst = append(rst, vv)
				k--
			}
		}
	}

	return rst
}

func topKFrequent2(nums []int, k int) []int {
	// 44ms
	res := []int{}
	Map := make(map[int]int, k)
	for _, e := range nums {
		Map[e]++
	}
	for ; k > 0; k-- {
		ress := 0
		index := -1
		for i, e := range Map {
			if index < e {
				index = e
				ress = i
			}
		}
		delete(Map, ress)
		res = append(res, ress)
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])

	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := topKFrequent(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
