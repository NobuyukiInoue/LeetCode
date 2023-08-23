package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func arrangeWords(text string) string {
	// 8ms - 9ms
	words := strings.Split(text, " ")
	lenmap := make(map[int][]string)
	for _, val := range words {
		arr, ok := lenmap[len(val)]
		if !ok {
			arr = make([]string, 0)
		}
		arr = append(arr, val)
		lenmap[len(val)] = arr
	}

	keys := make([]int, 0)
	for k := range lenmap {
		keys = append(keys, k)
	}

	sort.Ints(keys)

	res := ""
	for _, val := range keys {
		res += strings.Join(lenmap[val], " ") + " "
	}

	ans := []rune(strings.ToLower(res))
	ans[0] = rune(strings.ToUpper(string(ans[0]))[0])
	return strings.TrimRight(string(ans), " ")
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	text := strings.Replace(temp, "]", "", -1)
	fmt.Printf("text = \"%s\"\n", text)

	timeStart := time.Now()

	result := arrangeWords(text)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
