# MySQL基础概念

## 01|基础架构

### 逻辑架构图

![img](https://static001.geekbang.org/resource/image/0d/d9/0d2070e8f84c4801adbfa03bda1f98d9.png)

> MySQL 可以分为Server 层和存储索引擎层两部分呢

- Server 层包括连接器，查询缓存，分析器，优化器， 执行器等，涵盖MySQL的大多数核心服务功能，以及所有的内置函数(如内容，时间，数学和加密函数等)， 所有跨存储引擎的功能都在这一层实现，比如存储过程，触发器，视图等。
- 存储引擎  负责数据的存储和提取。

### 连接器

> 连接器负责跟客户端建立链接，获取权限，维持和管理连接。

```shell
mysql -h$ip -P$port -u$user -p
```

- 链接失败， 客户端程序结束执行
- 链接成功，连接器会到权限表里面查出你拥有的权限。 之后，这个连接里面的权限判断逻辑，都将依赖此时读到的权限。

### 查询缓存

MySQL 拿到一个查询请求后，会先到查询缓存看看，之前是不是执行过这条语句。之前执行过的语句以及结果可能以 key-value 对的形式， 被直接缓存在内存中。

**查询缓存的失效非常频繁，只要有对一个表的更新，这个表所有的查询缓存都会被清空**

禁用查询缓存:

​	将 query_cache_type 设置为  DEMAND

> MySQL 8.0 已经移除查询缓存

### 分析器

分析器先会做“语法分析”， 语法分析器会根据语法规则，判断你输入的这个SQL 语句是否满足MySQL 语法

```mysql

mysql> elect * from t where ID=1;

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'elect * from t where ID=1' at line 1
```

### 优化器

> 优化器是表里面有多个索引的时候，决定使用那个索引; 或者在一个语句有多表关联(join)的时候，决定各个表的连接顺序。

### 执行器

1. 校验权限
2. 会根据表的引擎定义，去使用这个引擎提供的接口
3. 将执行结果集合返回给客户端

## 02|日志系统

### redo  log (重做日志)

**redo log 是InnoDB 引擎特有的日志**

当有一条记录需要更新的时候 InnoDB引擎就会先把记录写到 redo log 里面，并更新内存， 这个时候更新就算完成了。 同时，InnoDB 引擎会在适当的时候，将这个操作记录更新到磁盘里面。

redo log  写入规则

​	则 redo log  从头开始写，写到末尾就又回到开头循环写

![img](https://static001.geekbang.org/resource/image/16/a7/16a7950217b3f0f4ed02db5db59562a7.png)

write pos 是当前记录的位置， 一边写一边后移

checkpoint 是当前要擦除的位置， 也是往后推移并且循环的， 擦除记录前要记录更新到数文件

有了 redo log，InnoDB 就可以保证即使数据库发生异常重启，之前提交的记录都不会丢失，这个能力称为 **crash-safe**。

### binlog (归档日志)

binlog 是 MySQL  Server层的日志。

binlog  两种模式

- statement 格式的话是记SQL 语句的
- row 格式会记录行的内容， 记录两条， 更新前和更新后都有

binlog 和 redo log 三点不同

- redo log 是 InnoDB 引擎特有的；binlog 是 MySQL 的 Server 层实现的，所有引擎都可以使用。
- redo log 是物理日志，记录的是“在某个数据页上做了什么修改”；binlog 是逻辑日志，记录的是这个语句的原始逻辑，比如“给 ID=2 这一行的 c 字段加 1 ”。
- redo log 是循环写的，空间固定会用完；binlog 是可以追加写入的。“追加写”是指 binlog 文件写到一定大小后会切换到下一个，并不会覆盖以前的日志。

![img](https://static001.geekbang.org/resource/image/2e/be/2e5bff4910ec189fe1ee6e2ecc7b4bbe.png)

浅色框 表示是在InnoDB 内部执行的

深色框 表示是在执行器中执行的

**redo log 将写入拆分为两个步骤: prepare 和 commit**

> 如果不使用“两阶段提交” 那么数据库的状态就有可能和用它的日志恢复出来的库的状态不一致

## 03| 事务隔离

### 隔离性与隔离级别

事务特性:  ACID(Atomicity, Consistency, Isolation, Durability, 即原子性，一致性，隔离性, 持久性)

SQL 标准的事务隔离级别

- 读未提交(read uncommitted):  一个事务还没提交时，它做的变更就能被别的事务看到。
- 读提交(read committed): 一个事务提交之后，它做的变更才会被其他事务看到。
- 可重复读(repeatable read): 一个事务执行过程中看到的数据，总是跟这个事务在启动时看到的数据是一致的。当然在可重复读隔离级别下，未提交变更对其他事务也是不可见的
- 串行化(serializable)  顾名思义是对于同一行记录，“写”会加“写锁”，“读”会加“读锁”。当出现读写锁冲突的时候，后访问的事务必须等前一个事务执行完成，才能继续执行。

eg:  假设数据表 T 中只有一列，其中一行的值为 1，下面是按照时间顺序执行两个事务的行为。

```mysql
mysql> create table T(c int) engine=InnoDB;
insert into T(c) values(1);
```

![img](https://static001.geekbang.org/resource/image/7d/f8/7dea45932a6b722eb069d2264d0066f8.png)

- 若隔离级别是: 读为提交 

  v1=2  这个时候B还未提交，但是结果已经被A看到了因此，V2, V3 也都是2

- 若隔离级别是: 读提交  

  则 v1 = 1  v2 = 2  事务B的更新在提交后才能被A看到， 所以V3 的值也是2

- 若隔离级别是: 可重复读

  则 v1 = v2 = 1  v3 = 2 之所以 v2 还是1, 遵循的就是这个要求: 事务在执行期间看到的数据前后必须是一致的

- 若隔离级别是: 串行化

  则在事务B执行 “将1改为2”的时候， 会被锁住。 直到事务A提交之后， 事务B才可以继续执行。所以从A的角度看，v1 v2 值是1， v3 的值是 2

不同的事务隔离级别 对应的干扰

| 隔离级别 | 脏读 | 不可重复读 | 幻读 |
| :------: | :--: | :--------: | :--: |
| 读未提交 |  √   |     √      |  √   |
|  读提交  |  ×   |     √      |  √   |
| 可重复读 |  ×   |     ×      |  √   |
|  串行化  |  ×   |     ×      |  ×   |

### 事务隔离的实现

 在 MySQL 中，实际上每条记录在更新哦时候都会同时记录一条回滚操作。记录上的最新的值，通过回滚操作，都可以得到前一个状态的值。

![img](https://static001.geekbang.org/resource/image/d9/ee/d9c313809e5ac148fc39feff532f0fee.png)

### 事务的启动方式

1. 显式启动事务语句:  begin 或 start transaction。 配套的提交语句是commit, 回滚语句是 rollback
2.  set autocommit =0 , 这个命令会将这个线程的自动提交关掉。意味 着你只执行一个select 语句，这个事务就启动了，而且并不会自动提交。这个事务持续存在直到你主动执行commit 或  rollback 语句， 或者断开连接。

如何查找长事务.

在  information_schema 库的 innodb_trx 这个表中查询长事务，比如这个

这个语句，用于查找持续时间超过60s的事务。

```mysql

select * from information_schema.innodb_trx where TIME_TO_SEC(timediff(now(),trx_started))>60
```

