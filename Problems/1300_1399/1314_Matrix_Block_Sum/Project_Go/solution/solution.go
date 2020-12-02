package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func matrixBlockSum(mat [][]int, K int) [][]int {
	// 4ms
	r, c := len(mat), len(mat[0])
	temp := make([][]int, r)
	answer := make([][]int, r)
	for i := 0; i < r; i++ {
		temp[i] = make([]int, c)
		answer[i] = make([]int, c)
	}

	for i := 0; i < r; i++ {
		res := 0
		for delta_c := 0; delta_c < K + 1; delta_c++ {
			if delta_c < c {
				res += mat[i][delta_c]
			}
		}
		temp[i][0] = res
	}

	for i := 0; i < r; i++ {
		res := temp[i][0]
		for j := 1; j < c; j++ {
			remove_c := j - K - 1
			if 0 <= remove_c && remove_c < c {
				res -= mat[i][remove_c]
			}
			add_c := j + K
			if 0 <= add_c && add_c < c {
				res += mat[i][add_c]
			}
			temp[i][j] = res
		}
	}

	for i := 0; i < c; i++ {
		res := 0
		for delta_r := 0; delta_r < K + 1; delta_r++ {
			res += temp[delta_r][i]
		}
		answer[0][i] = res
	}

	for i := 0; i < c; i++ {
		res := answer[0][i]
		for j := 1; j < r; j++ {
			remove_r := j - K - 1
			if 0 <= remove_r && remove_r < r {
				res -= temp[remove_r][i]
			}
			add_r := j + K
			if 0 <= add_r && add_r < r {
				res += temp[add_r][i]
			}
			answer[j][i] = res
		}
	}

	return answer
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "]],[")

	str_mat := strings.Split(strings.Replace(flds[0], "[[[", "", -1), "],[")
	mat := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		mat[i] = StringToIntArray(str_mat[i])
	}
	K, _ := strconv.Atoi(strings.Replace(flds[1], "]]", "", -1))

	fmt.Printf("mat = %s, K = %d\n", IntIntArrayToString(mat), K)

	timeStart := time.Now()

	result := matrixBlockSum(mat, K)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
