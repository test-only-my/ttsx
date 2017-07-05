from user import views
from django.conf.urls import url


urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^register/$',views.register),
    url(r'^register_check/$',views.register_check),
    # url(r'register_user/$',views.register_user),
    url(r'^login/$', views.login),
    url(r'^login_check/$',views.login_check),
    # url(r'bottom/$',views.bottom),
    url(r'^cart/$',views.cart),
    url(r'^detail/$',views.detail),
    url(r'^list/$',views.list),
    url(r'^user_center_site/$',views.user_center_site),
]