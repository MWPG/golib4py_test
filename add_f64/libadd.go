//libadd.go
package main

import "C"

//export add
func add(left, right C.double) C.double {
	merge := float64(left) + float64(right)
	return C.double(merge)
}

func main() {
}
