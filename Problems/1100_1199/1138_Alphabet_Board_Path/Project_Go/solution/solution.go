package solution

import (
	"bytes"
	"fmt"
	"strings"
	"time"
)

func alphabetBoardPath(target string) string {
	// 0ms
	board := []string {"abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"}
	res := ""
	x, y := 0, 0
	for _, ch := range(target) {
		for i := 0; i < len(board); i++ {
			pos := strings.Index(board[i], string(ch))
			if (pos >= 0) {
				toLastRow := false
				if (x > i) {
					res += string(bytes.Repeat([]byte("U"), x - i))
				} else if (x < i) {
					if (i == 5) {
						res += string(bytes.Repeat([]byte("D"), 4 - x))
						toLastRow = true
					} else {
						res += string(bytes.Repeat([]byte("D"), i - x))
					}
				}
				x = i
				if y > pos {
					res += string(bytes.Repeat([]byte("L"), y - pos))
				} else if (y < pos) {
					res += string(bytes.Repeat([]byte("R"), pos - y))
				}
				if (toLastRow) {
					res += "D"
				}
				res += "!"
				y = pos
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	target := strings.Replace(temp, "]", "", -1)
	fmt.Printf("target = %s\n", target)

	timeStart := time.Now()

	result := alphabetBoardPath(target)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
