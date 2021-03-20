# MySQL实践

## 01. 普通索引和唯一索引

>普通索引:   (由关键字Key或 Index 定义的索引) 的唯一任务就是加快对数据的访问速度, 因此应该只为那些经常出现的查询条件(Where) 或者排序条件(order by) 中的数据创建索引
>
>唯一索引:  创建索引的时候应该用关键字 UNIQUE 把它定义为一个唯一索引, 唯一索引可以保证数据记录的唯一性.

![img](https://static001.geekbang.org/resource/image/1e/46/1ed9536031d6698570ea175a7b7f9a46.png)

