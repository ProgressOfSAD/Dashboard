# 数据库字段说明文档

数据库中一共有10个表，该文档对这7个表的不同字段进行说明。字段的类型都是Django model里定义的类型

## UserInfo
该表用于存储用户注册时候以及之后认证的信息

序号|字段|类型|描述|其他
-|-|-|-|-
1|id|AutoField|用户的Id，由系统自动创建，用户的唯一标识|作为primary_key使用
2|username|CharField|用户注册时填写的名字|最大长度为16个字符
3|password|CharField|用户账号的密码|存储时使用MD5进行Hash
4|email|CharField|用户的邮箱|通过邮箱注册用户
5|gender|NullBooleanField|用户的性别|默认为NULL
6|phone|CharField|用户的电话号码|非必须
7|auth|BinaryField|用户是否经过认证，需要线下认证|默认为False，非必须
8|auth_info|CharField|用户的认证信息，用户认证时提供的信息|认证用户需要
9|real_name|CharField|用户的真实姓名|非必须
10|other|TextField|用户的其他信息，如自我介绍|
11|collections|ManyToManyField|用户的书籍收藏列表|关联BookInfo表  

<!--
## UserExtended  
该表用于记录用户的一些动态信息，包括各种书籍列表，不同的信用信息等

序号|字段|类型|描述|其他  
-|-|-|-|-  
1|user_id|OneToOneField|用户id，与UserInfo.user_id相同|  
2|collection|TextField|用户收藏的书籍列表|存储书籍的id,不同id之间用","隔开  
3|borrow_credit|IntegerField|记录用户借书的信用信息，用户不按期归还书籍，损坏书籍会导致信用降低|信用等级从0到5，等级过低时无法借到书籍，默认为5  
4|comment_credit|IntegerField|记录用户对书籍做出评价的可靠性，用户的评价被越多人举报，可靠性越低|等级从0到5，等级过低时无法评价书籍，默认为5  
5|report_credit|IntegerField|记录用户举报评论的有用性，随意举报评论会导致有用性降低|等级从0到5，等级过低时无法举报评论，默认为5
-->

## ManagerInfo
该表用于记录管理员的信息，只能通过超级管理员手动添加

序号|字段|类型|描述|其他
-|-|-|-|-
1|id|AutoField|管理员的id，管理员的唯一标识|作为primary_key使用
2|username|CharField|管理员的名字|
3|password|CharField|管理员账号的密码|存储时使用MD5进行hash
4|gender|IntegerField|管理员的性别|0:保密,1:男,2:女
5|email|EmailField|管理员的邮箱|
6|phone|CharField|管理员的电话号码|
7|other|TextField|其他信息，如个人简介|

## BookInfo
该表用于记录不同书籍的一些基本信息，这些信息一般保持不变

序号|字段|类型|描述|其他
-|-|-|-|-
1|id|AutoField|书籍的id，唯一标识符|作为primary_key使用
2|ISBN|CharField|书籍的ISBN编号|
3|name|CharField|书籍的名称|
4|author|CharField|书籍的作者|
5|brief|TextField|书籍的简介|
6|publish_time|CharField|出版时间|
7|press|CharField|出版社
8|types|ManyToManyField|书籍所属的类型|关联TypeInfo表，一本书有多种类型
9|cover|CharField|书籍封面|使用url表示
10|score|IntegerField|书籍的评分|0-5
11|contents|TextField|书籍的目录|

<!--
## BookExtended
该表用于记录书籍的一些动态信息，如评分，浏览次数，库存等

序号|字段|类型|描述|其他
-|-|-|-|-
1|book_id|OneToOneField|书籍id，与BookInfo.book_id相同|
2|score1|IntegerField|对该书籍评分为1的人数|默认为0，书用户对籍的评分从1到5
3|score2|IntegerField|对该书籍评分为2的人数|默认为0
4|score3|IntegerField|对该书籍评分为3的人数|默认为0
5|score4|IntegerField|对该书籍评分为4的人数|默认为0
6|score5|IntegerField|对该书籍评分为5的人数|默认为0
7|browsing_times|IntegerField|浏览次数|默认为0
8|state|IntegerField|书籍的状态|其中0为正常，1为被预定，2为被借出
-->

## TypeInfo
该表用于表示不同类型的id编号以及该类型的详细名称

序号|字段|类型|描述|其他
-|-|-|-|-
1|id|IntegerField|书籍类型的id|不同的书籍类型对应不同的id，默认为0
2|name|CharField|书籍类型的名称|例如计算机，传记等等

## Comment
该表用于记录用户的评论

序号|字段|类型|描述|其他
-|-|-|-|-
1|id|AutoField|该条评论的唯一标识|
2|uid|ForeignKey|该条评论的评论人员的id|与UserInfo相关联
3|bid|ForeignKey|该评论所评论的书籍的id|与BookInfo相关联
4|comment_time|DateTimeField|评论的时间|
5|content|TextField|评论的内容|
6|parent_comment|ForeignKey|评论对象的id|为0表示对这本书进行评论，其他表示Comment对象的id

## ScoreToBook
该表用户记录不同用户对不同书籍的评分

序号|字段|类型|描述|其他
-|-|-|-|-
1|uid|ForeignKey|评分者|使用UserInfo作为外键
2|bid|ForeignKey|评分的书籍|使用BookInfo作为外键，与uid一起作为联合主键
3|score|IntegerField|评分|选择为1-5

## AttitudeRecord
该表用于记录不同用户对不同评论的agree或者disagree情况，包括举报

序号|字段|类型|描述|其他
-|-|-|-|-
1|cid|ForeignKey|评论的id|与Comment表关联
2|uid|ForeignKey|对该评论操作的用户|与UserInfo表相关联，与cid作为联合主键
3|attitudee|IntegerField|赞同，不赞同或者举报|分别对应0, 1, 2
4|report_reasonIntegerField|对该评论进行举报时的理由|共有8种选择

## BookInstance
该表用于记录不同书籍的当前状态

序号|字段|类型|描述|其他
-|-|-|-|-
1|bid|ForeignKey|书籍的id|与BookInfo相关联
2|state|IntegerField|书籍的状态|0:正常,1:被预约,2:被借出

## ActiveRecord
该表用于记录用于的一些预约，借阅和归还记录

序号|字段|类型|描述|其他
-|-|-|-|-
1|uid|ForeignKey|用户的ID|与UserInfo表相关联
2|bid|ForeignKey|书籍的id|与BookInstance表相关联
3|active|IntegerField|操作类型|0:预约,1:借阅,2:归还
4|active_time|DateTimeField|记录产生的时间|
