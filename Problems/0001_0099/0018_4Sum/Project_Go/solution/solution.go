package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

var ans [][]int

func fourSum(nums []int, target int) [][]int {
	// 0ms - 3ms
	ans = make([][]int, 0)
	sort.Sort(sort.IntSlice(nums))
	df(nums, 0, len(nums)-1, target, 4, make([]int, 0))
	return ans
}

func df(nums []int, l, r, target, N int, res []int) {
	if r-l+1 < N || N < 2 || target < nums[l]*N || target > nums[r]*N {
		return
	}
	if N == 2 {
		for l < r {
			s := nums[l] + nums[r]
			if s == target {
				n_res := append(res, nums[l])
				n_res = append(n_res, nums[r])
				ans = append(ans, n_res)
				l++
				for l < r && nums[l-1] == nums[l] {
					l++
				}
			} else if s < target {
				l++
			} else {
				r--
			}
		}
	} else {
		for i := l; i < r+1; i++ {
			if i == l || (i > l && nums[i-1] != nums[i]) {
				df(nums, i+1, r, target-nums[i], N-1, append(res, nums[i]))
			}
		}
	}
}

func fourSum2(nums []int, target int) [][]int {
	// 47ms - 60ms
	sort.Sort(sort.IntSlice(nums))
	res := make([][]int, 0)
	n := len(nums)
	for i := 0; i <= n-3; i++ {
		for j := i + 1; j <= n-2; j++ {
			k := j + 1
			l := n - 1
			for k < l {
				sum := nums[i] + nums[j] + nums[k] + nums[l]
				if sum == target {
					temp := []int{nums[i], nums[j], nums[k], nums[l]}
					if !contains(res, temp) {
						res = append(res, temp)
					}
				}
				if sum >= target {
					l--
				} else {
					k++
				}
			}
		}
	}
	return res
}

func contains(nums [][]int, arr []int) bool {
	for _, num := range nums {
		check := true
		for i, _ := range num {
			if num[i] != arr[i] {
				check = false
				break
			}
		}
		if check {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])

	fmt.Printf("nums = [%s], target = %d\n", IntArrayToString(nums), target)

	timeStart := time.Now()

	result := fourSum(nums, target)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
