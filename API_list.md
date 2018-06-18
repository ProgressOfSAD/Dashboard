# 软件架构
## 1. 总体设计
![](https://raw.githubusercontent.com/ProgressOfSAD/Dashboard/master/asset/overall_design.png)

## 2. 详细设计
### 2.1. 前端
####2.1.1读者系统前端详细设计
#### 总体思想
包含多个页面的单页应用，技术栈为vue+vuex+axios+iview。作为图书馆读者服务系统，主要提供为读者登录、注册、订阅、检索、查看书籍信息、评分书籍、评论书籍、收藏书籍、设置个人信息的9个功能。对这9个模块，里面也会分别有相应的子模块。
#### 模块设计
- 登录模块
在使用需要读者权限的模块功能时，检查cookie是否处于登录状态。如果没有登录，则在右上角点击登录，进入登录界面。
登录界面包括用户名，密码和验证码输入以及提交和退出按钮。在本地检查输入格式，如果符合格式则把用户名密码加密发送到服务器检查，登录成功后记录登录状态并跳转到原页面，否则提示账号密码错误。
- 注册模块
在登录界面上方菜单栏有切换到注册界面的按钮，点击进入注册界面。
登录界面包括用户名，密码，确认密码以及提交和退出按钮。用户名规定为邮箱注册，在本地检查输入格式无误后向服务器提交用户名密码，服务器检索数据库无重复账号后，发送确认邮件。注册成功则自动跳转到登录界面。
- 查看书籍信息模块
在首页或者检索、书架界面点击某本书籍条目后，可以进入书籍信息界面。
点击书籍条目，发送相应的书籍id到服务器，返回该书籍的所有信息。书籍信息包括书名，作者，ISBN，简介，出版社，出版日期，总体评分，评论区，收藏状态。
- 订阅模块
在一本书籍的信息界面内，有订阅的按钮。点击后，检查是否处于登录状态，是则跳出订阅确认框。
确认框内有确认订阅和取消的按钮，确认订阅则首先本地检查库存数量是否不为0，是则会发送用户id和书籍id到服务器进行确认，成功后返回书籍信息界面。否则提示图书库存不足订阅失败。
- 检索模块
系统左上是搜索栏，点击后可输入检索关键词。关键词可以是书名和作者名，提交检索字符串到后台后返回检索结果界面。
服务器会返回书籍信息列表，检索界面依据匹配相关度排序列出每本书籍条目，优先显示书名匹配结果，其次是作者匹配结果。
- 评分书籍模块
在一本书籍的信息界面内，有评分的单选框。一共是5星制，点击提交评分按钮后，会检查登录状态，向服务器发送用户id，书籍id和评分，成功后返回书籍界面。服务器会取平均评分返回，实时更新评分。
- 评论书籍模块（暂定）
在一本书籍的信息界面下方，是该书本的评论区。每个读者都可以发表对该书本的书评，并可以被回复、点赞或者举报。
实现类似于贴吧一样的效果。
- 收藏书籍模块
在一本书籍的信息界面内，有收藏该书的按钮。点击收藏后，会检查登录状态，向服务器发送用户id，书籍id和收藏状态。
在个人信息界面可以进入书架界面，里面显示所有用户收藏的书籍条目。在里面可以取消收藏。
- 设置个人信息模块
用户登录后，系统后上角显示个人头像，点击后可以进入个人信息界面。侧边栏有三个选项，分别是个人书架，书评记录，消息提醒，设置账号。
个人书架显示所有收藏的书籍；书评记录是所有个人的书评；消息提醒是收到回复或点赞后的提醒；设置账号包含设置头像，设置昵称，修改密码功能。


####2.1.2管理员系统前端详细设计 

- 总体思路

包含多个页面的单页应用，各个页面间使用 vue-router 进行跳转，所有页面的共用信息使用 vuex 进行管理。

- 设计图

![][1]

- 登录界面

  - 设计内容

    进入登录页面前先检查 cookie，如果是已登录用户，直接跳转到应用页面。

    登录界面包含两个 input 框和一个确认按钮。点击确认按钮会将用户名和密码发送到服务器。如果登录成功，进入应用页面。否则提示错误。本地检查用户名密码是否符合格式。

  - 接口信息

    提交 k-v 对：传输 k-v 给服务器，返回用户是否登录。

    提交 用户名密码：传输 用户名密码给服务器，返回是否登录成功。如果登录成功，返回 k-v 对。

- 应用界面

  - 侧边栏

  - 设计内容

    包含了所有页面的一个侧边栏

    通过点击进行页面转换

- 仪表盘

  - 设计内容
    包含管理员用户的基本信息
  - 接口信息
    获取 用户信息：获取已经登录用户的相关信息。

- 举报信息箱

  - 设计内容
    信息箱所有管理员用户共有。
    信息箱容纳了未处理的举报信息，并且以红点数字形式显示在侧边栏上。
    对于每个信息，可以点开查看具体被举报的评论。右下角两个按钮。“忽略”表示搁置举报信息，“确认删除”表示受理举报信息，同时删除被举报的评论。无论点击哪个，该举报信息都会被删除。
  - 接口信息
    - 获取 举报信息：获取所有举报信息，每个举报信息包含被举报评论的 ID 和举报理由。
    -  删除 被举报的评论：删除相应的评论。返回是否删除成功
    -  删除 举报信息：删除对应的举报信息。返回是否删除成功

- 库存管理

  - 设计内容
    分为两个tab。
    一个tab显示“增加条目”，包含所有需要填写的条目信息和确认增加按钮。本地会对格式进行检查。点击确认按钮后会将条目信息发送至服务器。
    另一个tab为“管理条目”，包含一个搜索框。通过提交搜索关键词，可以将相关的条目一一列出。点击相应条目，可以进入信息更改页面。点击确认更改，可向服务器发送更改条目信息的请求。
  - 接口信息
    - 提交 增加条目信息请求及信息：提交新增条目的内容。返回是否新增成功。
    - 提交 搜索关键词：提交搜索关键词，返回关键词关联的条目。
    - 提交 信息更改请求：提交条目的新信息，返回是否修改成功。

- 借阅 

  - 设计内容
    分为两个tab。
    一个tab显示“创建借阅请求”，通过填写信息进行借阅。
    另一个tab为“预约借阅”，查询用户名，获取该用户的所有借阅请求，并点击确认或者取消。
  - 接口信息
  - - 提交 创建的借阅请求：提交借阅请求，返回是否借阅成功。
    - 提交 用户名搜索：提交用户名，返回该用户的所有预约请求。
    -  提交 预约信息的确认：提交确认信息，返回是否成功借阅
    - 提交 预约信息的取消：提交确认信息，返回是否成功取消。

- 归还

  - 设计内容
    通过搜索用户的信息，返回该用户的所有借阅记录，通过点击确认归还请求完成归还。
  - 接口内容
    - 提交 用户名：提交搜索的用户名，返回该用户的借阅记录表。
    - 提交 归还确认：提交借阅记录的归还确认。返回是否归还成功。

[1]: asset/manage_design.png

#### 前端API列表

### 2.2. 后端
#### 2.2.1. 技术栈
编程语言：Python3.6.4<br />
Web框架：Django2.0.3<br />
数据库：SQLite3<br />
缓存系统：Memcached<br />
消息队列：RabbitMQ<br />

#### 2.2.2. API总览
路由分发：
```Python
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user_app/', include('user_app.urls')),
    url(r'^manager_app/', include('manager_app.urls')),
]
```
user_app：
```Python
urlpatterns = [
    url(r'^registry/$', views.registry),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^category/(?P<cid>\d+)_(?P<begin>\d+)-(?P<end>\d+)/$', views.category),
    url(r'^detail/(?P<bid>\d+)/$', views.detail),
    url(r'^collect_book/$', views.collect_book),
    url(r'^subscribe_book/$', views.subscribe_book),
    url(r'^star_book/$', views.star_book),
    url(r'^comment_section/(?P<bid>\d+)/$', views.CommentSection.as_view()),
    url(r'^user_profile/(?P<uid>\d+)/$', views.UserProfile.as_view()),
    url(r'^retrieve/$', views.retrieve),
]
```
manager_app：
```Python
urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^manager_info/$', views.manager_info),
    url(r'^report_info_box/$', views.ReportInfoBox.as_view()),
    url(r'^inventory_management/$', views.InventoryManagement.as_view()),
    url(r'^debit/$', views.Debit.as_view()),
    url(r'^return/$', views.Return.as_view()),
]
```

#### 2.2.3. APP：user_app
#### 2.2.3.1. 简介
负责处理从读者服务平台发送过来的请求

#### 2.2.3.2. 功能
1、注册
```
API：user_app/registry/
```
请求（POST）
```Python
{
    'email': '',
    'username': '',
    'password': '',
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：数据格式的合法性由前端来确保。因为将格式检查放在用户的浏览器上进行可以减轻服务器的负担。
</blockquote>

2、登陆
```
API：user_app/login/
```
请求（POST）
```Python
{
    'username': '',
    'password': '',
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
3、登出
```
API：user_app/logout/
```
请求（POST）
```Python
{}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
4、获取某个书籍分类下的条目信息（用户可以处于未登陆状态）
```
API：user_app/category/(?P<cid>\d+)_(?P<begin>\d+)-(?P<end>\d+)/
```
<blockquote>
说明：如果访问user_app/category/3_5-10/，则后端返回数据库分类表中id为3的分类下的编号为5、6、7、8、9的条目。每个条目表示一本书籍，展示的信息包含书的封面、书名、作者、简介和评分。先将条目按书籍的评分高低进行排序再选取。这样做的好处是，前端页面的分页效果可以自由地决定。举例来说，如果是每页8个条目，前端想获取id为3的分类下的第2页的内容，就访问user_app/category/3_9-17/。
</blockquote>

请求（GET）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '',
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg的值是一个经过JSON序列化后的字典。字典中的key是书的id，value也是一个字典，用来表示一个书的条目。value字典的key-value对参考数据库中的书表。
</blockquote>

5、获取某本书的详细信息（用户可以处于未登陆状态）
```
API：user_app/detail/(?P<bid>\d+)/
```
<blockquote>
说明：bid指代书的id。/user_app/detail/3返回的就是id为3的书的详细信息。
</blockquote>

请求（GET）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '', # the message of book
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg的值是一个经过JSON序列化后的字典。其中的key-value对参考数据库中的书表。
</blockquote>

6、收藏
```
API：user_app/collect_book/
```
请求（POST）
```Python
{
    'bid': '', # book's id
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
7、订阅
```
API：user_app/subscribe_book/
```
请求（POST）
```Python
{
    'bid': '', # book's id
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
8、评分
```
API：user_app/star_book/
```
请求（POST）
```Python
{
    'bid': '', # book's id
    'star': '', # range: [1, 5]
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
9、评论区
```
API：user_app/comment_section/(?P<bid>\d+)/
```
<blockquote>
说明：bid指代书的id。/user_app/comment_section/3返回的就是id为3的书对应的评论区信息。
</blockquote>

请求（GET）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '', # information of the comment section
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg的值是一个经过JSON序列化后的（多层嵌套的）字典。形成一个森林结构。
</blockquote>

请求（POST）
```Python
{
    'protocol': '',
    'msg': '',
    'parent': '',
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：protocol取值为'0'时表示发表评论，取值为'1'时代表点赞，取值为'2'时代表踩，取值为'3'时代表举报。msg是评论的内容（只有在protocol的值为'0'时有内容）。parent代表回复、点赞、踩和举报的目标评论id，当评论不是回复别人时，parent取值'0'（数据库表中的id从1开始）。
</blockquote>

10、用户信息
```
API：user_app/user_profile/(?P<uid>\d+)/
```
<blockquote>
说明：uid指代用户的id。/user_app/user_profile/3返回的就是id为3的用户的详细信息。
</blockquote>

请求（GET）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '', # infomation of the user
    'error_msg': '', # notes of failure
}
```
请求（POST）
```Python
{
    'msg': '', # infomation of the user
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg的值是一个经过JSON序列化后的字典。其中的key-value对参考数据库表中的用户表。
</blockquote>

11、检索（用户可以处于未登陆状态）
```
API：user_app/retrieve/
```
请求（GET，user_app/retrieve/?key=xxx）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '', # infomation of the retrieve
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg的值是一个经过JSON序列化后的字典。字典中的key是书的id，value也是一个字典，用来表示一个书的条目。value字典的key-value对参考数据库中的书表。
</blockquote>

#### 2.2.4. APP：manager_app
#### 2.2.3.2. 简介
负责处理从管理员平台发送过来的请求

#### 2.2.3.2. 功能
1、登陆
```
API：manager_app/login/
```
请求（POST）
```Python
{
    'username': '',
    'password': '',
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
2、登出
```
API：user_app/logout/
```
请求（POST）
```Python
{}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
3、获取管理员自己的信息
```
API：manager_app/manager_info/
```
请求（GET）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '',
    'error_msg': '', # notes of failure
}
```
4、举报信息盒
```
API：manager_app/report_info_box/
```
请求（GET）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '{
        '1': '{
            'content': '',
            'report_reasons': '{
                '0': '',
                '1': '',
                '2': '',
                '3': '',
                '4': '',
                '5': '',
                '6': '',
                '7': '',
                '8': '',
            }',
        }',
        '2': ...
    }',
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg的值是一个经过JSON序列化后的字典。字典中的key是被举报的评论的id。字典的value是一个字典，其中'content'对应的value是评论的内容，而'report_reasion'的value又是一个字典。其对应关系如下。这些key对应的value是以该理由举报这条评论的举报人数（用字符串表示数字）。
</blockquote>

```Python
report_reason_choices = (
        (0, u'广告或垃圾信息'),
        (1, u'低俗或色情'),
        (2, u'违反相关法律法规或管理规定'),
        (3, u'辱骂或不友善'),
        (4, u'引战或过于偏激的主观判断'),
        (5, u'泄露他人隐私'),
        (6, u'与作品或讨论区主题无关'),
        (7, u'刷屏'),
        (8, u'其它原因'),
    )
```

请求（POST）
```Python
{
    'protocol': '',
    'cid': '', # comment's id
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：protocol取值为'0'时表示删除评论，取值为'1'时表示删除举报信息。举报信息也用评论的id来索引。
</blockquote>

5、类型管理
```
API：manager_app/type_management/
```
请求（GET，manager_app/type_management/）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '{
        '1': '',
        '2': '',
    }'
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：返回所有的类型信息。msg的key是类型的id，value是对应的类型。
</blockquote>

请求（POST）
```Python
{
    'protocol': '',
    'old': '',
    'new': '',
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：'protocol'取值为'0'时表示增加，'1'时表示删除，'2'时表示修改。增加时，'old'的值为空字符串，'new'的值为要增加的类型名。删除时，'old'的值为要删除的类型名，'new'的值为空字符串。修改时，'old'的值为旧的类型名，'new'的值为新的类型名。
</blockquote>

6、库存管理
```
API：manager_app/inventory_management/
```
请求（GET，manager_app/inventory/?key=xxx）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '{
        '1': '{
            'cover': '',
            'name': '',
            'author': '',
            'score': '',
            'brief': '',
            'ISBN': '',
            'publish_time': '',
            'press': '',
            'contents': '',
            'inventory': '',
            'types': '{
                '1': '',
                '2': ...
            }'
        }',
        '2': ...
    }',
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg的值是一个经过JSON序列化后的字典。字典中的key是书的id，value也是一个字典，用来表示一个书的条目。value字典的key-value对参考数据库中的书表。
</blockquote>

