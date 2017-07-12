from django.conf.urls import url
import views
urlpatterns = [
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^islogin/$',views.islogin,name='islogin'),
    url(r'^add/$',views.add,name='add'),
    url(r'^count1/$',views.count1,name='count1'),
]