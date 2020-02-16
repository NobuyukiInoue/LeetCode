package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

type myMap struct {
	num   int
	count int
}

type myMaps []myMap

func (l myMaps) Len() int {
	return len(l)
}

func (l myMaps) Swap(i, j int) {
	l[i], l[j] = l[j], l[i]
}

func (l myMaps) Less(i, j int) bool {
	if l[i].count == l[j].count {
		return (l[i].num < l[j].num)
	}
	return (l[i].count < l[j].count)
}

func rearrangeBarcodes(barcodes []int) []int {
	// 72ms
	barcodeLength := len(barcodes)
	dict := map[int]int{}
	for _, num := range barcodes {
		_, ok := dict[num]
		if ok {
			dict[num]++
		} else {
			dict[num] = 1
		}
	}

	dict2 := myMaps{}
	for k, v := range dict {
		e := myMap{k, v}
		dict2 = append(dict2, e)
	}

	sort.Sort(sort.Reverse(dict2))

	res := make([]int, barcodeLength)
	i := 0
	for _, entry := range dict2 {
		for count := 0; count < entry.count; count++ {
			res[i] = entry.num
			i += 2
			if i >= barcodeLength {
				i = 1
			}
		}
	}
	return res
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	barcodes := make([]int, len(flds))
	for i := 0; i < len(flds); i++ {
		barcodes[i], _ = strconv.Atoi(flds[i])
	}

	fmt.Printf("barcodes = %s\n", intArrayToString(barcodes))
	timeStart := time.Now()

	result := rearrangeBarcodes(barcodes)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