请求（POST）
```Python
{
    'protocol': '',
    'msg': '{
        'cover': '',
        'name': '',
        'author': '',
        'brief': '',
        'ISBN': '',
        'publish_time': '',
        'press': '',
        'contents': '',
        'inventory': '',
        'types': '{
            '1': '',
            '2': ...
        }'
    }',
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：protocol取值为'0'时表示新增条目，取值为'1'时表示修改
</blockquote>


7、借记
```
API：manager_app/debit/
```
请求（GET，manager_app/debit/?username=xxx）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '{
        '1': '{'username': '', 'book': '', 'active_time': ''}',
        '2': '{ ... }',
        ...
    }',
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg包含用户xxx所有的预约请求。'username'就是用户名，'book'是书名，'active_time'是预约的时间。
</blockquote>

请求（POST）
```Python
{
    'msg': '{
        'username': '',
        'bid': '',    # book id
    }',
}
```
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg是一个经过JSON序列化后的字典。
</blockquote>

8、归还
```
API：manager_app/return/
```
请求（GET，manager_app/return/?username=xxx）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '{
        '1': '{'username': '', 'book': '', 'active_time': ''}',
        '2': '{ ... }',
        ...
    }',
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg包含用户xxx所有的借阅记录。'username'就是用户名，'book'是书名，'active_time'是借出的时间。
</blockquote>

请求（POST）
```Python
{
    'rid': '' # record id
}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```

#### 2.2.5. user_app与manager_app之间的交互
