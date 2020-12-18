package solution

import (
	"fmt"
	"strings"
	"time"
)

func minDistance(word1 string, word2 string) int {
	// 4ms
	m, n := len(word1), len(word2)
	table := make([][]int, m + 1)
	for i := 0; i < m + 1; i++ {
		table[i] = make([]int, n + 1)
	}

	for i := 0; i < m + 1; i++ {
		table[i][0] = i
	}
	for j := 0; j < n + 1; j++ {
		table[0][j] = j
	}

	for i := 1; i < m + 1; i++ {
		for j := 1; j < n + 1; j++ {
			if word1[i - 1] == word2[j - 1] {
				table[i][j] = table[i - 1][j - 1]
			} else {
				table[i][j] = 1 + my3Min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
			}
		}
	}

	return table[m][n]
}

func my3Min(a int, b int, c int) int {
	if a <= b && a <= c {
		return a
	} else if b <= a && b <= c {
		return b
	}
	return c
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	word1, word2 := flds[0], flds[1]
	fmt.Printf("word1 = %s, word2 = %s\n", word1, word2)

	timeStart := time.Now()

	result :=  minDistance(word1, word2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
