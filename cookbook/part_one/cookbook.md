###  collections.defaultdict
not use defaultdict
```python
pairs = {}
d = {}
for key,value in pairs:
    if key not in key:
        d[key] = []
    d[key].append(value)
```
use defaultdict
```python
pairs = {} # have many data dict
from collections import  defaultdict
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
```
### Keeping Dictionaries in Order

```python
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
d
> OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])
```
> - OrderedDict 内部维护了一个双线列表, 它会根据元素加入的顺序来排列键的位置,
第一个加入的元素被放在链表的末尾
> - OrderedDict 是普通dict 的两倍, 注意内存占用问题


### Calculating With Dictionaries

1 . 最大值 最小值 排序
```python
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
# (45.23, 'ACME'), (205.55, 'IBM'),
# (612.78, 'AAPL')]
```
> - zip() 创建了一个迭代器, 其中的内容只能使用一次
> - 比较的时候同样的可以使用 zip() 将key values 对换

### Finding Commonalities In Two Dictionaries
dict.keys()  
dict.items() 都可以进行集合操作
```python
a = {
 'x' : 1,
 'y' : 2,
 'z' : 3
}

b = {
 'w' : 10,
 'x' : 11,
 'y' : 2
}
# find keys in common
a.keys() & b.keys()  # { 'x', 'y' }

# find keys in a are not in b
a.keys() - b.keys()  # { 'z' }

# find (key, value) pairs in common
a.items() & b.items() # { ('y', 2) }

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}
```
> - 字典的keys 方法会返回keys-view的对象
> -  keys(), 以及 items() 都可以使用 并集, 交集和 差集

### Removing Duplicates form a Sequence while Maintaining Order
1 . 序列中的值是可 hashable 
```python
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a)) 
# [1, 5, 2, 9, 10]
```
2 . 序列中不可 hash
```python
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

list(dedupe(a, key=lambda d: (d['x'],d['y'])))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
```
> - set(list)的方式会打乱 list的顺序

### Naming a Slice

```python

PRICE = slice(40, 48)  # 命名切片
```
> - 使用 indices(size) 方法将切片映射到特定大小的序列上. 返回一个(start, stop, step)元组

```python
 # 这个待定, 没怎么搞懂是干什么的...
 s = 'Hello World'
 a.indices(len(s))
```

### Determining the Most Frequently Occurring Items In a Sequence
1 . 普通用法
```python
words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

# 特殊用法
morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)

# Counter 可用于 + - 运算
a = Counter(words)
b = Counter(morewords)
# Combine counts
c = a + b
# Subtract counts
d = a - b
```
### Sorting a List of Dictionaries by a Common key
```python
from operator import itemgetter
rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
# 使用 lambda 函数
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
# min 和 max 函数同样适用
min(rows, key=itemgetter('uid'))
max(rows, key=itemgetter('uid'))
```
> - sorted 配合 itemgetter 进行字典的公共键来排序
> - 实际上 sorted 需要的是 一个 callable 的对象, itemgetter 就是创建一个这样的对象同理 lambda 也可以实现
> - 还有 min 和 max 函数
### Sorting Objects Without Native Comparison Support

**原理**: 使用sorted可以使用 ke参数进行排序, 可以调用该对象中的可排序对象 
```python
from operator import attrgetter
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return f'User({self.user_id})'
users = [User(23), User(3), User(99)]
sorted(users, key=lambda x: x.user_id)
sorted(users, key=attrgetter('user_id'))

by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

min(users, key=attrgetter('user_id'))

max(users, key=attrgetter('user_id'))
```
> - attrgetter 的效率比 lambda 函数快点
> - 同样支持 多字段综合排序, 以及 min 和 max 函数

### Grouping Records Together Based on a Field

**itertools.groupby()进行数据分组**

