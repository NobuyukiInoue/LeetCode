package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minHeightShelves(books [][]int, shelf_width int) int {
	// 0ms
	dp := make([]int, len(books)+1)
	for i := 1; i <= len(books); i++ {
		width := books[i-1][0]
		height := books[i-1][1]
		dp[i] = dp[i-1] + height
		for j := i - 1; j > 0; j-- {
			if width+books[j-1][0] <= shelf_width {
				width += books[j-1][0]
				height = myMax(height, books[j-1][1])
				dp[i] = myMin(dp[i], dp[j-1]+height)
			} else {
				break
			}
		}
	}

	return dp[len(books)]
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
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")
	books_str := strings.Split(flds[0], "],[")

	books := make([][]int, len(books_str))
	for i := 0; i < len(books_str); i++ {
		books[i] = StringToIntArray(books_str[i])
	}
	fmt.Printf("books = %s\n",IntIntArrayToString(books))

	shelf_width, _ := strconv.Atoi(strings.Replace(flds[1], "]]", "", -1))
	fmt.Printf("shelf_width = %d\n", shelf_width)

	timeStart := time.Now()

	result := minHeightShelves(books, shelf_width)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
