package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

// 0ms

type charCount struct {
	Ch rune
	Count int
}

type charCounts []charCount

func (this charCounts) Len() int {
	return len(this)
}

func (this charCounts) Less(a, b int) bool {
	return this[a].Count > this[b].Count
}

func (this charCounts) Swap(a, b int) {
	this[a], this[b] = this[b], this[a]
}

func frequencySort(s string) string {
	a, b := make([]charCount, 123), strings.Builder{}

	for _, v := range s {
		a[v].Ch = v
		a[v].Count++
	}

	sort.Sort(charCounts(a))

	for _, v := range a {
		b.WriteString(strings.Repeat(string(v.Ch), v.Count))
	}

	return b.String()
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := frequencySort(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