```python
from operator import itemgetter
from itertools import groupby

rows = [
 {'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
        
# 使用 defaultdict 整理数据
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
 rows_by_date[row['date']].append(row)
```
**结果:**
```python
'''
07/01/2012
 {'date': '07/01/2012', 'address': '5412 N CLARK'}
 {'date': '07/01/2012', 'address': '4801 N BROADWAY'}
07/02/2012
 {'date': '07/02/2012', 'address': '5800 E 58TH'}
 {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}
 {'date': '07/02/2012', 'address': '1060 W ADDISON'}
07/03/2012
 {'date': '07/03/2012', 'address': '2122 N CLARK'}
07/04/2012
 {'date': '07/04/2012', 'address': '5148 N CLARK'}
 {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}
'''
```
> - 使用 defaultdcit 也可以进行数据的整理

# Filtering Sequence Elements
**原理**: 使用列表推导式, 生成器表达式来筛选, 配合 filter() 和compress() 函数
```python
from itertools import compress
addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK'
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
# [False, False, True, False, False, True, True, False]
list(compress(addresses, more5))
# ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
```
> - filter() 和 compress() 都会返回一个迭代式 
# Extracting a Subset of Dictionary
**原理**: 使用字典推导式
```python
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
    
# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }
```
# Mapping Names to Sequence Elements
**原理**: collections.namedtuple() [命名元组] 工厂化方法
```python
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
# Subscriber(addr='jonesy@example.com', joined='2012-10-19')
sub.addr
# 'jonesy@example.com'

```
> - 一种格式化的工厂(封装后的class), 封装后代码更加规范.
> - 可以解耦
> - 不支持 直接赋值操作, 只能用着 _replace() 方法
> - _replace() 类似 copay()方法 创建一个新的对象重新赋值
```python

# 元组标准化的使用
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
# 不支持 直接赋值操作
s = Stock('ACME', 100, 123.45)
s.shares = 75 # Error
# 只能使用 _replace() 方法
s = s._replace(shares=75)
# Stock(name='ACME', shares=75, price=123.45)

# 另种使用(比较鸡肋)
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)
# Stock(name='ACME', shares=100, price=123.45, date=None, time=None)    
```
**总结**
> - namedtuple 相当于 dict 的替代品, 在处理大量数据的时候更加高效, 
但是修改麻烦, 所以适合做映射不适合操作.

# Transforming and Reducing Data at the Same Time

**原理**: 综合使用 先筛选后运算
```python
nums = [1, 2, 3, 4, 5]
# 两者表达的同一种意思
s = sum((x * x for x in nums)) # Pass generator-expr as argument
s = sum(x * x for x in nums) # More elegant syntax


# nums 重新赋值 如果 nums 很大 则影响效率(系统分配空间, 而且只是用一次比较浪费)
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])


portfolio = [
 {'name':'GOOG', 'shares': 50},
 {'name':'YHOO', 'shares': 75},
 {'name':'AOL', 'shares': 20},
 {'name':'SCOX', 'shares': 65}
]
# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
```
> - min 函数也可以制定 key 值对dcit进行筛选

# Combining Multiple Mapping into a Single Mapping

**原理**: 使用 collections.ChainMap() 方法合并以及和 dict.update()的区别
```python
from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a,b)
# 需要注意的是有重复, 获取前一个
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)
list(c.keys()) # ['x', 'z', 'y']
# 修改也会作用在第一个映射上面
c['z'] = 10
c['w'] = 40
a # {'z': 10, 'w': 40}
```
- ChainMap与带有作用域(全局,局部变量)的配合 更加合理
```python
from collections import ChainMap
values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
values # ChainMap({'x': 2}, {'x': 3}, {'x': 1})
 # Discard last mapping
values = values.parents
values['x'] # 1
# Discard last mapping
values = values.parents
values['x'] # 3
values # ChainMap({'x': 2})
```
ChainMap 和 dict.update() 对比
> - ChainMap 修改合并前的集合 会同时修改合并后的
> - dict.update() 修改不会映射过去
```python
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged # {'y': 2, 'z': 3, 'x': 1}
merged.update(a)
a['x'] = 13
# 修改合并前的数值 合并后不变
merged # {'y': 2, 'z': 3, 'x': 1}


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
from collections import ChainMap
merged = ChainMap(a, b)
a['x'] = 42
# 随着修改前变化
merged['x']  # 42
```