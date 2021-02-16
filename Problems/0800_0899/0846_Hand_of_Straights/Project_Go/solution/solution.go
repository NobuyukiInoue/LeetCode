package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

// 52ms

type IntCount struct {
	value int
	count int
}

func isNStraightHand(hand []int, W int) bool {
	if W == 1 {
		return true
	}
	if len(hand)%W != 0 {
		return false
	}

	temp := make(map[int]int)
	for _, h := range hand {
		temp[h]++
	}

	counts := []IntCount{}
	for k, v := range temp {
		counts = append(counts, IntCount{
			value: k,
			count: v,
		})
	}
	sort.Slice(counts, func(i, j int) bool {
		return counts[i].value < counts[j].value
	})

	n := len(hand) / W
	for n > 0 {
		counts[len(counts)-1].count--
		for i := 1; i < W; i++ {
			if len(counts)-1-i < 0 || counts[len(counts)-1-i].value+1 != counts[len(counts)-i].value {
				return false
			}
			counts[len(counts)-1-i].count--
		}

		p := len(counts) - W
		for i := len(counts) - W; i < len(counts); i++ {
			if counts[i].count != 0 {
				counts[p] = counts[i]
				p++
			}
		}
		counts = counts[:p]
		n--
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	hand := StringToIntArray(flds[0])
	W, _ := strconv.Atoi(flds[1])
	fmt.Printf("hand = [%s], W = %d\n", IntArrayToString(hand), W)

	timeStart := time.Now()

	result := isNStraightHand(hand, W)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
