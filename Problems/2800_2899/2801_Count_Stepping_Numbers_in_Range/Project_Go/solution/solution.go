package solution

import (
	"fmt"
	"strings"
	"time"
)

// 26ms - 33ms
var dp [][][][]int
var mod int

func countSteppingNumbers(low string, high string) int {
	mod = 1000000000 + 7
	init_dp(len(high), 2, 2, 10)
	x := sol(0, 0, 0, 0, high)
	init_dp(len(high), 2, 2, 10)
	y := sol(0, 0, 0, 0, low)
	var z int
	if check(low) {
		z = 1
	} else {
		z = 0
	}
	return (x - y + mod + z) % mod
}

func init_dp(m int, n int, o int, p int) {
	dp = make([][][][]int, m)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([][][]int, n)
		for j := 0; j < len(dp[i]); j++ {
			dp[i][j] = make([][]int, o)
			for k := 0; k < len(dp[i][j]); k++ {
				dp[i][j][k] = make([]int, p)
			}
		}
	}
}

func check(num string) bool {
	for i := 0; i < len(num)-1; i++ {
		x := int(num[i] - '0')
		y := int(num[i+1] - '0')
		if myAbs(x-y) != 1 {
			return false
		}
	}
	return true
}

func sol(idx int, f int, c int, p int, s string) int {
	if idx == len(s) {
		return 1
	}
	if dp[idx][f][c][p] != 0 {
		return dp[idx][f][c][p]
	}

	l := int(s[idx] - '0')
	if f == 1 {
		l = 9
	}
	ans := 0
	for d := 0; d <= l; d++ {
		if c == 0 || myAbs(p-d) == 1 {
			if f == 1 {
				if d == 0 {
					ans = (ans + sol(idx+1, 1, c, d, s)) % mod
				} else {
					ans = (ans + sol(idx+1, 1, 1, d, s)) % mod
				}
			} else {
				if d == l {
					if d == 0 {
						ans = (ans + sol(idx+1, 0, c, d, s)) % mod
					} else {
						ans = (ans + sol(idx+1, 0, 1, d, s)) % mod
					}
				} else {
					if d == 0 {
						ans = (ans + sol(idx+1, 1, c, d, s)) % mod
					} else {
						ans = (ans + sol(idx+1, 1, 1, d, s)) % mod
					}
				}
			}
		}
	}
	dp[idx][f][c][p] = ans
	return ans
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

/*
Time Limite Exceeded 2402/2522
var g_low string
var g_high string
var mod int

func countSteppingNumbers(low string, high string) int {
	g_low = ""
	for i := 0; i < len(high)-len(low); i++ {
		g_low += "0"
	}
	g_low = g_low + low
	g_high = high
	mod = 1000000000 + 7
	return dfs(0, false, false, -1, false)
}

func dfs(i int, is_greater_thn_low bool, is_less_thn_high bool, prev_digit int, nonzero bool) int {
	if i == len(g_high) {
		return 1
	}
	total := 0
	var start, end int
	if !is_greater_thn_low {
		start = int(g_low[i]) - '0'
	} else {
		start = 0
	}
	if !is_less_thn_high {
		end = int(g_high[i]-'0') + 1
	} else {
		end = 10
	}
	for nx_digit := start; nx_digit < end; nx_digit++ {
		if !nonzero || myAbs(prev_digit-nx_digit) == 1 {
			total += dfs(i+1, is_greater_thn_low || nx_digit > int(g_low[i]-'0'), is_less_thn_high || nx_digit < int(g_high[i]-'0'), nx_digit, nonzero || nx_digit != 0)
		}
	}
	return total % mod
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	low, high := flds[0], flds[1]
	fmt.Printf("low = %s, high = %s\n", low, high)

	timeStart := time.Now()

	result := countSteppingNumbers(low, high)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
