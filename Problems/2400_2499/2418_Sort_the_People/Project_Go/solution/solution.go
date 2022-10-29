package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func sortPeople(names []string, heights []int) []string {
	// 26ms - 60ms
	type people struct {
		name   string
		height int
	}
	tmp := make([]people, 0, len(names))
	for i := 0; i < len(names); i++ {
		t := people{
			name:   names[i],
			height: heights[i],
		}
		tmp = append(tmp, t)
	}
	sort.Slice(tmp, func(i, j int) bool { return tmp[i].height > tmp[j].height })
	ans := make([]string, 0, len(names))
	for _, t := range tmp {
		ans = append(ans, t.name)
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	names := strings.Split(flds[0], ",")
	heights := StringToIntArray(flds[1])
	fmt.Printf("names = [%s], heights = \"%s\"\n", names, IntArrayToString(heights))

	timeStart := time.Now()

	result := sortPeople(names, heights)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
