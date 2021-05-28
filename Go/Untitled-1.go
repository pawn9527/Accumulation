package main

import (
	"encoding/binary"
	"fmt"
	"io"
	"reflect"
)

type Country struct {
	Name string
}

type City struct {
	Name string
}

type Stringable interface {
	ToString() string
}

func (c Country) ToString() string {
	return "Conutry = " + c.Name
}

func (c City) ToString() string {
	return "City = " + c.Name
}

func PrintStr(p Stringable) {
	fmt.Println(p.ToString())
}

// 完整性

type Shape interface {
	Sides() int
	Area() int
}

type Square struct {
	len int
}

func (s *Square) Sides() int {
	return 4
}

func (s *Square) Area() int {
	return 5
}

type Point struct {
	Longitude     float64
	Latitude      float64
	Distance      float64
	ElevationGain float64
	ElevationLoss float64
}

func parse(r io.Reader) (*Point, error) {
	var p Point
	var err error
	read := func(data interface{}) {
		if err != nil {
			return
		}
		err = binary.Read(r, binary.BigEndian, data)
	}
	read(&p.Longitude)
	read(&p.Latitude)
	read(&p.Distance)
	read(&p.ElevationGain)
	read(&p.ElevationLoss)

	if err != nil {
		return &p, err
	}
	return &p, nil
}

func main() {
	v1 := []int{}
	v2 := []int{}
	fmt.Println("v1 == v2:", reflect.DeepEqual(v1, v2))

	m1 := map[string]string{"one": "a", "two": "b"}
	m2 := map[string]string{"two": "b", "one": "a"}

	fmt.Println("m1 == m2", reflect.DeepEqual(m1, m2))

	s1 := []int{1, 2, 3}
	s2 := []int{1, 2, 3}
	fmt.Println("s1 == s2:", reflect.DeepEqual(s1, s2))

	d1 := Country{"USA"}
	d2 := City{"Los Angeles"}
	PrintStr(d1)
	PrintStr(d2)

	s := Square{len: 5}
	fmt.Printf("%d\n", s.Sides())

	var _ Shape = (*Square)(nil)
}
