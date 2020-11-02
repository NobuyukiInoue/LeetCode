package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canFormArray(arr []int, pieces [][]int) bool {
	// 0ms
	for _, piece := range pieces {
		if indexOf(arr, piece[0]) < 0 {
			return false
		}
		idx := indexOf(arr, piece[0])
		if arrayDiff(arr, idx, piece) == false {
			return false
		}
	}
	return true
}

func indexOf(arr []int, target int) int {
	for i := 0; i < len(arr); i++ {
		if arr[i] == target {
			return i
		}
	}
	return -1
}

func arrayDiff(arr []int, start int, targetArr []int) bool {
	for i := 0; i < len(targetArr); i++ {
		if i+start > len(arr)-1 {
			return false
		}
		if arr[i+start] != targetArr[i] {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")

	arr := StringToIntArray(strings.Replace(flds[0], "[[", "", -1))
	fmt.Printf("arr = %s\n", IntArrayToString(arr))

	piecesStr := strings.Split(strings.Replace(flds[1], "]]]", "", -1), "],[")
	pieces := make([][]int, len(piecesStr))
	for i, _ := range piecesStr {
		pieces[i] = StringToIntArray(piecesStr[i])
	}
	fmt.Printf("pieses = %s\n", IntIntArrayToString(pieces))

	timeStart := time.Now()

	result := canFormArray(arr, pieces)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
