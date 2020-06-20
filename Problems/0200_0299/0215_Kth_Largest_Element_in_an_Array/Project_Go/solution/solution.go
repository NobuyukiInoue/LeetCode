package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func findKthLargest2(nums []int, k int) int {
	// 8ms
	sort.Sort(sort.IntSlice(nums))
	return nums[len(nums)-k]
}

func findKthLargest(nums []int, k int) int {
	// 4ms
	h := &heap{buf: nums}
	h.build()
	for i := 0; i < k; i++ {
		if i == k-1 {
			return h.pop()
		}
		h.pop()
	}
	return -1
}

type heap struct {
	buf []int
}

func (h *heap) pop() int {
	ret := h.buf[0]
	h.buf[0], h.buf[len(h.buf)-1] = h.buf[len(h.buf)-1], h.buf[0]
	h.buf = h.buf[:len(h.buf)-1]
	h.down(0)
	return ret
}

func (h *heap) up(idx int) {
	parent := (idx - 1) / 2
	if h.buf[parent] < h.buf[idx] {
		h.buf[parent], h.buf[idx] = h.buf[idx], h.buf[parent]
		h.up(parent)
	}
}

func (h *heap) down(idx int) {
	leftChild := idx*2 + 1
	rightChild := idx*2 + 2
	if leftChild < len(h.buf) && h.buf[leftChild] > h.buf[idx] {
		var swapWith int
		if rightChild < len(h.buf) && h.buf[rightChild] > h.buf[leftChild] {
			swapWith = rightChild
		} else {
			swapWith = leftChild
		}

		h.buf[swapWith], h.buf[idx] = h.buf[idx], h.buf[swapWith]
		h.down(swapWith)
		return
	}

	if rightChild < len(h.buf) && h.buf[rightChild] > h.buf[idx] {
		h.buf[rightChild], h.buf[idx] = h.buf[idx], h.buf[rightChild]
		h.down(rightChild)
	}
}

func (h *heap) build() {
	for i := len(h.buf); i >= 0; i -= 2 {
		parent := (i - 1) / 2
		h.down(parent)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s], k = %d\n", IntArrayToString(nums), k)

	timeStart := time.Now()

	result := findKthLargest(nums, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
