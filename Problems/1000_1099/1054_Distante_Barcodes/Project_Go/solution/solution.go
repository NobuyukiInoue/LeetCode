package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

type myMap struct {
	num   int
	count int
}

type myMaps []myMap

func rearrangeBarcodes(barcodes []int) []int {
	// 80ms
	barcodeLength := len(barcodes)
	dict := map[int]int{}
	for _, num := range barcodes {
		dict[num]++
	}

	dict2 := myMaps{}
	for k, v := range dict {
		e := myMap{k, v}
		dict2 = append(dict2, e)
	}

	sort.Slice(dict2, func(i, j int) bool {
		return dict2[i].count >= dict2[j].count
	})

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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	barcodes := StringToIntArray(flds)
	fmt.Printf("barcodes = [%s]\n", IntArrayToString(barcodes))
	timeStart := time.Now()

	result := rearrangeBarcodes(barcodes)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
