//libadd.go
package main

import "C"

//export add
func add(left, right *C.char) *C.char {
	merge := C.GoString(left) + C.GoString(right)
	return C.CString(merge)
}

func main() {
}
