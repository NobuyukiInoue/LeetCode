package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func tictactoe(moves [][]int) string {
	// 0ms
	aRow := make([]int, 3)
	aCol := make([]int, 3)
	bRow := make([]int, 3)
	bCol := make([]int, 3)

	aD1, aD2, bD1, bD2 := 0, 0, 0, 0

	for i := 0; i < len(moves); i++ {
		r, c := moves[i][0], moves[i][1]
		if i%2 == 1 {
			bRow[r]++
			if bRow[r] == 3 {
				return "B"
			}
			bCol[c]++
			if bCol[c] == 3 {
				return "B"
			}
			if r == c {
				bD1++
				if bD1 == 3 {
					return "B"
				}
			}
			if r+c == 2 {
				bD2++
				if bD2 == 3 {
					return "B"
				}
			}
		} else {
			aRow[r]++
			if aRow[r] == 3 {
				return "A"
			}
			aCol[c]++
			if aCol[c] == 3 {
				return "A"
			}
			if r == c {
				aD1++
				if aD1 == 3 {
					return "A"
				}
			}
			if r+c == 2 {
				aD2++
				if aD2 == 3 {
					return "A"
				}
			}
		}
	}
	if len(moves) == 9 {
		return "Draw"
	} else {
		return "Pending"
	}
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	moves := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		moves[i] = str2IntArray(flds[i])
	}

	fmt.Printf("moves = [")
	for i, _ := range moves {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(moves[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(moves[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := tictactoe(moves)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
