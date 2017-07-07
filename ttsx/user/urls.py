# coding=utf-8
from user import views
from django.conf.urls import url


urlpatterns = [
    # url(r'^index/$',views.index,name='index'),# name是别名，用来跟在命名空间后，拼成url
    url(r'^register/$',views.register,name='register'),
    url(r'^register_check/$',views.register_check, name='register_check'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_check/$',views.login_check,name='login_check'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^user_center_info/$',views.user_center_info,name='user_center_info'),
    url(r'^user_center_order/$',views.user_center_order,name='user_center_order'),
    url(r'^user_center_site/$', views.user_center_site,name='user_center_site'),
    url(r'^add_receive/$',views.add_receive,name='add_receive'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^detail/$',views.detail,name='detail'),
    url(r'^list/$',views.list,name='list'),

]