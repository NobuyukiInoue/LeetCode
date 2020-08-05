package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
	"unsafe"
)

func leastInterval(tasks []byte, n int) int {
	// 4ms
	if tasks == nil || len(tasks) == 0 {
		return 0
	}

	cnt := make([]int, 26)
	for _, ch := range tasks {
		cnt[ch-'A']++
	}

	sort.Sort(sort.IntSlice(cnt))

	maxCnt := cnt[25] - 1
	spaces := maxCnt * n
	for i := 24; i >= 0; i-- {
		spaces -= myMin(maxCnt, cnt[i])
	}
	spaces = myMax(0, spaces)
	return len(tasks) + spaces
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a int, b int) int {
	if a < b {
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

	tasksStr := strings.Replace(flds[0], ",", "", -1)
	tasks := StringToByteArray(tasksStr)
	n, _ := strconv.Atoi(flds[1])
	fmt.Printf("tasks = %s, n = %d\n", *(*string)(unsafe.Pointer(&tasks)), n)

	timeStart := time.Now()

	result := leastInterval(tasks, n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
