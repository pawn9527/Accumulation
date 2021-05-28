# 切片，接口，时间和性能

## Slice 切片
```
type slice struct {
    array unsafe.Pointer  // 指向存放数据的数组指针
    len  int  // 长度有多大
    cap  int  // 容量有多大
}
```
![](https://static001.geekbang.org/resource/image/ea/80/eac9bc362064f5cba58d663d3dde8780.png)

```go
foo = make([]int, 5)
foo[3] = 42
foo[4] = 100

bar := foo[1:4]
bar[1] = 99
```
![](https://static001.geekbang.org/resource/image/fb/c6/fb0574yye57002dfc435efe9db3c88c6.png)

> foo 和 bar 的 内存是共享的。所以 foo 和 bar 对数组内容的修改都会相互影响

```
a := make([]int, 32)
b := a[1:16]
a = append(a, 1)
a[2] = 42
```
![](https://static001.geekbang.org/resource/image/9a/13/9a29d71d309616f6092f6bea23f30013.png)

append() 操作让 a 的容量变成了 64，而长度是 33。

**append()这个函数在cap不够用的时候，就会重新分配内存以扩大容量，如果够用，就不用重新分配内存**


```
path := []byte("AAAA/BBBBBBBB")
sepIndex := bytes.IndexByte(path, '/')

dir1 := path[:sepIndex]    // => AAAA
dir2 := path[sepIndex+1:]  // => BBBBBBBB

dir1 = append(dir, "suffix"...)

dir1   // => AAAAsuffix
dir2   // => uffixBBBB
```
![](https://static001.geekbang.org/resource/image/17/aa/1727ca49dfe2e6a73627a52a899535aa.png)

> 修改此Bug
> dir1 := path[:sepIndex] ==修改为==>  path[:sepIndex:sepIndex]

## 深度比较

如果我们需要比较两个结构体中的数据是否相同，就要使用深度比较
使用 反射 reflect.DeepEqual() 来进行比较

```
	v1 := []int{}
	v2 := []int{}
	fmt.Println("v1 == v2:", reflect.DeepEqual(v1, v2))  // true

	m1 := map[string]string{"one": "a", "two": "b"}
	m2 := map[string]string{"two": "b", "one": "a"}

	fmt.Println("m1 == m2", reflect.DeepEqual(m1, m2))  // true

	s1 := []int{1, 2, 3}
	s2 := []int{1, 2, 3}
	fmt.Println("s1 == s2:", reflect.DeepEqual(s1, s2))  // true
```
## 接口编程

```
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

d1 := Country{"USA"}
d2 := City{"Los Angeles"}
PrintStr(d1)
PrintStr(d2)
```
面向对象编程方法的黄金法则 ---- Program to an inferface not an implementation

## 接口完整性检查


```
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

 
// func (s *Square) Area() int {
// 	return 5
// }

s := Square{len: 5}
fmt.Printf("%d\n", s.Sides())  // 4
```
Square 并没有实现 Shape 接口的所有方法，但是程序可以跑通，但是这样的编程方式并不严谨。

**强制实现接口的所有方法**
```
var _ Shape = (*Square)(nil)
```

## 时间

Go 使用 time.Time  和 time.Duration 这两种类型。

- 在命令行上，flag通过 time.ParseDuration 支持了 time.Duration
- JSON 中的 encoding/json 中也可以把 time.Time 编码成 RFE 3339的格式。
- 数据库使用的 database/sql 也支持把 DATATIME 或 TIMESTAMP 类型转成time.Time
- YAML 也可以使用 gopkg.in/yaml.v2 支持 time.Time, time.Duration 和 REC 3339 格式。

最后，如果你要做全球化跨时区的应用，一定要把所有服务器和时间全部使用 UTC 时间。

## 性能提示

- 如果需要把数字转换为字符串，使用 strconv.Itoa() 比 fmt.Sprintf() 要快一倍左右。
- 尽可能避免把String 转为[]Byte, 这个转换会导致性能下降
- 如果在for-loop 里对某个Slice 使用 append(), 先把Slice的容量扩充到位，这样可以避免内存重新分配以及系统自动按照 2 的 N 次方幂进行扩展但又用不到的情况，从而避免浪费内存。
- 使用StringBuffer 或是 StirngBuild 来拼接字符串，性能会比使用 + 或者 += 高三到四个数量级。
- 尽可能使用并发的 goroutine, 然后使用 sync.WaitGroup 来同步分片操作。
- 避免在热代码中进行内存分配，这样会导致gc很忙。尽可能使用 sync.Pool 来重用对象。
- 使用 lock-free 的操作，避免使用mutex，尽可能使用 sync/Atomic包
- 使用 I/O 缓冲， I/O 是个非常非常慢的操作，使用 bufi.NewWrite()和 bufio.NewReader() 可以带来更高的性能。
- 对于在 for-loop 里的固定的正则表达式，一定要使用 regexp.Compile() 编译正则表达式。性能会提升两个数量级。
- 如果你需要更高性能的协议，就要考虑使用 protobuf 或者 msgp 而不是JOSN， 因为JSON的序列化和反序列化里使用了反射。
- 你在使用 Map 的时候，使用整型的 key 会比字符串的要快，因为整型比较比字符串比较要快。
