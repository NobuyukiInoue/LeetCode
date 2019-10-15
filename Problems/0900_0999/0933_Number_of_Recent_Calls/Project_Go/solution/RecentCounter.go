package solution

type RecentCounter struct {
	curName    string
	beforeName []string
	beforeTm   []int
	cn         int
	point      int
}

func Constructor() RecentCounter {
	return RecentCounter{}
}

const K int = 3000

func findKey(this *RecentCounter, t int) int {

	for i := this.point; i < len(this.beforeTm); i++ {
		if this.beforeTm[i]+K >= t {
			this.point = i
			return len(this.beforeTm) - i + 1
		}
	}
	return 1
}

func (this *RecentCounter) Ping(t int) int {

	this.cn = 1
	for _, v := range this.beforeName {
		if this.curName == v {
			this.cn = findKey(this, t)
			break
		}
	}
	this.beforeName = append(this.beforeName, this.curName)
	this.beforeTm = append(this.beforeTm, t)
	return this.cn
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
