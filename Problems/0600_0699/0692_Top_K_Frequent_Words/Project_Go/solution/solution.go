package solution

import (
	"fmt"
	"strconv"
	"strings"
	"sort"
	"time"
)

type elem struct {
	word string
	freq int
}

func topKFrequent(words []string, k int) []string {
	// 4ms
	dict := make(map[string]int)
	for _, v := range words {
		dict[v]++
	}

	var list []elem
	for k, v := range dict {
		list = append(list, elem{word: k, freq: v})
	}

	sort.Slice(list, func(i int, j int) bool {
		if list[i].freq != list[j].freq {
			return list[i].freq > list[j].freq
		}
		return list[i].word < list[j].word
	})

	res := make([]string, k)
	for i := 0; i < k; i++ {
		res[i] = list[i].word
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	words := strings.Split(flds[0], ",")
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("words = %s, k = %d\n", words, k)

	timeStart := time.Now()

	result := topKFrequent(words, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
