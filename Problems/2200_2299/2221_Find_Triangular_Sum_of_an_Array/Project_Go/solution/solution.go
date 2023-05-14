package solution

import (
	"fmt"
	"strings"
	"time"
)

func triangularSum(nums []int) int {
	// 12ms
	res, n := 0, len(nums)-1
	mCk, exp2, exp5 := 1, 0, 0
	inv := []int{0, 1, 0, 7, 0, 0, 0, 3, 0, 9}
	pow2mod10 := []int{6, 2, 4, 8}

	for k := 0; true; k++ {
		if exp2 == 0 || exp5 == 0 {
			var mCk_ int
			if exp2 > 0 {
				mCk_ = mCk * pow2mod10[exp2%4]
			} else if exp5 > 0 {
				mCk_ = mCk * 5
			} else {
				mCk_ = mCk
			}
			res = (res + mCk_*nums[k]) % 10
		}
		if k == n {
			return res
		}
		// mCk *= m - k
		mul := n - k
		for mul%2 == 0 {
			mul /= 2
			exp2++
		}
		for mul%5 == 0 {
			mul /= 5
			exp5++
		}
		mCk = mCk * mul % 10

		// mCk /= k + 1
		div := k + 1
		for div%2 == 0 {
			div /= 2
			exp2--
		}
		for div%5 == 0 {
			div /= 5
			exp5--
		}
		mCk = mCk * inv[div%10] % 10
	}
	return res
}

func triangularSum_while(nums []int) int {
	// 49ms - 54ms
	n := len(nums)
	for n != 1 {
		for i := 0; i < n-1; i++ {
			nums[i] = (nums[i] + nums[i+1]) % 10
		}
		n--
	}
	return nums[0]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := triangularSum(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
