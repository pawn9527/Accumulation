### Mongodb Aggregation 聚合
```
db.orders.aggregate([
    {$math: {status: "A"}},
    {$group: {_id: "$cust_id", total: {$sum: "$amount"}}}
])
```
![](https://docs.mongodb.com/manual/_images/aggregation-pipeline.bakedsvg.svg)

### Single Aggregation  单聚合
```
db.collection.estimatedDocumentCount(),
db.collection.count(),
db.collection.distinct().
```
![](https://docs.mongodb.com/manual/_images/distinct.bakedsvg.svg)

### Aggregation - $unwind 操作符:

- 如果文档中含有 array 类型的字段, 并且其中包含多个元素, 
使用 $unwind 操作符会根据元素数量输出多个文档, 每个文档的array字段中 仅包含 array 中的的单个元素

```
db.getCollection("12-28").aggregate({
    $math: {
        'gas_flow.id': 1
    },
    {
        $unwind: "$gas_flow"
    }
})
```
### Aggregation - $filter
