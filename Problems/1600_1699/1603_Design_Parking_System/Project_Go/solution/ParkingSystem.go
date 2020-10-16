package solution

// 40ms

type ParkingSystem struct {
    Slot []int
}


func Constructor(big int, medium int, small int) ParkingSystem {
    return ParkingSystem{[]int{ 0, big, medium, small } }
}


func (this *ParkingSystem) AddCar(carType int) bool {
    if this.Slot[carType] > 0 {
        this.Slot[carType]--
        return true
    }
    return false
}


/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */
