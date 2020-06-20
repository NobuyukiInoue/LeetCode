package solution

import (
	"fmt"
	"strings"
	"time"
)

func imageSmoother(M [][]int) [][]int {
	res := make([][]int, len(M))
	for i, _ := range res {
		res[i] = make([]int, len(M[0]))
	}

	resWork := make([][]int, len(M)+2)
	for i, _ := range resWork {
		resWork[i] = make([]int, len(M[0])+2)
	}

	for i := 0; i < len(M)*len(M[0]); i++ {
		resWork[i/len(M[0])+1][i%len(M[0])+1] = M[i/len(M[0])][i%len(M[0])]
	}

	for i := 0; i < len(M)*len(M[0]); i++ {
		row := i / len(M[0])
		col := i % len(M[0])
		count := 9
		sum := resWork[row+1][col+1] +
			resWork[row+0][col+0] +
			resWork[row+0][col+1] +
			resWork[row+0][col+2] +
			resWork[row+1][col+0] +
			resWork[row+1][col+2] +
			resWork[row+2][col+0] +
			resWork[row+2][col+1] +
			resWork[row+2][col+2]

		if row == 0 || col == 0 || row == len(M)-1 || col == len(M[0])-1 {
			count = 6
			if row == 0 && col == 0 {
				count = 4
			} else if row == len(M)-1 && col == len(M[0])-1 {
				count = 4
			} else if row == 0 && col == len(M[0])-1 {
				count = 4
			} else if row == len(M)-1 && col == 0 {
				count = 4
			}
		}

		if len(M) == 1 || len(M[0]) == 1 {
			count = 3
			if row == 0 || col == 0 {
				if row == 0 && col == 0 {
					count = 2
				} else if row == 0 && col == len(M[0])-1 {
					count = 2
				} else if row == len(M)-1 && col == 0 {
					count = 2
				}
			}
			if len(M) == len(M[0]) {
				count = 1
			}
		}

		res[row][col] = sum / count
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	M := make([][]int, len(flds))
	for i, _ := range flds {
		M[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("M = %s\n", IntIntArrayToGridString(M))

	timeStart := time.Now()

	result := imageSmoother(M)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
