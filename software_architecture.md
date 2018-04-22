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
    url(r'^comment_section/$', views.CommentSection.as_view()),
    url(r'^user_profile/$', views.UserProfile.as_view()),
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

请求（GET）
```Python
{}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '',
    'error_msg': '', # notes of failure
}
```
<blockquote>
说明：msg的value是一个字典，字典中的每个值代表一本书。
</blockquote>

5、获取某本书的详细信息（用户可以处于未登陆状态）<br />
API：user_app/detail/(?P<bid>\d+)/<br />
请求（GET）
```Python
{}
```
响应
```Python
{
    'status': '', # 'success' or 'failure'
    'msg': '', # the message of book
    'error_msg': '', # notes of failure
}
```
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
API：user_app/comment_section/<br />
10、用户信息<br />
API：user_app/user_profile/<br />
11、检索（用户可以处于未登陆状态）<br />
API：user_app/retrieve/<br />
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
    'status': '',
    'error_msg': '',
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
    'status': '',
    'error_msg': '',
}
```
3、获取管理员自己的信息<br />
API：manager_app/manager_info/<br />
请求（GET）<br />
响应
```Python
{
    'status': '',
    'msg': '',
    'error_msg': '',
}
```
4、举报信息管理<br />
API：manager_app/report_info_box/<br />
5、库存管理<br />
API：manager_app/inventory_management/<br />
6、借记
API：manager_app/debit/<br />
7、归还<br />
API：manager_app/return/<br />
#### 2.2.5. user_app与manager_app之间的交互
