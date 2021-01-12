package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxNumber(nums1 []int, nums2 []int, k int) []int {
	// 8ms
    res := make([]int, k)
    for i := 0; i <= k; i++ {
        if len(nums1) >= i && len(nums2) >= k - i {
            res1 := getMax(nums1, i)
            res2 := getMax(nums2, k - i)
            temp := merge(res1, res2)
            if isLarger(temp, res) {
                res = temp
            }
        }
    }
    return res
}

func getMax(nums []int, k int) []int {
    discard := len(nums) - k
    var stack []int
    for i := 0; i < len(nums); i++ {
        for len(stack) > 0 && discard > 0 && stack[len(stack) - 1] < nums[i] {
            stack = stack[:len(stack) - 1]
            discard--
        }
        stack = append(stack, nums[i])
    }
    return stack[:k]
}

func merge(a []int, b []int) []int {
    var res []int
    for len(a) > 0 && len(b) > 0 {
        if isLarger(a, b) {
            res = append(res, a[0])
            a = a[1:]
        } else {
            res = append(res, b[0])
            b = b[1:]
        }
    }
    
    if len(a) > 0 {
        res = append(res, a...)
    }
    
    if len(b) > 0 {
        res = append(res, b...)
    }
    
    return res
}

func isLarger(a []int, b []int) bool {
    l := myMin(len(a), len(b))
    for i := 0; i < l; i++ {
        if a[i] < b[i] {
            return false
        } else if a[i] > b[i] {
            return true
        }
    }
    return len(a) > len(b)
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

	nums1 := StringToIntArray(flds[0])
	nums2 := StringToIntArray(flds[1])
	k, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums1 = [%s], nums2 = [%s], k = %d\n", IntArrayToString(nums1), IntArrayToString(nums2), k)

	timeStart := time.Now()

	result := maxNumber(nums1, nums2, k)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
