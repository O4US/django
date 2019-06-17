"""python_crawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import *
from . import view,control
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', view.index),
    url(r'^index$', view.index,name='index'),
    url(r'^movies$', view.movies,name='movies'),
    url(r'^weathers$', view.weathers,name='weathers'),
    url(r'^phones$', view.phones,name='phones'),
    url(r'^insertsearch$', view.insertsearch,name='insertsearch'),
    url(r'^phonesearch$', view.phonesearch,name='phonesearch'),
    url(r'^moviesearch$', view.moviesearch,name='moviesearch'),
    url(r'^weathersearch$', view.weathersearch,name='weathersearch'),
    url(r'^login$', view.login,name='login'),
    url(r'^regist$', view.regist,name='regist'),
    url(r'^control$', view.control,name='control'),

    url(r'^deleteall$', control.deletelall,name='deleteall'),
    url(r'^insertdata$', control.insertdata,name='insertdata'),
    url(r'^updatabase$', control.updatabase,name='updatabase'),
    url(r'^phone_search$', control.search_phone,name='phone_search'),#京东获取手机
    url(r'^loginpost$', control.login,name='loginpost'),#登录
    url(r'^registpost$', control.regist,name='registpost'),#注册
    url(r'^unlogin$', control.unlogin,name='unlogin'),#注销
    url(r'^login12306$', control.login12306,name='login12306'),#登录12306
    url(r'^baike_search$', control.baike_search,name='baike_search'),#百科深度获取
]