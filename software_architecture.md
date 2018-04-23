# 软件架构
## 1. 总体设计
![](https://raw.githubusercontent.com/ProgressOfSAD/Dashboard/master/asset/overall_design.png)

## 2. 详细设计
### 2.1. 前端

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
1、注册<br />
API：user_app/registry/<br />
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

2、登陆<br />
API：user_app/login/<br />
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
3、登出<br />
API：user_app/logout/<br />
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
4、获取某个书籍分类下的条目信息（用户可以处于未登陆状态）<br />
API：user_app/category/(?P<cid>\d+)_(?P<begin>\d+)-(?P<end>\d+)/<br />
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
说明：msg的值是一个字符串化的字典。字典中的key是书的id，value也是一个字典，用来表示一个书的条目。value字典的key-value对参考数据库中的书表。
</blockquote>

5、获取某本书的详细信息（用户可以处于未登陆状态）<br />
API：user_app/detail/(?P<bid>\d+)/<br />
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
说明：msg的值是一个字符串化的字典。其中的key-value对参考数据库中的书表。
</blockquote>

6、收藏<br />
API：user_app/collect_book/<br />
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
7、订阅<br />
API：user_app/subscribe_book/<br />
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
8、评分<br />
API：user_app/star_book/<br />
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
9、评论区<br />
API：user_app/comment_section/(?P<bid>\d+)/<br />
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
说明：msg的值是一个字符串化的（多层嵌套的）字典。形成一个森林结构。
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

10、用户信息<br />
API：user_app/user_profile/(?P<uid>\d+)/<br />
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
说明：msg的值是一个字符串化的字典。其中的key-value对参考数据库表中的用户表。
</blockquote>

11、检索（用户可以处于未登陆状态）<br />
API：user_app/retrieve/<br />
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
说明：msg的值是一个字符串化的字典。字典中的key是书的id，value也是一个字典，用来表示一个书的条目。value字典的key-value对参考数据库中的书表。
</blockquote>

#### 2.2.4. APP：manager_app
#### 2.2.3.2. 简介
负责处理从管理员平台发送过来的请求

#### 2.2.3.2. 功能
1、登陆<br />
API：user_app/login/<br />
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
2、登出<br />
API：user_app/logout/<br />
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
3、获取管理员自己的信息<br />
API：manager_app/manager_info/<br />
请求（GET）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '',
    'error_msg': '', # notes of failure
}
```
4、举报信息盒<br />
API：manager_app/report_info_box/<br />
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
说明：msg的值是一个字符串化的字典。字典中的key是被举报的评论的id，value是举报的理由。
</blockquote>

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

5、库存管理<br />
API：manager_app/inventory_management/<br />
请求（GET，manager_app/inventory/?key=xxx）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '', # infomation of the retrieve
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg的值是一个字符串化的字典。字典中的key是书的id，value也是一个字典，用来表示一个书的条目。value字典的key-value对参考数据库中的书表。
</blockquote>

请求（POST）
```Python
{
    'protocol': '',
    'msg': '',
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


6、借记
API：manager_app/debit/<br />
请求（GET，manager_app/debit/?username=xxx）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '',
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg包含用户xxx所有的预约请求。
</blockquote>

请求（POST）
```Python
{
    'msg': '',
}
```
```Python
{
    'status': '', # 'success' or 'failure'
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg是一个字符串化的字典。具体内容参考数据库中借书登记表。
</blockquote>

7、归还<br />
API：manager_app/return/<br />
请求（GET，manager_app/return/?username=xxx）<br />
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '',
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg包含用户xxx所有的借阅记录。
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
