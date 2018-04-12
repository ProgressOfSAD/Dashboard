# 数据库字段说明文档

数据库中一共有7个表，该文档对这7个表的不同字段进行说明。字段的类型都是Django model里定义的类型

## UserInfo
该表用于存储用户注册时候以及之后认证的信息

序号|字段|类型|描述|其他
-|-|-|-|-
1|user_id|AutoField|用户的Id，由系统自动创建，用户的唯一标识|作为primary_key使用
2|name|CharField|用户注册时填写的名字|最大长度为16个字符
3|password|CharField|用户账号的密码|存储时使用MD5进行Hash
4|email|CharField|用户的邮箱|通过邮箱注册用户
5|gender|NullBooleanField|用户的性别|默认为NULL
6|phone|CharField|用户的电话号码|非必须
7|auth|BinaryField|用户是否经过认证，需要线下认证|默认为False，非必须
8|auth_info|CharField|用户的认证信息，用户认证时提供的信息|认证用户需要
9|real_name|CharField|用户的真实姓名|非必须
10|other|TextField|用户的其他信息，如自我介绍|

## UserExtended
该表用于记录用户的一些动态信息，包括各种书籍列表，不同的信用信息等

序号|字段|类型|描述|其他
-|-|-|-|-
1|user_id|OneToOneField|用户id，与UserInfo.user_id相同|
2|collection|TextField|用户收藏的书籍列表|存储书籍的id,不同id之间用","隔开
3|borrow_credit|IntegerField|记录用户借书的信用信息，用户不按期归还书籍，损坏书籍会导致信用降低|信用等级从0到5，等级过低时无法借到书籍，默认为5
4|comment_credit|IntegerField|记录用户对书籍做出评价的可靠性，用户的评价被越多人举报，可靠性越低|等级从0到5，等级过低时无法评价书籍，默认为5
5|report_credit|IntegerField|记录用户举报评论的有用性，随意举报评论会导致有用性降低|等级从0到5，等级过低时无法举报评论，默认为5

## ManagerInfo
该表用于记录管理员的信息，只能通过超级管理员手动添加

序号|字段|类型|描述|其他
-|-|-|-|-
1|manager_id|AutoField|管理员的id，管理员的唯一标识|作为primary_key使用
2|name|CharField|管理员的名字|
3|password|CharField|管理员账号的密码|存储时使用MD5进行hash
4|gender|NullBooleanField|管理员的性别|
5|email|EmailField|管理员的邮箱|
6|phone|CharField|管理员的电话号码|
7|other|TextField|其他信息，如个人简介|

## BookInfo
该表用于记录不同书籍的一些基本信息，这些信息一般保持不变

序号|字段|类型|描述|其他
-|-|-|-|-
1|bookid|AutoField|书籍的id，唯一标识符|作为primary_key使用
2|ISBN|CharField|书籍的ISBN编号|
3|name|CharField|书籍的名称|
4|author|CharField|书籍的作者|
5|brief|TextField|书籍的简介|
6|publish_time|CharField|出版时间|
7|press|CharField|出版社
8|type|CharField|书籍所属的类型|记录类型的id,不同id之间用","隔开

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

## TypeList
该表用于表示不同类型的id编号以及该类型的详细名称

序号|字段|类型|描述|其他
-|-|-|-|-
1|type_id|IntegerField|书籍类型的id|不同的书籍类型对应不同的id，默认为0
2|type_name|CharField|书籍类型的名称|例如计算机，传记等等

## Comment
该表用于记录用户的评论

序号|字段|类型|描述|其他
-|-|-|-|-
1|models_id|CharField|该条评论的唯一标识|长度为64
2|user_id|ForeignKey|该条评论的评论人员的id|
3|book_id|ForeignKey|该评论所评论的书籍的id|
4|reported_times|IntegerField|评论被举报的次数|被举报次数过多会被删除
5|comment_time|CharField|评论的时间|
6|contend|TextField|评论的内容|
7|agree|IntegerField|赞同该评论的人数|默认为0
8|disagree|IntegerField|不赞同该评论的人数|默认为0

## User_Book
该表用于记录用户预订书籍，借书和还书的一些信息

序号|字段|类型|描述|其他
-|-|-|-|-
1|user_id|ForeignKey|本条记录对应的用户id|
2|book_id|ForeignKey|本条记录对应的书籍的id|
3|time|CHarField|该条记录提出/操作的时间|预订、借书、还书的时间
4|state|IntegerField|相关操作|例如没有操作(0),预订(1),借(2),归还(3)

## ScoreToBook
该表用户记录不同用户对不同书籍的评分

序号|字段|类型|描述|其他
-|-|-|-|-
1|user_id|ForeignKey|评分者|
2|book_id|ForeignKey|评分的书籍|与user_id一起作为联合主键
3|score|IntegerField|评分|

## AgreeDisagree
该表用于记录不同用户对不同评论的agree或者disagree情况，包括举报

序号|字段|类型|描述|其他
-|-|-|-|-
1|comment_id|ForeignKey|评论的id|
2|user_id|ForeignKey|对该评论操作的用户
3|agree_disagree|NullBooleanField|赞同或者不赞同|可以为空
4|reported|CharField|对该评论进行举报时的理由|为空字符串表示没有举报
