from user import views
from django.conf.urls import url


urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^register/$',views.register),
    url(r'^register_check/$',views.register_check),
    url(r'^login/$', views.login),
    url(r'^login_check/$',views.login_check),
    url(r'user_center_info/$',views.user_center_info),
    url(r'^user_center_order/$',views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),
    # url(r'bottom/$',views.bottom),
    url(r'^cart/$',views.cart),
    url(r'^detail/$',views.detail),
    url(r'^list/$',views.list),

]