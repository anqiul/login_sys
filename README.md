## a django login system
## 这是一个可重用的登录和注册APP

## 简单的使用方法：

---
    创建虚拟环境
    使用pip安装第三方依赖
    修改settings.example.py文件为settings.py
    运行migrate命令，创建数据库和数据表
    运行python manage.py runserver启动服务器
    需要添加css和js文件并配置setting.py
---

路由设置：

```python
from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
    path('captcha/', include('captcha.urls'))   # 增加这一行
]

```
<a href="https://www.liujiangblog.com/course/django/">参考</a>