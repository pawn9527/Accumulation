**目录(Table of Contents)**
[TOCM]
[TOC]
# odoo 命令

创建模块: `./odoo-bin scaffold mymodule myaddons`

> mymodule 新建的模块名称
> myaddons 创建的所在的文件夹

权限设置: 文件夹权限 - 755;  文件权限 - 644


# odoo 中的一些坑

1. onchange 不能提交数据库

    - 问题: onchange 自动更新后, 点击保存不能存储到数据库
    - 原因: 字段中有 readonly 的设置, 表单提交不会提交对应字段
    - 解决: 删除对应的readonly 的限制
 
# odoo 设置说明

1. field 属性中的 option 的用法    

 
**Many2One widget (default)**

**option** : 对于Many2One 字段来控制 跳转,创建修改

    - no_quick_create
    - no_create_edit
    - no_create
    - no_open

**Example**
 
```xml
<field name="field_name" options="{'no_quick_create': True, 'no_open': True}"/>
```
 2 . TreeView 不同状态设置不同颜色
 
    - tree 中设置属性 colors
    
 **Example**
 ```xml
<record id="colors_tree_view" model="ir.ui.view">
    <field name="name">colors.tree.view</field>
    <field name="model">your.module</field>
    <field name="arch" type="xml">
        <tree string="Colors Tree" colors="blue:state == 'draft';gray:state in ('cancel','done');black:state == 'open'" >
            <field name="name"/>
        </tree>
    </field>
</record>
```
 3  . onchange 加载 one2Many 数据
 
    - 只需要给 one2Many 字段创建值
 
**Example**

```python
from odoo import api
@api.multi
@api.onchange
def _onchange_some_filed(self):
    for bom in self:
        note_ids = []
        for line in bom.bom_lines:
            note_ids.append(0, 0, {
                "name": "name",
                "field1": line.field1,
                "filed2": line.field2,
            })
        bom.update(note_ids=note_ids)
    return {'bom', 'bom'}     

```
> - (0, 0,  { values })    link to a new record that needs to be created with the given values dictionary
> - (1, ID, { values })    update the linked record with id = ID (write *values* on it)
> - (2, ID)                remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)
> - (3, ID)                cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)
> - (4, ID)                link to existing record with id = ID (adds a relationship)
> - (5)                    unlink all (like using (3,ID) for all linked records)
> - (6, 0, [IDs])          replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)

4  . odoo actions (windows actions)

    -  button or model mothed return window
    
 ```python
{
    "type": "ir.actions.act_window",
    "res_model": "product.product",
    "views": [[False, "form"]],
    "res_id": a_product_id,
    "target": "new",
}
```
> - res_model: 视图所呈现的视图
> - views: [[view_id, view_type]]  view_id 对应视图的id, view_type 对应视图的类型(tree, form) 
> - res_id(可选): 如果默认视图是form, 这个指定对应的某个视图, 否则为新建
> - search_view_id(可选): (id, name) id - 对应的搜索视图的数据库标识符. 默认为获取模型的默认搜素视图
> - target (可选): current (主要区域)/ fullscreen(全屏模式)/ new (对话框or弹框) 默认--current 
> - context(可选): 给视图传递的上下文参数
> - domain(可选): 过滤所展示的视图的内容 (view_type为tree 居多)
> - limit(可选): 列表中展示的条数, 默认为80条
> - auto_search(可选): 是否在加载默认视图后默认搜索

**Example**

展示 customer 的列表和表单 (model: res.partner)

```json
{
  "type": "ir.actions.act_windows",
  "res_model": "res.partner",
  "views": [[False, "tree"],[False, "form"]],
  "domain": [[customer, "=", true]]
}
```
还有上文的, id 为 a_product_id 的视图展示页面

5  . 如何指定对应的 tree and form 视图
   -  model:  ir.actions.act_window
   
Partner:

```xml
<record id="base.action_partner_form" model="ir.actions.act_window">
    <field name="name">Customers</field>
    <field name="type">ir.actions.act_window</field>
    <field name="res_model">res.partner</field>
    <field name="view_type">form</field>
    <field name="view_mode">tree,form,kanban</field>
    <field name="domain">[('customer','=',1)]</field>
    <field name="context">{'default_customer':1, 'search_default_customer':1}</field>
    <field name="search_view_id" ref="base.view_res_partner_filter"/>
    <field name="filter" eval="True"/>
    <field name="help" type="html">
        <p class="oe_view_nocontent_create">
            Click to add a contact in your address book.
        </p><p>
            OpenERP helps you easily track all activities related to
            a customer: discussions, history of business opportunities,
            documents, etc.
        </p>
    </field>
</record> 
```
修改视图的序列
```xml
<record id="base.action_partner_tree_view1" model="ir.actions.act_window.view">
    <field name="sequence" eval="0"/>
    <field name="view_mode">tree</field>
    <field name="view_id" ref="base.view_partner_tree"/>
    <field name="act_window_id" ref="base.action_partner_form"/>
</record>
<record id="base.action_partner_form_view2" model="ir.actions.act_window.view">
    <field eval="1" name="sequence"/>
    <field name="view_mode">form</field>
    <field name="view_id" ref="base.view_partner_form"/>
    <field name="act_window_id" ref="base.action_partner_form"/>
</record>
<record id="base.action_partner_form_view1" model="ir.actions.act_window.view">
    <field eval="2" name="sequence"/>
    <field name="view_mode">kanban</field>
    <field name="view_id" ref="base.res_partner_kanban_view"/>
    <field name="act_window_id" ref="base.action_partner_form"/>
</record>
```

## TODO 没时间整理

好的博文:  odoo onchange 所有返回类型 [传送门](https://www.odoo.com/forum/how-to/developers-13/what-should-onchange-methods-do-and-return-57760)


Field Widgets

1.1  Text Field Widgets
   - email
   - url 
   - html

1.2  Numeric Fields
   - handle
   - float_time 
   - monetary  货币金额
   - progressbar  进度条

1.3  For relational and selection fields

   - many2many_tags
   - selections   use many2one field (default)
   - radio  
   - priority   
   - state_selection or kanban_state_selection    
   
